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
import figure
#######################################
"""
Use date an time of request to present value as 'now' in GFS and WRF
And date to present for 'full' day in all models
will or not receive specific date?  or only awser for request date ???
Does CFS has a card? or it is only for the 'first day'??
This is exctly the same as calendar.

"""
###############################################################################
#CFS
def DATA_cfs_card(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, time, iz, ixCFS, iyCFS, date0, utc0, TOP, BOT, PRO):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens5, time, VAR, ixCFS, iyCFS, TOP, BOT) 
	prob_t_g2, prob_t_r2, prob_t_y2, value_t2, max_t2, min_t2 = prob_time._get_TIMEP(ens2, ens6, time, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_t_g3, prob_t_r3, prob_t_y3, value_t3, max_t3, min_t3 = prob_time._get_TIMEP(ens3, ens7, time, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_t_g4, prob_t_r4, prob_t_y4, value_t4, max_t4, min_t4 = prob_time._get_TIMEP(ens4, ens8, time, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_a_g2, prob_a_r2, prob_a_y2, value_a2, max_a2, min_a2 = prob_area._get_AREAP(ens2, time, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_a_g3, prob_a_r3, prob_a_y3, value_a3, max_a3, min_a3 = prob_area._get_AREAP(ens3, time, VAR, ixCFS, iyCFS, TOP, BOT)
	prob_a_g4, prob_a_r4, prob_a_y4, value_a4, max_a4, min_a4 = prob_area._get_AREAP(ens4, time, VAR, ixCFS, iyCFS, TOP, BOT)
	color	= []
	value	= []
	prob	= []
	date	= []
	mini	= []
	maxi	= []
	fig		= []
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
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		if prob_c[argmax(prob_c)] < PRO:
			color.append(2)
			value.append((((2*value_t  +  value_a)/3) + (max(max_v) + min(min_v)))/3)
			
		else:
			color.append((argmax(prob_c) + 1))
			value.append((2*value_t  +  value_a)/3)
		f1 = figure._get_card(value[i], CFS)
		prob.append(prob_c[argmax(prob_c)])		
		maxi.append(max(max_v))
		mini.append(min(min_v))
		date.append(d1)
		fig.append(f1)
		a += 4
		b += 4


	return(date, prob, color, value, maxi, mini, fig)

###############################################################################
#GFS
def DATA_gfs_card(ens1, ens2, time, iz, ixGFS, iyGFS, date0, utc0, TOP, BOT, PRO)
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens2, time, VAR, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, VAR, ixGFS, iyGFS, TOP, BOT)
	color	= []
	value	= []
	prob	= []
	date	= []
	mini	= []
	maxi	= []
	fig		= []
	a = 0
	b = 24
	for i in range(0, max_i//24):
		max_v		= max(max_t1[a:b], max_t2[a:b])
		min_v		= min(min_t1[a:b], min_t2[a:b])
		prob_a_g	= (np.mean(prob_a_g1[a:b]) + np.mean(prob_a_g2[a:b]))/2
		prob_t_g 	= (np.mean(prob_t_g1[a:b]) + np.mean(prob_t_g2[a:b]))/2
		prob_a_r 	= (np.mean(prob_a_r1[a:b]) + np.mean(prob_a_r2[a:b]))/2
		prob_t_r	= (np.mean(prob_t_r1[a:b]) + np.mean(prob_t_r2[a:b]))/2
		prob_a_y	= (np.mean(prob_a_y1[a:b]) + np.mean(prob_a_y2[a:b]))/2
		prob_t_y	= (np.mean(prob_t_y1[a:b]) + np.mean(prob_t_y2[a:b]))/2
		value_a		= (np.mean(value_a1[a:b]) + np.mean(value_a2[a:b]))/2
		value_t 	= (np.mean(value_t1[a:b]) + np.mean(value_t2[a:b]))/2
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
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		f1 = figure._get_card(value[i], CFS)
		prob.append(prob_c[argmax(prob_c)])		
		maxi.append(max(max_v))
		mini.append(min(min_v))
		date.append(d1)
		fig.append(f1)
		if b <= max_i - 24:
			a += 24
			b += 24
		else:
			a += 6	
			b += 6	
	return(date, prob, color, value, maxi, mini, fig)	

###############################################################################
#WRF
def DATA_wrf_card(ens1, ens2, time, iz, ixWRF, iyWRF, date0, utc0, TOP, BOT, PRO)
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, value_t1, max_t1, min_t1 = prob_time._get_TIMEP(ens1, ens2, time, VAR, ixWRF, iyWRF, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, value_a1, max_a1, min_a1 = prob_area._get_AREAP(ens1, time, VAR, ixWRF, iyWRF, TOP, BOT)
	color	= []
	value	= []
	prob	= []
	date	= []
	mini	= []
	maxi	= []
	fig		= []
	a = 0
	b = 24
	for i in range(0, max_i//24):
		max_v		= max(max_t1[a:b], max_t2[a:b])
		min_v		= min(min_t1[a:b], min_t2[a:b])
		prob_a_g	= (np.mean(prob_a_g1[a:b]) + np.mean(prob_a_g2[a:b]))/2
		prob_t_g 	= (np.mean(prob_t_g1[a:b]) + np.mean(prob_t_g2[a:b]))/2
		prob_a_r 	= (np.mean(prob_a_r1[a:b]) + np.mean(prob_a_r2[a:b]))/2
		prob_t_r	= (np.mean(prob_t_r1[a:b]) + np.mean(prob_t_r2[a:b]))/2
		prob_a_y	= (np.mean(prob_a_y1[a:b]) + np.mean(prob_a_y2[a:b]))/2
		prob_t_y	= (np.mean(prob_t_y1[a:b]) + np.mean(prob_t_y2[a:b]))/2
		value_a		= (np.mean(value_a1[a:b]) + np.mean(value_a2[a:b]))/2
		value_t 	= (np.mean(value_t1[a:b]) + np.mean(value_t2[a:b]))/2
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
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		f1 = figure._get_card(value[i], CFS)
		prob.append(prob_c[argmax(prob_c)])		
		maxi.append(max(max_v))
		mini.append(min(min_v))
		date.append(d1)
		fig.append(f1)
		a += 24
		b += 24
	return(date, prob, color, value, maxi, mini, fig)	

###############################################################################
"""
Now part, only GFS and WRF
"""
