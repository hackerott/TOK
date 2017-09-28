#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import datetime

#######################################
import prob_area
import prob_time
#######################################
###############################################################################
#CFS
def DATA_cfs_gcard(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, time, ixCFS, iyCFS, date0, utc0, TOP, BOT, PRO, var_id):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens5, time, 4, ixCFS, iyCFS, TOP, BOT) 
	prob_t_g2, prob_t_r2, prob_t_y2, value_t2, max_t2, min_t2 = prob_time._get_TIMEP(ens2, ens6, time, 4, ixCFS, iyCFS, TOP, BOT)
	prob_t_g3, prob_t_r3, prob_t_y3, value_t3, max_t3, min_t3 = prob_time._get_TIMEP(ens3, ens7, time, 4, ixCFS, iyCFS, TOP, BOT)
	prob_t_g4, prob_t_r4, prob_t_y4, value_t4, max_t4, min_t4 = prob_time._get_TIMEP(ens4, ens8, time, 4, ixCFS, iyCFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, ixCFS, iyCFS, TOP, BOT)
	prob_a_g2, prob_a_r2, prob_a_y2, value_a2, max_a2, min_a2 = prob_area._get_AREAP(ens2, time, ixCFS, iyCFS, TOP, BOT)
	prob_a_g3, prob_a_r3, prob_a_y3, value_a3, max_a3, min_a3 = prob_area._get_AREAP(ens3, time, ixCFS, iyCFS, TOP, BOT)
	prob_a_g4, prob_a_r4, prob_a_y4, value_a4, max_a4, min_a4 = prob_area._get_AREAP(ens4, time, ixCFS, iyCFS, TOP, BOT)
	del prob_a_g1, prob_a_r1, prob_a_y1, prob_a_g2, prob_a_r2, prob_a_y2, prob_a_g3, prob_a_r3, prob_a_y3, prob_a_g4, prob_a_r4, prob_a_y4, prob_t_g1, prob_t_r1, prob_t_y1, prob_t_g2, prob_t_r2, prob_t_y2, prob_t_g3, prob_t_r3, prob_t_y3, prob_t_g4, prob_t_r4, prob_t_y4
	del ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8
	value	= []
	date	= []
	value	= []
	date	= []
	a = 0
	b = 4
	for i in range(0, max_i//4):
		max_v = max(np.nanmax(max_t1[a:b]), np.nanmax(max_t2[a:b]), np.nanmax(max_t3[a:b]), np.nanmax(max_t4[a:b]),np.nanmax(max_a1[a:b]), np.nanmax(max_a2[a:b]), np.nanmax(max_a3[a:b]),np.nanmax(max_a4[a:b]))
		min_v = min(np.nanmin(min_t1[a:b]), np.nanmin(min_t2[a:b]), np.nanmin(min_t3[a:b]), np.nanmin(min_t4[a:b]), np.nanmin(min_a1[a:b]), np.nanmin(min_a2[a:b]), np.nanmin(min_a3[a:b]), np.nanmin(min_a4[a:b]))
		if var_id == 1:
			value_a = (np.subtract(value_a1[b], value_a1[a]) + np.subtract(value_a2[b], value_a2[a]) + np.subtract(value_a3[b], value_a3[a]) + np.subtract(value_a4[b], value_a4[a]))/4
			value_t = (np.subtract(value_t1[b], value_t1[a]) + np.subtract(value_t2[b], value_t2[a]) + np.subtract(value_t3[b], value_t3[a]) + np.subtract(value_t4[b], value_t4[a]))/4
			value_p 	= ((2*value_t  +  value_a)/3)
		elif var_id == 2:
			value_p = max_v
		elif var_id == 3:
			value_p = [max_v, min_v]
		elif var_id == 4:
			value_a = (np.mean(value_a1[a:b]) + np.mean(value_a2[a:b]) + np.mean(value_a3[a:b]) + np.mean(value_a4[a:b]))/4
			value_t = (np.mean(value_t1[a:b]) + np.mean(value_t2[a:b]) + np.mean(value_t3[a:b]) + np.mean(value_t4[a:b]))/4
			value_p 	= ((2*value_t  +  value_a)/3)
		elif var_id == 5:
			value_p = min_v
		elif var_id == 6:
			value_a = (np.mean(value_a1[a:b]) + np.mean(value_a2[a:b]) + np.mean(value_a3[a:b]) + np.mean(value_a4[a:b]))/4
			value_t = (np.mean(value_t1[a:b]) + np.mean(value_t2[a:b]) + np.mean(value_t3[a:b]) + np.mean(value_t4[a:b]))/4
			value_p 	= ((2*value_t  +  value_a)/3)
		# value.append(int(value_p*10)/10.0)
		value.append(value_p)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = 8 + i) + datetime.timedelta(hours = utc0)
		date.append(d1)
		a += 4
		b += 4
	del value_t1, value_a1
	return(date, 'null', 'null', value, 'null', 'null')
###############################################################################
#GFS
def DATA_gfs_gcard(ens1, ens2, time, ixGFS, iyGFS, date0, utc0, TOP, BOT, PRO, var_id):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, ixGFS, iyGFS, TOP, BOT)
	del prob_a_g1, prob_a_r1, prob_a_y1, prob_t_g1, prob_t_r1, prob_t_y1 
	del ens1, ens2  
	value	= []
	date	= []
	a = 0
	b = 24
	for i in range(0, max_i//24):
		max_v	= max(np.nanmax(max_t1[a:b]), np.nanmax(max_a1[a:b]))
		min_v	= min(np.nanmin(min_t1[a:b]), np.nanmin(min_a1[a:b]))
		if var_id == 1:
			value_a	= (np.subtract(value_a1[b], value_a1[a]))
			value_t	= (np.subtract(value_t1[b], value_t1[a]))
			value_p	= ((2*value_t  +  value_a)/3)
		elif var_id == 2:
			if np.isnan(max_v):
				value_p = (value_t1 + value_a1)/2
			else:		
				value_p = max_v
		elif var_id == 3:
			value_p = [max_v, min_v]
		elif var_id == 4:
			value_a	= np.mean(value_a1[a:b])
			value_t	= np.mean(value_t1[a:b])
			value_p	= ((2*value_t  +  value_a)/3)
		elif var_id == 5:
			value_p = min_v
		elif var_id == 6:
			value_a	= np.mean(value_a1[a:b])
			value_t	= np.mean(value_t1[a:b])
			value_p	= ((2*value_t  +  value_a)/3)
		# value.append(int(value_p*10)/10.0)
		value.append(value_p)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		date.append(d1)
		a += 24
		b += 24
	del value_t1, value_a1
	return(date, 'null', 'null', value, 'null', 'null')
###############################################################################
#WRF
def DATA_wrf_gcard(ens1, ens2, time, ixWRF, iyWRF, date0, utc0, TOP, BOT, PRO, var_id):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens2, time, 12, ixWRF, iyWRF, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, ixWRF, iyWRF, TOP, BOT)
	del prob_a_g1, prob_a_r1, prob_a_y1, prob_t_g1, prob_t_r1, prob_t_y1 
	del ens1, ens2  

	value	= []
	date	= []
	a = 0
	b = 24
	for i in range(0, max_i//24):
		max_v	= max(np.nanmax(max_t1[a:b]), np.nanmax(max_a1[a:b]))
		min_v	= min(np.nanmin(min_t1[a:b]), np.nanmin(min_a1[a:b]))
		if var_id == 1:
			value_a		= (np.subtract(value_a1[b], value_a1[a]))
			value_t 	= (np.subtract(value_t1[b], value_t1[a]))
			value_p 	= ((2*value_t  +  value_a)/3)
		elif var_id == 2:
			value_p = max_v
		elif var_id == 3:
			value_p = [max_v, min_v]
		elif var_id == 4:
			value_a		= np.mean(value_a1[a:b])
			value_t 	= np.mean(value_t1[a:b])
			value_p 	= ((2*value_t  +  value_a)/3)
		elif var_id == 5:
			value_p = min_v
		elif var_id == 6:
			value_a		= np.mean(value_a1[a:b])
			value_t 	= np.mean(value_t1[a:b])
			value_p 	= ((2*value_t  +  value_a)/3)
		# value.append(int(value_p*10)/10.0)
		value.append(value_p)
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		date.append(d1)
		a += 24
		b += 24
	del value_t1, value_a1
	return(date, 'null', 'null', value, 'null', 'null')	
###############################################################################
