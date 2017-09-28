#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import datetime

#######################################
import prob_area
import prob_time
#######################################
"""
Each variable should have botton and top limits to calculate the alert level, as also the limit for indecision, where the alert color should be truncated (ex: whem max prob is below X%, set color to y).
 
"""
###############################################################################
#CFS
def DATA_cfs_calendar(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, time, ixCFS, iyCFS, date0, utc0, TOP, BOT, PRO, var_id):
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
	for i in range(0, max_i//4):
		max_v = max(max(max_t1[a:b]), max(max_t2[a:b]), max(max_t3[a:b]), max(max_t4[a:b]),max(max_a1[a:b]), max(max_a2[a:b]), max(max_a3[a:b]),max(max_a4[a:b]))
		min_v = min(min(min_t1[a:b]), min(min_t2[a:b]), min(min_t3[a:b]), min(min_t4[a:b]), min(min_a1[a:b]), min(min_a2[a:b]), min(min_a3[a:b]), min(min_a4[a:b]))
		prob_a_g = (np.mean(prob_a_g1[a:b]) + np.mean(prob_a_g2[a:b]) + np.mean(prob_a_g3[a:b]) + np.mean(prob_a_g4[a:b]))/4
		prob_t_g = (np.mean(prob_t_g1[a:b]) + np.mean(prob_t_g2[a:b]) + np.mean(prob_t_g3[a:b]) + np.mean(prob_t_g4[a:b]))/4
		prob_a_r = (np.mean(prob_a_r1[a:b]) + np.mean(prob_a_r2[a:b]) + np.mean(prob_a_r3[a:b]) + np.mean(prob_a_r4[a:b]))/4
		prob_t_r = (np.mean(prob_t_r1[a:b]) + np.mean(prob_t_r2[a:b]) + np.mean(prob_t_r3[a:b]) + np.mean(prob_t_r4[a:b]))/4
		prob_a_y = (np.mean(prob_a_y1[a:b]) + np.mean(prob_a_y2[a:b]) + np.mean(prob_a_y3[a:b]) + np.mean(prob_a_y4[a:b]))/4
		prob_t_y = (np.mean(prob_t_y1[a:b]) + np.mean(prob_t_y2[a:b]) + np.mean(prob_t_y3[a:b]) + np.mean(prob_t_y4[a:b]))/4
		if var_id == 1:
			value_a = (np.subtract(value_a1[b], value_a1[a]) + np.subtract(value_a2[b], value_a2[a]) + np.subtract(value_a3[b], value_a3[a]) + np.subtract(value_a4[b], value_a4[a]))/4
			value_t = (np.subtract(value_t1[b], value_t1[a]) + np.subtract(value_t2[b], value_t2[a]) + np.subtract(value_t3[b], value_t3[a]) + np.subtract(value_t4[b], value_t4[a]))/4
		else:	
			value_a = (np.mean(value_a1[a:b]) + np.mean(value_a2[a:b]) + np.mean(value_a3[a:b]) + np.mean(value_a4[a:b]))/4
			value_t = (np.mean(value_t1[a:b]) + np.mean(value_t2[a:b]) + np.mean(value_t3[a:b]) + np.mean(value_t4[a:b]))/4

		prob_g = ((2*prob_t_g + prob_a_g)/3)
		prob_r = ((2*prob_t_r + prob_a_r)/3)
		prob_y = ((2*prob_t_y + prob_a_y)/3)

		prob_c = [prob_g, prob_r, prob_y]
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = 8 + i) + datetime.timedelta(hours = utc0)
		if prob_c[np.argmax(prob_c)] < PRO:
			color.append(2)
			result_prov = ((((2*value_t  +  value_a)/3) + max_v + min_v)/3)
			result_prov = np.around(result_prov, decimals=1)

		else:
			color.append((np.argmax(prob_c) + 1))
			result_prov = ((2*value_t  +  value_a)/3)
			result_prov = np.around(result_prov, decimals=1)

		value.append(result_prov)
		prob.append(prob_c[np.argmax(prob_c)])		
		maxi.append(max_v)
		mini.append(min_v)
		date.append(d1)
		a += 4
		b += 4

	return(date, prob, color, value, maxi, mini)

###############################################################################
#GFS
def DATA_gfs_calendar(ens1, ens2, time, ixGFS, iyGFS, date0, utc0, TOP, BOT, PRO, var_id):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, ixGFS, iyGFS, TOP, BOT)

	color	= []
	value	= []
	prob	= []
	date	= []
	mini	= []
	maxi	= []

	a = 0
	b = 24
	for i in range(0, max_i//24):
		max_v		= max(max(max_t1[a:b]), max(max_a1[a:b]))
		min_v		= min(min(min_t1[a:b]), min(min_a1[a:b]))
		prob_a_g	= (np.mean(prob_a_g1[a:b]))
		prob_t_g 	= (np.mean(prob_t_g1[a:b]))
		prob_a_r 	= (np.mean(prob_a_r1[a:b]))
		prob_t_r	= (np.mean(prob_t_r1[a:b]))
		prob_a_y	= (np.mean(prob_a_y1[a:b]))
		prob_t_y	= (np.mean(prob_t_y1[a:b]))
		if var_id == 1: # and var_id == 4:
			value_a		= (np.subtract(value_a1[b], value_a1[a]))
			value_t 	= (np.subtract(value_t1[b], value_t1[a]))
		else:	
			value_a		= (np.mean(value_a1[a:b]))
			value_t 	= (np.mean(value_t1[a:b]))


		prob_g	= ((2*prob_t_g + prob_a_g)/3)
		prob_r	= ((2*prob_t_r + prob_a_r)/3)
		prob_y	= ((2*prob_t_y + prob_a_y)/3)

		prob_c	= [prob_g, prob_r, prob_y]

		if prob_c[np.argmax(prob_c)] < PRO:
			color.append(2)
			result_prov = ((((2*value_t  +  value_a)/3) + max_v + min_v)/3)
			result_prov = np.around(result_prov, decimals=1)

		else:
			color.append((np.argmax(prob_c) + 1))
			result_prov = ((2*value_t  +  value_a)/3)
			result_prov = np.around(result_prov, decimals=1)

		value.append(result_prov)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		prob.append(prob_c[np.argmax(prob_c)])		
		maxi.append(max_v)
		mini.append(min_v)
		date.append(d1)
		a += 24
		b += 24
		
	return(date, prob, color, value, maxi, mini)	

###############################################################################
#WRF
def DATA_wrf_calendar(ens1, ens2, time, ixWRF, iyWRF, date0, utc0, TOP, BOT, PRO, var_id):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens2, time, 12, ixWRF, iyWRF, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, ixWRF, iyWRF, TOP, BOT)

	color	= []
	value	= []
	prob	= []
	date	= []
	mini	= []
	maxi	= []

	a = 0
	b = 24
	for i in range(0, max_i//24):
		max_v		= max(max(max_t1[a:b]), max(max_a1[a:b]))
		min_v		= min(min(min_t1[a:b]), min(min_a1[a:b]))
		prob_a_g	= (np.mean(prob_a_g1[a:b]))
		prob_t_g 	= (np.mean(prob_t_g1[a:b]))
		prob_a_r 	= (np.mean(prob_a_r1[a:b]))
		prob_t_r	= (np.mean(prob_t_r1[a:b]))
		prob_a_y	= (np.mean(prob_a_y1[a:b]))
		prob_t_y	= (np.mean(prob_t_y1[a:b]))
		if var_id == 1: # and var_id == 4:
			value_a		= (np.subtract(value_a1[b], value_a1[a]))
			value_t 	= (np.subtract(value_t1[b], value_t1[a]))
		else:	
			value_a		= (np.mean(value_a1[a:b]))
			value_t 	= (np.mean(value_t1[a:b]))

		prob_g	= ((2*prob_t_g + prob_a_g)/3)
		prob_r	= ((2*prob_t_r + prob_a_r)/3)
		prob_y	= ((2*prob_t_y + prob_a_y)/3)
		prob_c	= [prob_g, prob_r, prob_y]

		if prob_c[np.argmax(prob_c)] < PRO:
			color.append(2)
			result_prov = ((((2*value_t  +  value_a)/3) + max_v + min_v)/3)
			result_prov = np.around(result_prov, decimals=1)
		else:
			color.append((np.argmax(prob_c) + 1))
			result_prov = ((2*value_t  +  value_a)/3)
			result_prov = np.around(result_prov, decimals=1)

		value.append(result_prov)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		prob.append(prob_c[np.argmax(prob_c)])		
		maxi.append(max_v)
		mini.append(min_v)
		date.append(d1)
		a += 24
		b += 24

	return(date, prob, color, value, maxi, mini)	

###############################################################################
