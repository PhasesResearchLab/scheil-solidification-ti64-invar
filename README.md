[![DOI](https://zenodo.org/badge/237029581.svg)](https://zenodo.org/badge/latestdoi/237029581)

## Installing

Follow the instructions for installing the `scheil` package in the [scheil documentation](http://scheil.readthedocs.io). Requires `scheil >= 0.1.2`.

## Reproducing the results

The `scheil` notebook in this repo contains the code to reproduce the Scheil-Gulliver calculation figures in [link to arxiv paper].

The notebook is split up into several main parts:

1. Calculation of a point grid. The Fe-Ni-Ti system can be unusually tricky to converge, in most cases this is not necessary, but doing this can speed up the speed and accuracy of equilibrium calculations.
2. Simulation of Scheil-Gulliver and equilibrium solidification for each studied composition.
3. Simulation of Scheil-Gulliver and equilibrium solidification along the path of the gradient.

### Running
The notebook should be run in the top level directory, or at least one that includes the `helper.py` file and the Fe-Ni-Ti TDB.

The Fe-Ni-Ti parameters are taken from J. De Keyzer, G. Cacciamani, N. Dupin, P. Wollants, Thermodynamic modeling and optimization of the Fe–Ni–Ti system, *Calphad*. 33 (2009) 109–123. doi:[10.1016/j.calphad.2008.10.003](https://10.1016/j.calphad.2008.10.003).

### Results
The notebook will create (or update) the `results` directory with saved JSON data from the Scheil-Gulliver solidification simulations and the produced figures.
If you want to reproduce the results from scratch, just remote the `results` directory.


## Citing

To cite this work, please cite the relevant version. The following DOI, [doi:10.5281/zenodo.3630599](https://doi.org/10.5281/zenodo.3630599), will link to the latest version of the code on Zenodo where you can cite the specific version that you haved used. For example, version 1.0 can be cited as:


`Brandon Bocklund, Lourdes D. Bobbio, Richard A. Otis, Allison M. Beese, & Zi-Kui Liu. (2020, January 29). PhasesResearchLab/scheil-solidification-ti64-invar: 1.0 (Version 1.0). Zenodo. http://doi.org/10.5281/zenodo.3630600`

```
@software{brandon_bocklund_2020_3630600,
  author       = {Brandon Bocklund and
                  Lourdes D. Bobbio and
                  Richard A. Otis and
                  Allison M. Beese and
                  Zi-Kui Liu},
  title        = {{PhasesResearchLab/scheil-solidification-
                   ti64-invar: 1.0}},
  month        = jan,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.3630600},
  url          = {https://doi.org/10.5281/zenodo.3630600}
}
```

## License

Code (`.py` and `.ipynb` files) in this repository are MIT licensed.
