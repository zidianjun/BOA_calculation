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
# T/°C   p/kbar
1051.29405	2.04854
...


Directly run "python demo.py" to get the results.

When changing the parameters such as the propotion of Fe3+ and the errors of the measurements, simply go to config.py.
