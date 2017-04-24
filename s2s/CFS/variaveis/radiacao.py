#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

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
	radiation_e1 = ens1.variables['dswrfsfc']
	radiation_e2 = ens2.variables['dswrfsfc']
	radiation_e3 = ens3.variables['dswrfsfc']
	radiation_e4 = ens4.variables['dswrfsfc']
	radiation_e5 = ens5.variables['dswrfsfc']
	radiation_e6 = ens6.variables['dswrfsfc']
	radiation_e7 = ens7.variables['dswrfsfc']
	radiation_e8 = ens8.variables['dswrfsfc']

	max_j = max_i // 4
	day = iz // 4
	date = []
	rad_e1 = []
	rad_e2 = []
	rad_e3 = []
	rad_e4 = []
	rad_e5 = []
	rad_e6 = []
	rad_e7 = []
	rad_e8 = []
	for i in range(day, max_j):
		rad_e1.append(sum(radiation_e1[b:a, ixCFS, iyCFS]))
		rad_e2.append(sum(radiation_e2[b:a, ixCFS, iyCFS]))
		rad_e3.append(sum(radiation_e3[b:a, ixCFS, iyCFS]))
		rad_e4.append(sum(radiation_e4[b:a, ixCFS, iyCFS]))
		rad_e5.append(sum(radiation_e5[c:d, ixCFS, iyCFS]))
		rad_e6.append(sum(radiation_e6[c:d, ixCFS, iyCFS]))
		rad_e7.append(sum(radiation_e7[c:d, ixCFS, iyCFS]))
		rad_e8.append(sum(radiation_e8[c:d, ixCFS, iyCFS]))

		if (sum(radiation_e1[b:a, ixCFS, iyCFS])) < 5:
			rad_e1.append(0)	
		if (sum(radiation_e2[b:a, ixCFS, iyCFS])) < 5:
			rad_e2.append(0)	
		if (sum(radiation_e3[b:a, ixCFS, iyCFS])) < 5:
			rad_e3.append(0)
		if (sum(radiation_e4[b:a, ixCFS, iyCFS])) < 5:
			rad_e4.append(0)
		if (sum(radiation_e5[b:a, ixCFS, iyCFS])) < 5:
			rad_e5.append(0)
		if (sum(radiation_e6[b:a, ixCFS, iyCFS])) < 5:
			rad_e6.append(0)
		if (sum(radiation_e7[b:a, ixCFS, iyCFS])) < 5:
			rad_e7.append(0)
		if (sum(radiation_e8[b:a, ixCFS, iyCFS])) < 5:
			rad_e8.append(0)
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
	for i in range(dia, max_j):
	## day 1
		if 500 <= rad_e1[i] < 750:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * rad_e1[i])
		elif rad_e1[i] < 500:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * rad_e1[i])
		elif rad_e1[i] >= 750: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * rad_e1[i])

		if 500 <= rad_e2[i] < 750:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * rad_e2[i])
		elif rad_e2[i] < 500:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * rad_e2[i])
		elif rad_e2[i] >= 750: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * rad_e2[i])		

		if 500 <= rad_e3[i] < 750:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * rad_e3[i])
		elif rad_e3[i] < 500:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * rad_e3[i])
		elif rad_e3[i] >= 750: 
			prob_g[i] += 0.175 #verde
	
		if 500 <= rad_e4[i] < 750:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * rad_e4[i])
		elif rad_e4[i] < 500:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * rad_e4[i])
		elif rad_e4[i] >= 750: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * rad_e4[i])
## day 2
		if 500 <= rad_e5[i] < 750:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * rad_e5[i])
		elif rad_e5[i] < 500:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * rad_e5[i])
		elif rad_e5[i] >= 750: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * rad_e5[i])
	
		if 500 <= rad_e6[i] < 750:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * rad_e6[i])
		elif rad_e6[i] < 500:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * rad_e6[i])
		elif rad_e6[i] >= 750: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * rad_e6[i])
		
		if 500 <= rad_e7[i] < 750:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * rad_e7[i])
		elif rad_e7[i] < 500:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * rad_e7[i])
		elif rad_e7[i] >= 750: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * rad_e7[i])
		
		if 500 <= rad_e8[i] < 750:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * rad_e8[i])
		elif rad_e8[i] < 500:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * rad_e8[i])
		elif rad_e8[i] >= 750: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * rad_e8[i])	

		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0) + datetime.timedelta(days = 10)
		date.append(d1)

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
			if val[i] < 500:			
				color[i] = 3
				prob[i] = 0.3
			elif val[i] >= 750:
				color[i] = 1
				prob[i] = 0.3
			else:
				color[i] = 2
				prob[i] = 0.3
	return(date, prob, color, val, max_j)
