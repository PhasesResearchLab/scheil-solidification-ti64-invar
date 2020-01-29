## Installing

Follow the instructions for installing the `scheil` package in the [scheil documentation](http://scheil.readthedocs.io)

## Running

The `scheil` notebook in this repo contains the code to reproduce the Scheil-Gulliver calculation figures in [link to arxiv paper].

The notebook is split up into several main parts:

1. Calculation of a point grid. The Fe-Ni-Ti system can be unusually tricky to converge, in most cases this is not necessary, but doing this can speed up the speed and accuracy of equilibrium calculations.
2. Simulation of Scheil-Gulliver and equilibrium solidification for each studied composition.
3. Simulation of Scheil-Gulliver and equilibrium solidification along the path of the gradient.

The notebook should be run in the top level directory, or at least one that includes the `helper.py` file and the Fe-Ni-Ti TDB. It will create (or update) the `results` directory with saved JSON data from the Scheil-Gulliver solidification simulations and the produced figures.

The Fe-Ni-Ti parameters are taken from J. De Keyzer, G. Cacciamani, N. Dupin, P. Wollants, Thermodynamic modeling and optimization of the Fe–Ni–Ti system, *Calphad*. 33 (2009) 109–123. doi:[10.1016/j.calphad.2008.10.003](https://10.1016/j.calphad.2008.10.003).
