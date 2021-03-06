# BOA calculation
A discretization method of calculating the buffer overlapping area (BOA) of two buffers in P-T space (Di et al. 2020, American Mineralogist, 105, 149).

Requirements:
Python 2, numpy, and matplotlib


The input data should be like:

primary melt composition:
# SiO2 TiO2 Al2O3 TFe2O3 MgO CaO Na2O K2O P2O5 TOTAL
52.74 	2.45 	13.88 	8.49 	0.11 	6.17 	5.50 	3.86 	5.53 	99.69 

...

(The order of the species does not matter, while all the species must be included. The input primary melt compositions should be in equlibrium with olivine + orthopyroxene)

cpx-melt P-T:
# T p
1051.29405	2.04854

...

(the unit of T: °C, the unit of p: kbar. The input P-T should be from equilibrated cpx-melt pairs.)


Manual:
1. Click the green button "clone or download" to get the whole repository into a local device.
2. Make sure that Python 2 has been already installed, as well as numpy and matplotlib.
3. Copy and Paste your primary melt composition and cpx-melt P-T data into ./data/primary_melt_composition.txt and ./data/cpx_melt.txt, respectively.
4. Change the parameters in config.py. The changeable parameters include a melt Fe3+ proportion (Fe3+/FeT), errors of the thermobarometers, intended H2O content range and increment, and the size of unit.
5. Run "python demo.py" to get the outcome.
6. The outcome is a figure showing a scatter of H2O content (.wt%) and BOA as well as printing them on the screen.
