
# proportion of Fe3+
proportion_Fe3 = 0.28


# error of T and p
E_A_T = 33 # T error of cpx-melt
E_A_p = 1.7 # p error of cpx-melt
E_B_T = 36 # T error of Si activity
E_B_p = 2.0 # p error of Si activity


# size of discretization unit
# if the range is larger, use 10 times dx and dy, otherwise 4
d_x = 0.5
d_y = 0.05


# H2O range
H2O_begin = 3.6
H2O_end = 5.5
H2O_interval = 0.01

# H2O_begin = 0.0
# H2O_end = 10.0
# H2O_interval = 0.1


# molar mass
# do not change the default values
M = {
	"SiO2": 60.09,
	"TiO2": 79.87,
	"Al2O3": 101.96,
	"Fe2O3": 159.69,
	"MnO": 70.94,
	"MgO": 40.30,
	"CaO": 56.08,
	"Na2O": 61.98,
	"K2O": 94.20,
	"P2O5": 141.94,
	"H2O": 18.02,
}

