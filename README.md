# BOA calculation
A discretization method of calculating the buffer overlapping area (BOA) of two buffers in P-T space.

Requirements:
numpy and matplotlib


The input data should be like:

primary melt composition:
# SiO2 TiO2 Al2O3 TFe2O3 MgO CaO Na2O K2O P2O5 TOTAL
52.74 	2.45 	13.88 	8.49 	0.11 	6.17 	5.50 	3.86 	5.53 	1.00 	99.69 
...

(The order of the species does not matter, while all the species must be included.)

cpx-melt P-T:
# T p
1051.29405	2.04854
...

(the unit of T: °C, the unit of p: kbar)


Manual:
1. Click the green button "clone or download" to get the whole repository into a local device.
2. Make sure Python 2 has been already installed.
3. Copy and Paste your primary melt composition and cpx-melt data into ./data/primary_melt_composition.txt and ./data/cpx_melt.txt, respectively.
4. Change the parameters in config.py, e.g. the propotion of Fe3+ and the errors of the measurements. Our default parameters are shown in Di et al. (2019).
5. Run "python demo.py" to get the outcome.
6. The outcome is a figure showing a scatter of H2O content (.wt%) and BOA.
