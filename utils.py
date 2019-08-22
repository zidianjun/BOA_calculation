
import numpy as np
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__) ) ) )
import config

def cal_overlap_area(x1_array, y1_array, x2_array, y2_array,
					 xerr1, yerr1, xerr2, yerr2,
					 left, right, down, up):
	area_total = 0
	unit_coefficient = 10 if config.H2O_end - config.H2O_begin > 5 else 4
	d_x = config.d_x * unit_coefficient
	d_y = config.d_y * unit_coefficient
	d_area = d_x * d_y
	for i in np.arange(left, right, d_x):
		for j in np.arange(down, up, d_y):
			flag = 0
			for m in range(len(x1_array)):
				for n in range(len(x2_array)):
					if (abs(i - x1_array[m]) < xerr1
						and j < y1_array[m] + yerr1 * np.sqrt(1 - (i - x1_array[m]) ** 2 / xerr1 ** 2)
						and j > y1_array[m] - yerr1 * np.sqrt(1 - (i - x1_array[m]) ** 2 / xerr1 ** 2)
						and abs(i - x2_array[n]) < xerr2
						and j < y2_array[n] + yerr2 * np.sqrt(1 - (i - x2_array[n]) ** 2 / xerr2 ** 2)
						and j > y2_array[n] - yerr2 * np.sqrt(1 - (i - x2_array[n]) ** 2 / xerr2 ** 2)):
						area_total += d_area
						flag = 1 # to make sure each unit will only be counted once
						break
				if flag == 1:
					break
	return area_total

def cal_m_SiO2(array):
	return [element / config.M["SiO2"] for element in array]

def cal_m_TiO2(array):
	return [element / config.M["TiO2"] for element in array]

def cal_m_Al2O3(array):
	return [element / config.M["Al2O3"] for element in array]

def cal_m_Fe2O3(array):
	return [element / config.M["Fe2O3"] * 2 * config.proportion_Fe3 / 2 for element in array]

def cal_m_FeO(array):
	return [element / config.M["Fe2O3"] * 2 * (1 - config.proportion_Fe3) for element in array]

def cal_m_MnO(array):
	return [element / config.M["MnO"] for element in array]

def cal_m_MgO(array):
	return [element / config.M["MgO"] for element in array]

def cal_m_CaO(array):
	return [element / config.M["CaO"] for element in array]

def cal_m_Na2O(array):
	return [element / config.M["Na2O"] for element in array]

def cal_m_K2O(array):
	return [element / config.M["K2O"] for element in array]

def cal_m_P2O5(array):
	return [element / config.M["P2O5"] for element in array]

def cal_m_H2O(array, percent_H2O):
	return [percent_H2O * 0.01 * element / (1 - percent_H2O * 0.01) / config.M["H2O"] for element in array]

def cal_specie_m_Si4O8(m_SiO2, m_FeO, m_MgO, m_CaO, m_Na2O, m_K2O):
	specie_m_SiO2 = []
	for i in range(len(m_SiO2)):
		specie_m_SiO2.append(0.25 * (m_SiO2[i] - 0.5 * (m_FeO[i] + m_MgO[i] + m_CaO[i]) - m_Na2O[i] - m_K2O[i]))
	return filter(None, specie_m_SiO2)

def cal_specie_m_Ti4O8(m_TiO2):
	return [0.25 * element for element in m_TiO2]

def cal_specie_m_Al16_3O8(m_Al2O3, m_Na2O):
	specie_m_Al16_3O8 = []
	for i in range(len(m_Al2O3)):
		specie_m_Al16_3O8.append(0.375 * (m_Al2O3[i] - m_Na2O[i]))
	return filter(None, specie_m_Al16_3O8)

def cal_specie_m_Fe16_3O8(m_Fe2O3):
	return [0.375 * element for element in m_Fe2O3]

def cal_specie_m_Fe4Si2O8(m_FeO):
	return [0.25 * element for element in m_FeO]

def cal_specie_m_Mg4Si2O8(m_MgO):
	return [0.25 * element for element in m_MgO]

def cal_specie_m_Ca4Si2O8(m_CaO):
	return [0.25 * element for element in m_CaO]

def cal_specie_m_Na2Al2Si2O8(m_Na2O):
	return [element for element in m_Na2O]

def cal_specie_m_K2Al2Si2O8(m_K2O):
	return [element for element in m_K2O]

def cal_specie_m_P16_5O8(m_P2O5):
	return [0.625 * element for element in m_P2O5]

def cal_specie_m_H16O8(m_H2O):
	return [0.125 * element for element in m_H2O]

def cal_t_p(percent_H2O, primary_data):
	m_SiO2 = cal_m_SiO2(primary_data["SiO2"])
	m_TiO2 = cal_m_TiO2(primary_data["TiO2"])
	m_Al2O3 = cal_m_Al2O3(primary_data["Al2O3"])
	m_Fe2O3 = cal_m_Fe2O3(primary_data["TFe2O3"])
	m_FeO = cal_m_FeO(primary_data["TFe2O3"])
	m_MgO = cal_m_MgO(primary_data["MgO"])
	m_CaO = cal_m_CaO(primary_data["CaO"])
	m_Na2O = cal_m_Na2O(primary_data["Na2O"])
	m_K2O = cal_m_K2O(primary_data["K2O"])
	m_P2O5 = cal_m_P2O5(primary_data["P2O5"])
	m_H2O = cal_m_H2O(primary_data["TOTAL"], percent_H2O)

	total = []
	specie_m_SiO2 = cal_specie_m_Si4O8(m_SiO2, m_FeO, m_MgO, m_CaO, m_Na2O, m_K2O)
	total.append(specie_m_SiO2)
	specie_m_Ti4O8 = cal_specie_m_Ti4O8(m_TiO2)
	total.append(specie_m_Ti4O8)
	specie_m_Al16_3O8 = cal_specie_m_Al16_3O8(m_Al2O3, m_Na2O)
	total.append(specie_m_Al16_3O8)
	specie_m_Fe16_3O8 = cal_specie_m_Fe16_3O8(m_Fe2O3)
	total.append(specie_m_Fe16_3O8)
	specie_m_Fe4Si2O8 = cal_specie_m_Fe4Si2O8(m_FeO)
	total.append(specie_m_Fe4Si2O8)
	specie_m_Mg4Si2O8 = cal_specie_m_Mg4Si2O8(m_MgO)
	total.append(specie_m_Mg4Si2O8)
	specie_m_Ca4Si2O8 = cal_specie_m_Ca4Si2O8(m_CaO)
	total.append(specie_m_Ca4Si2O8)
	specie_m_Na2Al2Si2O8 = cal_specie_m_Na2Al2Si2O8(m_Na2O)
	total.append(specie_m_Na2Al2Si2O8)
	specie_m_K2Al2Si2O8 = cal_specie_m_K2Al2Si2O8(m_K2O)
	total.append(specie_m_K2Al2Si2O8)
	specie_m_P16_5O8 = cal_specie_m_P16_5O8(m_P2O5)
	total.append(specie_m_P16_5O8)
	specie_m_H16O8 = cal_specie_m_H16O8(m_H2O)
	total.append(specie_m_H16O8)

	total = np.transpose(filter(None, total))
	# concatenate the sum at the end of each row
	Total = np.concatenate((total, np.sum(total, axis=1)[np.newaxis, :].T), axis=1)

	Nrow, Ncol = Total.shape
	for i in range(Nrow): # normalize each row as sum equals 100
		norm = 100 / Total[i][-1]
		for j in range(Ncol):
			Total[i][j] = Total[i][j] * norm

	temperature = []
	pressure = []
	for i in range(Nrow): # Equation 3 in Lee et al. (2009)
		temperature.append(916.45 + 13.68 * Total[i][5] + 4580 /
						   Total[i][0] - 0.509 * Total[i][10] * Total[i][5])
	filter(None, temperature)
	for i in range(Nrow): # Equation 2 in Lee et al. (2009)
		pressure.append(10 * (np.log(Total[i][0]) - 4.019 + 0.0165 * Total[i][4] + 0.0005 * Total[i][6] ** 2) /
						(-770 * (temperature[i] + 273.15) ** (-1) + 0.0058 * (temperature[i] + 273.15) ** 0.5 - 0.003 * Total[i][10]))

	return temperature, pressure
