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
		max_v		= np.nanmax([max_t1[i], max_a1[i]])
		min_v		= np.nanmin([min_t1[i], min_a1[i]])
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
			result_prov = np.around(result_prov, decimals=2)
			if result_prov < 1 and result_prov > 0:
				result_prov = int((result_prov * 10))/10.0
			else:
				try:
					result_prov = int(result_prov)
				except:
					result_prov = result_prov
		else:
			color.append((np.argmax(prob_c) + 1))
			result_prov = ((2*value_t  +  value_a)/3)
			result_prov = np.around(result_prov, decimals=2)
			if result_prov < 1 and result_prov > 0:
				result_prov = int((result_prov * 10))/10.0
			else:
				result_prov = int(result_prov)

		value.append(result_prov)
		prob.append(prob_c[np.argmax(prob_c)])		
		maxi.append(max_v)
		mini.append(min_v)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = i) + datetime.timedelta(hours = utc0)
	
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
		max_v		= np.nanmax([max_t1[i], max_a1[i]])
		min_v		= np.nanmin([min_t1[i], min_a1[i]])
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
			result_prov = np.around(result_prov, decimals=2)
			if result_prov < 1 and result_prov > 0:
				result_prov = int((result_prov * 10))/10.0
			else:
				result_prov = int(result_prov)
		else:
			color.append((np.argmax(prob_c) + 1))
			result_prov = ((2*value_t  +  value_a)/3)
			result_prov = np.around(result_prov, decimals=2)
			if result_prov < 1 and result_prov > 0:
				result_prov = int((result_prov * 10))/10.0
			else:
				result_prov = int(result_prov)

		value.append(result_prov)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = i) + datetime.timedelta(hours = utc0)
		prob.append(prob_c[np.argmax(prob_c)])		
		maxi.append(max_v)
		mini.append(min_v)
		date.append(d1)

	return(date, prob, color, value, maxi, mini)	

###############################################################################
def DATA_cfs_table(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, time, ixCFS, iyCFS, date0, utc0, TOP, BOT, PRO, var_id):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens5, time, 4, ixCFS, iyCFS, TOP, BOT) 
	prob_t_g2, prob_t_r2, prob_t_y2, value_t2, max_t2, min_t2 = prob_time._get_TIMEP(ens2, ens6, time, 4, ixCFS, iyCFS, TOP, BOT)
	prob_t_g3, prob_t_r3, prob_t_y3, value_t3, max_t3, min_t3 = prob_time._get_TIMEP(ens3, ens7, time, 4, ixCFS, iyCFS, TOP, BOT)
	prob_t_g4, prob_t_r4, prob_t_y4, value_t4, max_t4, min_t4 = prob_time._get_TIMEP(ens4, ens8, time, 4, ixCFS, iyCFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, ixCFS, iyCFS, TOP, BOT)
	prob_a_g2, prob_a_r2, prob_a_y2, value_a2, max_a2, min_a2 = prob_area._get_AREAP(ens2, time, ixCFS, iyCFS, TOP, BOT)
	prob_a_g3, prob_a_r3, prob_a_y3, value_a3, max_a3, min_a3 = prob_area._get_AREAP(ens3, time, ixCFS, iyCFS, TOP, BOT)
	prob_a_g4, prob_a_r4, prob_a_y4, value_a4, max_a4, min_a4 = prob_area._get_AREAP(ens4, time, ixCFS, iyCFS, TOP, BOT)

	color	= []
	value	= []
	prob	= []
	date	= []
	mini	= []
	maxi	= []

	a = 0
	b = 4
	result_prov = 0
	for i in range(0, max_i):
		prob_a_g = ((np.nanmean(prob_a_g1[i]) + np.nanmax(prob_a_g1[i]))/2 + (np.nanmean(prob_a_g2[i]) + np.nanmax(prob_a_g2[i]))/2 + (np.nanmean(prob_a_g3[i]) + np.nanmax(prob_a_g3[i]))/2 + (np.nanmean(prob_a_g4[i]) + np.nanmax(prob_a_g4[i]))/2)/4
		prob_t_g = ((np.nanmean(prob_t_g1[i]) + np.nanmax(prob_t_g1[i]))/2 + (np.nanmean(prob_t_g2[i]) + np.nanmax(prob_t_g2[i]))/2 + (np.nanmean(prob_t_g3[i]) + np.nanmax(prob_t_g3[i]))/2 + (np.nanmean(prob_t_g4[i]) + np.nanmax(prob_t_g4[i]))/2)/4
		prob_a_r = ((np.nanmean(prob_a_r1[i]) + np.nanmax(prob_a_r1[i]))/2 + (np.nanmean(prob_a_r2[i]) + np.nanmax(prob_a_r2[i]))/2 + (np.nanmean(prob_a_r3[i]) + np.nanmax(prob_a_r3[i]))/2 + (np.nanmean(prob_a_r4[i]) + np.nanmax(prob_a_r4[i]))/2)/4
		prob_t_r = ((np.nanmean(prob_t_r1[i]) + np.nanmax(prob_t_r1[i]))/2 + (np.nanmean(prob_t_r2[i]) + np.nanmax(prob_t_r2[i]))/2 + (np.nanmean(prob_t_r3[i]) + np.nanmax(prob_t_r3[i]))/2 + (np.nanmean(prob_t_r4[i]) + np.nanmax(prob_t_r4[i]))/2)/4
		prob_a_y = ((np.nanmean(prob_a_y1[i]) + np.nanmax(prob_a_y1[i]))/2 + (np.nanmean(prob_a_y2[i]) + np.nanmax(prob_a_y2[i]))/2 + (np.nanmean(prob_a_y3[i]) + np.nanmax(prob_a_y3[i]))/2 + (np.nanmean(prob_a_y4[i]) + np.nanmax(prob_a_y4[i]))/2)/4
		prob_t_y = ((np.nanmean(prob_t_y1[i]) + np.nanmax(prob_t_y1[i]))/2 + (np.nanmean(prob_t_y2[i]) + np.nanmax(prob_t_y2[i]))/2 + (np.nanmean(prob_t_y3[i]) + np.nanmax(prob_t_y3[i]))/2 + (np.nanmean(prob_t_y4[i]) + np.nanmax(prob_t_y4[i]))/2)/4
		if var_id == 1:
			value_a = np.nansum([value_a1[i], value_a2[i], value_a3[i], value_a4[i]])/4
			value_t = np.nansum([value_t1[i], value_t2[i], value_t3[i], value_t4[i]])/4
			max_v = max(np.nansum(max_t1[i]), np.nansum(max_t2[i]), np.nansum(max_t3[i]), np.nansum(max_t4[i]), np.nansum(max_a1[i]), np.nansum(max_a2[i]), np.nansum(max_a3[i]), np.nansum(max_a4[i]))
			min_v = min(np.nansum(min_t1[i]), np.nansum(min_t2[i]), np.nansum(min_t3[i]), np.nansum(min_t4[i]), np.nansum(min_a1[i]), np.nansum(min_a2[i]), np.nansum(min_a3[i]), np.nansum(min_a4[i]))
		else:	
			value_a = np.nanmean([value_a1[i], value_a2[i], value_a3[i], value_a4[i]])/4
			value_t = np.nanmean([value_t1[i], value_t2[i], value_t3[i], value_t4[i]])/4
			max_v = max((max_t1[i]), (max_t2[i]), (max_t3[i]), (max_t4[i]),(max_a1[i]), (max_a2[i]), (max_a3[i]),(max_a4[i]))
			min_v = min((min_t1[i]), (min_t2[i]), (min_t3[i]), (min_t4[i]), (min_a1[i]), (min_a2[i]), (min_a3[i]), (min_a4[i]))

		prob_g = ((2*prob_t_g + prob_a_g)/3)
		prob_r = ((2*prob_t_r + prob_a_r)/3)
		prob_y = ((2*prob_t_y + prob_a_y)/3)

		prob_c = [prob_g, prob_r, prob_y]
		d1 = date0 + datetime.timedelta(days = 8) + datetime.timedelta(hours = 6*i) + datetime.timedelta(hours = utc0)
		if prob_c[np.argmax(prob_c)] < PRO:
			color.append(2)
			result_prov = ((((2*value_t  +  value_a)/3) + max_v + min_v)/3)
			result_prov = np.around(result_prov, decimals=2)
			if result_prov < 1 and result_prov > 0:
				result_prov = int((result_prov * 10))/10.0
			else:
				try:
					result_prov = int(result_prov)
				except:
					result_prov = result_prov

		else:
			color.append((np.argmax(prob_c) + 1))
			result_prov = ((2*value_t  +  value_a)/3)
			result_prov = np.around(result_prov, decimals=2)
			if result_prov < 1 and result_prov > 0:
				result_prov = int((result_prov * 10))/10.0
			else:
				try:
					result_prov = int(result_prov)
				except:
					result_prov = result_prov

		value.append(result_prov)
		prob.append(prob_c[np.argmax(prob_c)])		
		maxi.append(max_v)
		mini.append(min_v)
		date.append(d1)

	return(date, prob, color, value, maxi, mini)
