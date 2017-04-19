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
	chuva_e1 = ens1.variables['pratesfc']
	chuva_e2 = ens2.variables['pratesfc']
	chuva_e3 = ens3.variables['pratesfc']
	chuva_e4 = ens4.variables['pratesfc']
	chuva_e5 = ens5.variables['pratesfc']
	chuva_e6 = ens6.variables['pratesfc']
	chuva_e7 = ens7.variables['pratesfc']
	chuva_e8 = ens8.variables['pratesfc']

	max_j = max_i // 4
	dia = iz // 4
	data = []
	chu_e1 = []
	chu_e2 = []
	chu_e3 = []
	chu_e4 = []
	chu_e5 = []
	chu_e6 = []
	chu_e7 = []
	chu_e8 = []
	for i in range(dia, max_j):
		chu_e1.append(sum(chuva_e1[b:a, ixCFS, iyCFS]))
		chu_e2.append(sum(chuva_e2[b:a, ixCFS, iyCFS]))
		chu_e3.append(sum(chuva_e3[b:a, ixCFS, iyCFS]))
		chu_e4.append(sum(chuva_e4[b:a, ixCFS, iyCFS]))
		chu_e5.append(sum(chuva_e5[c:d, ixCFS, iyCFS]))
		chu_e6.append(sum(chuva_e6[c:d, ixCFS, iyCFS]))
		chu_e7.append(sum(chuva_e7[c:d, ixCFS, iyCFS]))
		chu_e8.append(sum(chuva_e8[c:d, ixCFS, iyCFS]))

		if (sum(chuva_e1[b:a, ixCFS, iyCFS])) < 0.01:
			chu_e1.append(0)	
		if (sum(chuva_e2[b:a, ixCFS, iyCFS])) < 0.01:
			chu_e2.append(0)	
		if (sum(chuva_e3[b:a, ixCFS, iyCFS])) < 0.01:
			chu_e3.append(0)
		if (sum(chuva_e4[b:a, ixCFS, iyCFS])) < 0.01:
			chu_e4.append(0)
		if (sum(chuva_e5[b:a, ixCFS, iyCFS])) < 0.01:
			chu_e5.append(0)
		if (sum(chuva_e6[b:a, ixCFS, iyCFS])) < 0.01:
			chu_e6.append(0)
		if (sum(chuva_e7[b:a, ixCFS, iyCFS])) < 0.01:
			chu_e7.append(0)
		if (sum(chuva_e8[b:a, ixCFS, iyCFS])) < 0.01:
			chu_e8.append(0)
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
	cor	= [0] * max_j
	for i in range(dia, max_j):
	## dia 1
		if chu_e1[i] <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * chu_e1[i])
		elif chu_e1[i] >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * chu_e1[i])
		elif 1 < chu_e1[i] < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * chu_e1[i])

		if chu_e2[i] <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * chu_e2[i])
		elif chu_e2[i] >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * chu_e2[i])
		elif 1 < chu_e2[i] < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * chu_e2[i])		

		if chu_e3[i] <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * chu_e3[i])
		elif chu_e3[i] >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * chu_e3[i])
		elif 1 < chu_e3[i] < 10: 
			prob_g[i] += 0.175 #verde
	
		if chu_e4[i] <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * chu_e4[i])
		elif chu_e4[i] >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * chu_e4[i])
		elif 1 < chu_e4[i] < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * chu_e4[i])
## dia 2
		if chu_e5[i] <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * chu_e5[i])
		elif chu_e5[i] >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * chu_e5[i])
		elif 1 < chu_e5[i] < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * chu_e5[i])
	
		if chu_e6[i] <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * chu_e6[i])
		elif chu_e6[i] >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * chu_e6[i])
		elif 1 < chu_e6[i] < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * chu_e6[i])
		
		if chu_e7[i] <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * chu_e7[i])
		elif chu_e7[i] >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * chu_e7[i])
		elif 1 < chu_e7[i] < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * chu_e7[i])
		
		if chu_e8[i] <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * chu_e8[i])
		elif chu_e8[i] >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * chu_e8[i])
		elif 1 < chu_e8[i] < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * chu_e8[i])	

		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0) + datetime.timedelta(days = 10)
		data.append(d1)

	for i in range(dia, max_j):
		if   prob_y[i] > prob_r[i] and prob_y[i] > prob_g[i]:
			cor[i] = 2 
			prob[i] = prob_y[i]
			val[i] = val_y[i]/prob_y[i]
		elif prob_r[i] > prob_y[i] and prob_r[i] > prob_g[i]:
			cor[i] = 3
			prob[i] = prob_r[i]
			val[i] = val_r[i]/prob_r[i] 
		elif prob_g[i] > prob_y[i] and prob_g[i] > prob_r[i]:
			cor[i] = 1
			prob[i] = prob_g[i]
			val[i] = val_g[i]/prob_g[i]
		elif prob_y[i] == prob_r[i] and prob_y[i] > prob_g[i]:
			cor[i] = 2
			prob[i] = prob_y[i] + pro_g[i]/2
			val[i] = (2.5*(val_y[i]/prob_y[i]) + 0.5*(val_g[i]/prob_g[i]))/3
		elif prob_r[i] == prob_g[i] and prob_r[i] > prob_y[i]:
			cor[i] = 3
			prob[i] = prob_r[i] + prob_y[i]/2
			val[i] = (2.5*(val_r[i]/prob_r[i]) + 0.5*(val_y[i]/prob_y[i]))/3
		elif prob_g[i]  == prob_y[i] and prob_g[i] > prob_r[i]:
			cor[i] = 1
			prob[i] = prob_g[i] + prob_r[i]/2
			val[i] = (2.5*(val_g[i]/prob_g[i]) + 0.5*(val_r[i]/prob_r[i]))/3
		elif prob_y[i] == prob_r[i] and prob_y[i] < prob_g[i]:
			cor[i] = 1
			prob[i] = prob_g[i] + prob_y[i]/2
			val[i] = (2.5*(val_g[i]/prob_g[i]) + 0.5*(val_y[i]/prob_y[i]))/3			
		elif prob_r[i] == prob_g[i] and prob_r[i] < prob_y[i]:
			cor[i] = 2
			prob[i] =  prob_y[i] + prob_r/2
			val[i] = (2.5*(val_y[i]/prob_y[i]) + 0.5*(val_r[i]/prob_r[i]))/3
		elif prob_g[i]  == prob_y[i] and prob_g[i] < prob_r[i]:
			cor[i] = 3
			prob[i] = prob_r[i] + prob_g[i]/2
			val[i] = (2.5*(val_r[i]/prob_r[i]) + 0.5*(val_g[i]/prob_g[i]))/3
		else:
			val[i] = (val_r[i] + val_g[i] + val_y[i])/3
			if val[i] <= 1:			
				cor[i] = 3
				prob[i] = 0.3
			elif val[i] <= 10:
				cor[i] = 1
				prob[i] = 0.3
			else:
				cor[i] = 2
				prob[i] = 0.3
	return(data, prob, cor, val, max_j)
