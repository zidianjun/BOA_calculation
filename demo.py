#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__) ) ) )
import config
import utils

if __name__ == "__main__":
	primary_data = np.genfromtxt('./data/primary_data.txt', names=True)
	group_A = np.genfromtxt('./data/group_A.txt', names=True)

	trend = []
	for percent_H2O in np.arange(config.H2O_begin, config.H2O_end, config.H2O_interval):
		temperature, pressure = utils.cal_t_p(percent_H2O, primary_data)
		left = min(temperature) - config.E_B_T
		right = max(group_A["T"]) + config.E_A_T
		down = min(pressure) - config.E_B_p
		up = max(group_A["p"]) + config.E_A_p
		area = utils.cal_overlap_area(group_A["T"], group_A["p"], temperature, pressure,
									  config.E_A_T, config.E_A_p, config.E_B_T, config.E_B_p,
									  left, right, down, up)
		trend.append([percent_H2O, area])
		print('%s, %s' %(round(percent_H2O, 2), round(area, 2)))

	plt.scatter(np.array(trend)[:, 0], np.array(trend)[:, 1], color = 'k')
	plt.xlabel('H2O wt.%')
	plt.ylabel('overlap degree')
	plt.show()
