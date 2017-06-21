#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan, mean

def prob_limits():
'''
Possible method:
	-Use 50 percentile of the variable as base, add STD to top limit, subtract it for botton limit.
	-Use 70 perentile as top limit and 30 percentile as botton limit
	-Stract mean from a climatological database
	-Use the seasonal mean from the closest station

'''

	TOP = 
	BOT = 
	PRO = 
	
	return(TOP, BOT, PRO)

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
	
	if iz == 0:
		a = 4
		b = iz
	else:
		a = iz + 4
		b = iz
	c = b
	d = a	
		
	uwind_e1 = ens1.variables['ugrd10m']
	uwind_e2 = ens2.variables['ugrd10m']
	uwind_e3 = ens3.variables['ugrd10m']
	uwind_e4 = ens4.variables['ugrd10m']
	uwind_e5 = ens5.variables['ugrd10m']
	uwind_e6 = ens6.variables['ugrd10m']
	uwind_e7 = ens7.variables['ugrd10m']
	uwind_e8 = ens8.variables['ugrd10m']
	vwind_e1 = ens1.variables['vgrd10m']
	vwind_e2 = ens2.variables['vgrd10m']
	vwind_e3 = ens3.variables['vgrd10m']
	vwind_e4 = ens4.variables['vgrd10m']
	vwind_e5 = ens5.variables['vgrd10m']
	vwind_e6 = ens6.variables['vgrd10m']
	vwind_e7 = ens7.variables['vgrd10m']
	vwind_e8 = ens8.variables['vgrd10m']
	
	wind_e1	= []
	wind_e2	= []
	wind_e3	= []
	wind_e4	= [] 
	wind_e5	= []
	wind_e6	= []
	wind_e7	= []
	wind_e8	= []

	for i in range(0, max_i):
		wind_e1.append(sqrt(power(uwind_e1[i, ixCFS, iyCFS], 2) + power(vwind_e1[i, ixCFS, iyCFS], 2)))
		wind_e2.append(sqrt(power(uwind_e2[i, ixCFS, iyCFS], 2) + power(vwind_e2[i, ixCFS, iyCFS], 2)))
		wind_e3.append(sqrt(power(uwind_e3[i, ixCFS, iyCFS], 2) + power(vwind_e3[i, ixCFS, iyCFS], 2)))
		wind_e4.append(sqrt(power(uwind_e4[i, ixCFS, iyCFS], 2) + power(vwind_e4[i, ixCFS, iyCFS], 2)))

		wind_e5.append(sqrt(power(uwind_e5[i, ixCFS, iyCFS], 2) + power(vwind_e5[i, ixCFS, iyCFS], 2)))
		wind_e6.append(sqrt(power(uwind_e6[i, ixCFS, iyCFS], 2) + power(vwind_e6[i, ixCFS, iyCFS], 2)))
		wind_e7.append(sqrt(power(uwind_e7[i, ixCFS, iyCFS], 2) + power(vwind_e7[i, ixCFS, iyCFS], 2)))
		wind_e8.append(sqrt(power(uwind_e8[i, ixCFS, iyCFS], 2) + power(vwind_e8[i, ixCFS, iyCFS], 2)))
		

	max_j = max_i // 4
	day = iz // 4
	date = []
	prob_g	= [0] * max_j
	prob_r	= [0] * max_j
	prob_y	= [0] * max_j
	prob	= []
	val_g	= [0] * max_j
	val_r	= [0] * max_j
	val_y	= [0] * max_j
	val	= []
	color	= []
	

################################################################################	
	if iz == 0:
		a = 4
		b = iz
	else:
		a = iz + 4
		b = iz
	c = b + 4 
	d = a + 4	
	for i in range(day, max_j):
		if a > max_i:
			break
		out_e1 = wind_e1[b+argmax(wind_e1[b:a])]
		out_e2 = wind_e2[b+argmax(wind_e2[b:a])]
		out_e3 = wind_e3[b+argmax(wind_e3[b:a])]
		out_e4 = wind_e4[b+argmax(wind_e4[b:a])]
		out_e5 = wind_e5[b+argmax(wind_e5[b:a])]
		out_e6 = wind_e6[b+argmax(wind_e6[b:a])]
		out_e7 = wind_e7[b+argmax(wind_e7[b:a])]
		out_e8 = wind_e8[b+argmax(wind_e8[b:a])]
		a += 4
		b += 4
		c += 4
		d += 4
################################################################################	
	## day 1
		if out_e1 <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * out_e1)
		elif out_e1 >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * out_e1)
		elif 1 < out_e1 < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * out_e1)

		if out_e2 <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * out_e2)
		elif out_e2 >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * out_e2)
		elif 1 < out_e2 < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * out_e2)		

		if out_e3 <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * out_e3)
		elif out_e3 >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * out_e3)
		elif 1 < out_e3 < 10: 
			prob_g[i] += 0.175 #verde
	
		if out_e4 <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * out_e4)
		elif out_e4 >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * out_e4)
		elif 1 < out_e4 < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * out_e4)
## day 2
		if out_e5 <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * out_e5)
		elif out_e5 >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * out_e5)
		elif 1 < out_e5 < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * out_e5)
	
		if out_e6 <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * out_e6)
		elif out_e6 >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * out_e6)
		elif 1 < out_e6 < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * out_e6)
		
		if out_e7 <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * out_e7)
		elif out_e7 >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * out_e7)
		elif 1 < out_e7 < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * out_e7)
		
		if out_e8 <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * out_e8)
		elif out_e8 >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * out_e8)
		elif 1 < out_e8 < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * out_e8)	

		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0) + datetime.timedelta(days = 10)
		date.append(d1)

	for i in range(day, max_j):
		if   prob_y[i] > prob_r[i] and prob_y[i] > prob_g[i]:
			color.append(2) 
			prob.append(prob_y[i])
			val.append(val_y[i]/prob_y[i])
		elif prob_r[i] > prob_y[i] and prob_r[i] > prob_g[i]:
			color.append(3)
			prob.append(prob_r[i])
			val.append(val_r[i]/prob_r[i])
		elif prob_g[i] > prob_y[i] and prob_g[i] > prob_r[i]:
			color.append(1)
			prob.append(prob_g[i])
			val.append(val_g[i]/prob_g[i])
		elif prob_y[i] == prob_r[i] and prob_y[i] > prob_g[i]:
			color.append(2)
			prob.append(prob_y[i] + pro_g[i]/2)
			val.append((2.5*(val_y[i]/prob_y[i]) + 0.5*(val_g[i]/prob_g[i]))/3)
		elif prob_r[i] == prob_g[i] and prob_r[i] > prob_y[i]:
			color.append(3)
			prob.append(prob_r[i] + prob_y[i]/2)
			val.append((2.5*(val_r[i]/prob_r[i]) + 0.5*(val_y[i]/prob_y[i]))/3)
		elif prob_g[i]  == prob_y[i] and prob_g[i] > prob_r[i]:
			color.append(1)
			prob.append(prob_g[i] + prob_r[i]/2)
			val.append((2.5*(val_g[i]/prob_g[i]) + 0.5*(val_r[i]/prob_r[i]))/3)
		elif prob_y[i] == prob_r[i] and prob_y[i] < prob_g[i]:
			color.append(1)
			prob.append(prob_g[i] + prob_y[i]/2)
			val.append((2.5*(val_g[i]/prob_g[i]) + 0.5*(val_y[i]/prob_y[i]))/3)
		elif prob_r[i] == prob_g[i] and prob_r[i] < prob_y[i]:
			color.append(2)
			prob.append(prob_y[i] + prob_r/2)
			val.append((2.5*(val_y[i]/prob_y[i]) + 0.5*(val_r[i]/prob_r[i]))/3)
		elif prob_g[i]  == prob_y[i] and prob_g[i] < prob_r[i]:
			color.append(3)
			prob.append(prob_r[i] + prob_g[i]/2)
			val.append((2.5*(val_r[i]/prob_r[i]) + 0.5*(val_g[i]/prob_g[i]))/3)
		else:
			val.append((val_r[i] + val_g[i] + val_y[i])/3)
			if val[i] <= 1:			
				color.append(3)
				prob.append(0.3)
			elif val[i] <= 10:
				color.append(1)
				prob.append(0.3)
			else:
				color.append(2)
				prob.append(0.3)
	return(date, prob, color, val, max_j)


