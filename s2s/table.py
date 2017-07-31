#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
#from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan, mean

#######################################
import prob_area
import prob_time
# import figure
#######################################
"""
Each variable should have botton and top limits to calculate the alert level, as also the limit for indecision, where the alert color should be truncated (ex: whem max prob is below X%, set color to y).
 
"""
###############################################################################
#GFS
def DATA_gfs_table(ens1, ens2, time, ixGFS, iyGFS, date0, utc0, TOP, BOT, PRO):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, ixGFS, iyGFS, TOP, BOT)

	color	= []
	value	= []
	prob	= []
	date	= []
	mini	= []
	maxi	= []

	b = 0
	for i in range(0, max_i):
		max_v		= max(max_t1[i], max_a1[i])
		min_v		= min(min_t1[i], min_a1[i])
		prob_a_g	= np.mean(prob_a_g1[i])
		prob_t_g 	= np.mean(prob_t_g1[i])
		prob_a_r 	= np.mean(prob_a_r1[i])
		prob_t_r	= np.mean(prob_t_r1[i])
		prob_a_y	= np.mean(prob_a_y1[i])
		prob_t_y	= np.mean(prob_t_y1[i])
		value_a		= np.mean(value_a1[i])
		value_t 	= np.mean(value_t1[i])

		prob_g	= ((2*prob_t_g + prob_a_g)/3)
		prob_r	= ((2*prob_t_r + prob_a_r)/3)
		prob_y	= ((2*prob_t_y + prob_a_y)/3)

		prob_c	= [prob_g, prob_r, prob_y]

		if prob_c[np.argmax(prob_c)] < PRO:
			color.append(2)
			result_prov = ((((2*value_t  +  value_a)/3) + max_v + min_v)/3)
			result_prov = np.around(result_prov, decimals=1)
			if result_prov < 1 and result_prov > 0:
				result_prov = int((result_prov * 10))/10.0
			else:
				result_prov = int(result_prov)
		else:
			color.append((np.argmax(prob_c) + 1))
			result_prov = ((2*value_t  +  value_a)/3)
			result_prov = np.around(result_prov, decimals=1)
			# if result_prov < 1 and result_prov > 0:
			# 	result_prov = int((result_prov * 10))/10.0
			# else:
			# 	result_prov = int(result_prov)

		value.append(result_prov)
		prob.append(prob_c[np.argmax(prob_c)])		
		maxi.append(max_v)
		mini.append(min_v)
		if b <= max_i - 24:
			d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = b) + datetime.timedelta(hours = utc0)
			b += 1
		else:
			d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = b) + datetime.timedelta(hours = utc0)
			b += 4

		date.append(d1)
	return(date, prob, color, value, maxi, mini)	

###############################################################################
#WRF
def DATA_wrf_table(ens1, ens2, time, ixWRF, iyWRF, date0, utc0, TOP, BOT, PRO):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens2, time, 24, ixWRF, iyWRF, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, ixWRF, iyWRF, TOP, BOT)

	color	= []
	value	= []
	prob	= []
	date	= []
	mini	= []
	maxi	= []
	fig		= []

	for i in range(0, max_i):
		max_v		= max(max_t1[i], max_a1[i])
		min_v		= min(min_t1[i], min_a1[i])
		prob_a_g	= np.mean(prob_a_g1[i])
		prob_t_g 	= np.mean(prob_t_g1[i])
		prob_a_r 	= np.mean(prob_a_r1[i])
		prob_t_r	= np.mean(prob_t_r1[i])
		prob_a_y	= np.mean(prob_a_y1[i])
		prob_t_y	= np.mean(prob_t_y1[i])
		value_a		= np.mean(value_a1[i])
		value_t 	= np.mean(value_t1[i])

		prob_g	= ((2*prob_t_g + prob_a_g)/3)
		prob_r	= ((2*prob_t_r + prob_a_r)/3)
		prob_y	= ((2*prob_t_y + prob_a_y)/3)

		prob_c	= [prob_g, prob_r, prob_y]

		if prob_c[np.argmax(prob_c)] < PRO:
			color.append(2)
			result_prov = ((((2*value_t  +  value_a)/3) + max_v + min_v)/3)
			result_prov = np.around(result_prov, decimals=1)
			if result_prov < 1 and result_prov > 0:
				result_prov = int((result_prov * 10))/10.0
			else:
				result_prov = int(result_prov)
		else:
			color.append((np.argmax(prob_c) + 1))
			result_prov = ((2*value_t  +  value_a)/3)
			result_prov = np.around(result_prov, decimals=1)
			# if result_prov < 1 and result_prov > 0:
			# 	result_prov = int((result_prov * 10))/10.0
			# else:
			# 	result_prov = int(result_prov)

		value.append(result_prov)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = i) + datetime.timedelta(hours = utc0)
		prob.append(prob_c[np.argmax(prob_c)])		
		maxi.append(max_v)
		mini.append(min_v)
		date.append(d1)

	return(date, prob, color, value, maxi, mini)	

###############################################################################
