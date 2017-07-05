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
	fig		= []

	# a = 0
	# b = 24
	b = 0
	for i in range(0, max_i):

		max_v		= max(max_t1[i], max_a1[i])
		min_v		= min(min_t1[i], min_a1[i])

		prob_a_g	= (np.mean(prob_a_g1[i]) + np.mean(prob_a_g2[i]))/2
		prob_t_g 	= (np.mean(prob_t_g1[i]) + np.mean(prob_t_g2[i]))/2

		prob_a_r 	= (np.mean(prob_a_r1[i]) + np.mean(prob_a_r2[i]))/2
		prob_t_r	= (np.mean(prob_t_r1[i]) + np.mean(prob_t_r2[i]))/2

		prob_a_y	= (np.mean(prob_a_y1[i]) + np.mean(prob_a_y2[i]))/2
		prob_t_y	= (np.mean(prob_t_y1[i]) + np.mean(prob_t_y2[i]))/2

		value_a		= (np.mean(value_a1[i]) + np.mean(value_a2[i]))/2
		value_t 	= (np.mean(value_t1[i]) + np.mean(value_t2[i]))/2

		prob_g	= ((2*prob_t_g + prob_a_g)/3)
		prob_r	= ((2*prob_t_r + prob_a_r)/3)
		prob_y	= ((2*prob_t_y + prob_a_y)/3)

		prob_c	= [prob_g, prob_r, prob_y]

		if prob_c[argmax(prob_c)] < PRO:
			color.append(2)
			value.append((((2*value_t  +  value_a)/3) + (max(max_v) + min(min_v)))/3)

		else:
			color.append((argmax(prob_c) + 1))
			value.append((2*value_t  +  value_a)/3)

		
		# f1 = figure._get_table(value[i], CFS)
		prob.append(prob_c[argmax(prob_c)])		
		maxi.append(max(max_v))
		mini.append(min(min_v))
		fig.append('Null')		
		# fig.append(f1)

		if b <= max_i - 24:
			# a += 24
			# b += 24
			d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = b) + datetime.timedelta(hours = utc0)
			b += 1
		else:
			# a += 6	
			# b += 6	
			d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = b) + datetime.timedelta(hours = utc0)
			b += 4

		date.append(d1)
	return(date, prob, color, value, maxi, mini, fig)	

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

#	a = 0
#	b = 24
	for i in range(0, max_i//24):

		max_v		= max(max_t1[i], max_a1[i])
		min_v		= min(min_t1[i], min_a1[i])

		prob_a_g	= (np.mean(prob_a_g1[i]) + np.mean(prob_a_g2[i]))/2
		prob_t_g 	= (np.mean(prob_t_g1[i]) + np.mean(prob_t_g2[i]))/2

		prob_a_r 	= (np.mean(prob_a_r1[i]) + np.mean(prob_a_r2[i]))/2
		prob_t_r	= (np.mean(prob_t_r1[i]) + np.mean(prob_t_r2[i]))/2

		prob_a_y	= (np.mean(prob_a_y1[i]) + np.mean(prob_a_y2[i]))/2
		prob_t_y	= (np.mean(prob_t_y1[i]) + np.mean(prob_t_y2[i]))/2

		value_a		= (np.mean(value_a1[i]) + np.mean(value_a2[i]))/2
		value_t 	= (np.mean(value_t1[i]) + np.mean(value_t2[i]))/2

		prob_g	= ((2*prob_t_g + prob_a_g)/3)
		prob_r	= ((2*prob_t_r + prob_a_r)/3)
		prob_y	= ((2*prob_t_y + prob_a_y)/3)

		prob_c	= [prob_g, prob_r, prob_y]

		if prob_c[argmax(prob_c)] < PRO:
			color.append(2)
			value.append((((2*value_t  +  value_a)/3) + (max(max_v) + min(min_v)))/3)
			
		else:
			color.append((argmax(prob_c) + 1))
			value.append((2*value_t  +  value_a)/3)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = i) + datetime.timedelta(hours = utc0)
		f1 = figure._get_table(value[i], CFS)
		prob.append(prob_c[argmax(prob_c)])		
		maxi.append(max(max_v))
		mini.append(min(min_v))
		date.append(d1)
		fig.append(f1)
#		a += 24
#		b += 24

	return(date, prob, color, value, maxi, mini, fig)	

###############################################################################
