#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan, mean

#######################################
import prob_area
import prob_time
#######################################
"""
Each variable should have botton and top limits to calculate the alert level, as also the limit for indecision, where the alert color should be truncated (ex: whem max prob is below X%, set color to y).
 

"""
VAR = 'chuva'
TOP = 
BOT = 
PRO = 

def calendario(CFS_E1, CFS_E2, CFS_E3, CFS_E4, CFS_E5, CFS_E6, CFS_E7, CFS_E8, iz, ixCFS, iyCFS, date0, utc0):
	ens1 = netCDF4.Dataset(CFS_E1, 'r')
	ens2 = netCDF4.Dataset(CFS_E2, 'r')
	ens3 = netCDF4.Dataset(CFS_E3, 'r')
	ens4 = netCDF4.Dataset(CFS_E4, 'r')
	ens5 = netCDF4.Dataset(CFS_E5, 'r')
	ens6 = netCDF4.Dataset(CFS_E6, 'r')
	ens7 = netCDF4.Dataset(CFS_E7, 'r')
	ens8 = netCDF4.Dataset(CFS_E8, 'r')
	time = ens1.variables['time']
	max_i = len(time)
	
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens5, VAR, ixCFS, iyCFS, TOP, BOT) 
	prob_t_g2, prob_t_r2, prob_t_y2, value_t2, max_t2, min_t2 = prob_time._get_TIMEP(ens2, ens6, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_t_g3, prob_t_r3, prob_t_y3, value_t3, max_t3, min_t3 = prob_time._get_TIMEP(ens3, ens7, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_t_g4, prob_t_r4, prob_t_y4, value_t4, max_t4, min_t4 = prob_time._get_TIMEP(ens4, ens8, VAR, ixCFS, iyCFS, TOP, BOT)


	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_a_g2, prob_a_r2, prob_a_y2, value_a2, max_a2, min_a2 = prob_area._get_AREAP(ens1, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_a_g3, prob_a_r3, prob_a_y3, value_a3, max_a3, min_a3 = prob_area._get_AREAP(ens1, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_a_g4, prob_a_r4, prob_a_y4, value_a4, max_a4, min_a4 = prob_area._get_AREAP(ens1, VAR, ixCFS, iyCFS, TOP, BOT)

	a = 0
	b = 4
	for i in range(0, max_i//4):
		max_v = max(max_t1[a:b], max_t2[a:b], max_t3[a:b], max_t4[a:b], max_a1[a:b], max_a2[a:b], max_a3[a:b], max_a4[a:b])
		min_v = min(min_t1[a:b], min_t2[a:b], min_t3[a:b], min_t4[a:b], min_a1[a:b], min_a2[a:b], min_a3[a:b], min_a4[a:b])

		prob_a_g = (np.mean(prob_a_g1[a:b]) + np.mean(prob_a_g2[a:b]) + np.mean(prob_a_g3[a:b]) + np.mean(prob_a_g4[a:b]))/4
		prob_t_g = (np.mean(prob_t_g1[a:b]) + np.mean(prob_t_g2[a:b]) + np.mean(prob_t_g3[a:b]) + np.mean(prob_t_g4[a:b]))/4

		prob_a_r = (np.mean(prob_a_r1[a:b]) + np.mean(prob_a_r2[a:b]) + np.mean(prob_a_r3[a:b]) + np.mean(prob_a_r4[a:b]))/4
		prob_t_r = (np.mean(prob_t_r1[a:b]) + np.mean(prob_t_r2[a:b]) + np.mean(prob_t_r3[a:b]) + np.mean(prob_t_r4[a:b]))/4

		prob_a_y = (np.mean(prob_a_y1[a:b]) + np.mean(prob_a_y2[a:b]) + np.mean(prob_a_y3[a:b]) + np.mean(prob_a_y4[a:b]))/4
		prob_t_y = (np.mean(prob_t_y1[a:b]) + np.mean(prob_t_y2[a:b]) + np.mean(prob_t_y3[a:b]) + np.mean(prob_t_y4[a:b]))/4

		value_a = (np.mean(value_a1[a:b]) + np.mean(value_a2[a:b]) + np.mean(value_a3[a:b]) + np.mean(value_a4[a:b]))/4
		value_t = (np.mean(value_t1[a:b]) + np.mean(value_t2[a:b]) + np.mean(value_t3[a:b]) + np.mean(value_t4[a:b]))/4

		prob_g = ((2*prob_t_g + prob_a_g)/3)
		prob_r = ((2*prob_t_r + prob_a_r)/3)
		prob_y = ((2*prob_t_y + prob_a_y)/3)

		prob_c = [prob_g, prob_r, prob_y]

### needs a condition if argmax(prob_c) < PRO:  and a elif 


		if prob_c[argmax(prob_c)] < PRO:
			color.append(2)
			value.append((((2*value_t  +  value_a)/3) + (max(max_v) + min(min_v)))/3)
			
		else:
			color.append((argmax(prob_c) + 1))
			value.append((2*value_t  +  value_a)/3)
		prob.append(prob_c[argmax(prob_c)])		
		maxi.append(max(max_v))
		mini.append(min(min_v))
		a += 4
		b += 4


return(date, prob, color, value, max_v, min_v)




