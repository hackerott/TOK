#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

def prob_limits():
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
	rain_e1 = ens1.variables['pratesfc']
	rain_e2 = ens2.variables['pratesfc']
	rain_e3 = ens3.variables['pratesfc']
	rain_e4 = ens4.variables['pratesfc']
	rain_e5 = ens5.variables['pratesfc']
	rain_e6 = ens6.variables['pratesfc']
	rain_e7 = ens7.variables['pratesfc']
	rain_e8 = ens8.variables['pratesfc']

	max_j = max_i // 4
	day = iz // 4
	date = []
	raine1 = []
	raine2 = []
	raine3 = []
	raine4 = []
	raine5 = []
	raine6 = []
	raine7 = []
	raine8 = []
	for i in range(day, max_j):
		raine1.append(sum(rain_e1[b:a, ixCFS, iyCFS]))
		raine2.append(sum(rain_e2[b:a, ixCFS, iyCFS]))
		raine3.append(sum(rain_e3[b:a, ixCFS, iyCFS]))
		raine4.append(sum(rain_e4[b:a, ixCFS, iyCFS]))
		raine5.append(sum(rain_e5[c:d, ixCFS, iyCFS]))
		raine6.append(sum(rain_e6[c:d, ixCFS, iyCFS]))
		raine7.append(sum(rain_e7[c:d, ixCFS, iyCFS]))
		raine8.append(sum(rain_e8[c:d, ixCFS, iyCFS]))

		if (sum(rain_e1[b:a, ixCFS, iyCFS])) < 0.01:
			raine1.append(0)	
		if (sum(rain_e2[b:a, ixCFS, iyCFS])) < 0.01:
			raine2.append(0)	
		if (sum(rain_e3[b:a, ixCFS, iyCFS])) < 0.01:
			raine3.append(0)
		if (sum(rain_e4[b:a, ixCFS, iyCFS])) < 0.01:
			raine4.append(0)
		if (sum(rain_e5[b:a, ixCFS, iyCFS])) < 0.01:
			raine5.append(0)
		if (sum(rain_e6[b:a, ixCFS, iyCFS])) < 0.01:
			raine6.append(0)
		if (sum(rain_e7[b:a, ixCFS, iyCFS])) < 0.01:
			raine7.append(0)
		if (sum(rain_e8[b:a, ixCFS, iyCFS])) < 0.01:
			raine8.append(0)
		a += 4
		b += 4
		c += 4
		d += 4

	prob_y	= [0] * max_j
	prob_g	= [0] * max_j 
	prob_r	= [0] * max_j
	prob	= [0] * max_j
	val_y	= [0] * max_j
	val_r	= [0] * max_j
	val_g	= [0] * max_j
	val	= [0] * max_j
	color	= [0] * max_j
	for i in range(day, max_j):
	## day 1
		if raine1[i] <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * raine1[i])
		elif raine1[i] >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * raine1[i])
		elif 1 < raine1[i] < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * raine1[i])

		if raine2[i] <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * raine2[i])
		elif raine2[i] >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * raine2[i])
		elif 1 < raine2[i] < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * raine2[i])		

		if raine3[i] <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * raine3[i])
		elif raine3[i] >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * raine3[i])
		elif 1 < raine3[i] < 10: 
			prob_g[i] += 0.175 #verde
	
		if raine4[i] <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * raine4[i])
		elif raine4[i] >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * raine4[i])
		elif 1 < raine4[i] < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * raine4[i])
## day 2
		if raine5[i] <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * raine5[i])
		elif raine5[i] >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * raine5[i])
		elif 1 < raine5[i] < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * raine5[i])
	
		if raine6[i] <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * raine6[i])
		elif raine6[i] >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * raine6[i])
		elif 1 < raine6[i] < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * raine6[i])
		
		if raine7[i] <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * raine7[i])
		elif raine7[i] >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * raine7[i])
		elif 1 < raine7[i] < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * raine7[i])
		
		if raine8[i] <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * raine8[i])
		elif raine8[i] >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * raine8[i])
		elif 1 < raine8[i] < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * raine8[i])	

		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0) + datetime.timedelta(days = 10)
		data.append(d1)

	for i in range(day, max_j):
		if   prob_y[i] > prob_r[i] and prob_y[i] > prob_g[i]:
			color[i] = 2 
			prob[i] = prob_y[i]
			val[i] = val_y[i]/prob_y[i]
		elif prob_r[i] > prob_y[i] and prob_r[i] > prob_g[i]:
			color[i] = 3
			prob[i] = prob_r[i]
			val[i] = val_r[i]/prob_r[i] 
		elif prob_g[i] > prob_y[i] and prob_g[i] > prob_r[i]:
			color[i] = 1
			prob[i] = prob_g[i]
			val[i] = val_g[i]/prob_g[i]
		elif prob_y[i] == prob_r[i] and prob_y[i] > prob_g[i]:
			color[i] = 2
			prob[i] = prob_y[i] + pro_g[i]/2
			val[i] = (2.5*(val_y[i]/prob_y[i]) + 0.5*(val_g[i]/prob_g[i]))/3
		elif prob_r[i] == prob_g[i] and prob_r[i] > prob_y[i]:
			color[i] = 3
			prob[i] = prob_r[i] + prob_y[i]/2
			val[i] = (2.5*(val_r[i]/prob_r[i]) + 0.5*(val_y[i]/prob_y[i]))/3
		elif prob_g[i]  == prob_y[i] and prob_g[i] > prob_r[i]:
			color[i] = 1
			prob[i] = prob_g[i] + prob_r[i]/2
			val[i] = (2.5*(val_g[i]/prob_g[i]) + 0.5*(val_r[i]/prob_r[i]))/3
		elif prob_y[i] == prob_r[i] and prob_y[i] < prob_g[i]:
			color[i] = 1
			prob[i] = prob_g[i] + prob_y[i]/2
			val[i] = (2.5*(val_g[i]/prob_g[i]) + 0.5*(val_y[i]/prob_y[i]))/3			
		elif prob_r[i] == prob_g[i] and prob_r[i] < prob_y[i]:
			color[i] = 2
			prob[i] =  prob_y[i] + prob_r/2
			val[i] = (2.5*(val_y[i]/prob_y[i]) + 0.5*(val_r[i]/prob_r[i]))/3
		elif prob_g[i]  == prob_y[i] and prob_g[i] < prob_r[i]:
			color[i] = 3
			prob[i] = prob_r[i] + prob_g[i]/2
			val[i] = (2.5*(val_r[i]/prob_r[i]) + 0.5*(val_g[i]/prob_g[i]))/3
		else:
			val[i] = (val_r[i] + val_g[i] + val_y[i])/3
			if val[i] <= 1:			
				color[i] = 3
				prob[i] = 0.3
			elif val[i] <= 10:
				color[i] = 1
				prob[i] = 0.3
			else:
				color[i] = 2
				prob[i] = 0.3
	return(date, prob, color, val, max_j)
