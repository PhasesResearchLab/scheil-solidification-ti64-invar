# Add points manually to the convex hull

import numpy as np
from pycalphad.core.utils import generate_dof, unpack_components
from pycalphad import calculate, equilibrium
from scheil.utils import local_sample


def sample_phase_points(dbf, comps, phase_name, conditions, calc_pdens, pdens):
    """Sample new points from a phase around the single phase equilibrium site fractions at the given conditions.

    Parameters
    ----------
    dbf :

    comps :

    phase_name :

    conditions :

    calc_pdens :
        The point density passed to calculate for the nominal points added.
    pdens : int
        The number of points to add in the local sampling at each set of equilibrium site fractions.

    Returns
    -------
    np.ndarray[:,:]

    """
    _, subl_dof = generate_dof(dbf.phases[phase_name], unpack_components(dbf, comps))
    # subl_dof is number of species in each sublattice, e.g. (FE,NI,TI)(FE,NI)(FE,NI,TI) is [3, 2, 3]
    eqgrid = equilibrium(dbf, comps, [phase_name], conditions)
    all_eq_pts = eqgrid.Y.values[eqgrid.Phase.values == phase_name]
    # sample points locally
    additional_points = local_sample(all_eq_pts, subl_dof, pdens)
    # get the grid between endmembers and random point sampling from calculate
    pts_calc = calculate(dbf, comps, phase_name, pdens=calc_pdens, P=101325, T=300, N=1).Y.values.squeeze()
    return np.concatenate([additional_points, pts_calc], axis=0)


# Weight fractions in pycalphad
from pycalphad import variables as v
from pycalphad.variables import Species, StateVariable
class WeightFraction(StateVariable):
    """
    Weight fractions are symbols with built-in assumptions of being real and nonnegative.
    """
    def __new__(cls, *args): #pylint: disable=W0221
        new_self = None
        varname = None
        phase_name = None
        species = None
        if len(args) == 1:
            # this is an overall composition variable
            species = Species(args[0])
            varname = 'W_' + species.escaped_name.upper()
        elif len(args) == 2:
            # this is a phase-specific composition variable
            phase_name = args[0].upper()
            species = Species(args[1])
            varname = 'W_' + phase_name + '_' + species.escaped_name.upper()
        else:
            # not defined
            raise ValueError('Weight fraction not defined for args: '+args)

        #pylint: disable=E1121
        new_self = StateVariable.__new__(cls, varname, nonnegative=True)
        new_self.phase_name = phase_name
        new_self.species = species
        return new_self

    def __getnewargs__(self):
        if self.phase_name is not None:
            return self.phase_name, self.species
        else:
            return self.species,

    def _latex(self, printer=None):
        "LaTeX representation."
        #pylint: disable=E1101
        if self.phase_name:
            return 'w^{'+self.phase_name.replace('_', '-') + \
                '}_{'+self.species.escaped_name+'}'
        else:
            return 'w_{'+self.species.escaped_name+'}'


v.W = WeightFraction
def W_to_X(indep_weights, dbf, comps):
    # TODO: enable mass computation for a species, not just the pure elements in the database
    # TODO: extend to arrays of independent components
    comps = set(comps) - {'VA'}
    dep_weights = {wvar.species.name: weight for wvar, weight in indep_weights.items()}
    indep_comps = set(dep_weights.keys())
    dep_components = list(comps.difference(indep_comps))
    assert len(dep_components) == 1
    dep_weights[dep_components[0]] = 1-sum(dep_weights.values())
    N_i = {sp: dep_weights[sp]/dbf.refstates[sp]['mass'] for sp in dep_weights.keys()}
    X_i = {v.X(sp): N_i[sp]/sum(N_i.values()) for sp in dep_weights.keys()}
    del X_i[v.X(dep_components[0])]
    return X_i


# Interpolate compositions (as pycalphad variables)
def comp_interp(xold, xnew, mix=1.0):
    """Interpolate between two compositions by mixing them.

    Mix controls how much of the new composition to add.  A mix of 1.0 means
    to discard the old step completely and a mix of 0 means to discard the
    new step completely (note a mix of of 0 therefore means the composition
    will never change).
    """
    newcomp = {}
    for c in xold.keys():
        newcomp[c] = xold[c] + (xnew[c] - xold[c])*mix
    return newcomp