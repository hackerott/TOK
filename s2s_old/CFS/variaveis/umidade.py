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
	q2_e1 = ens1.variables['spfh2m']
	q2_e2 = ens2.variables['spfh2m']
	q2_e3 = ens3.variables['spfh2m']
	q2_e4 = ens4.variables['spfh2m']
	q2_e5 = ens5.variables['spfh2m']
	q2_e6 = ens6.variables['spfh2m']
	q2_e7 = ens7.variables['spfh2m']
	q2_e8 = ens8.variables['spfh2m']
	t2_e1 = ens1.variables['tmp2m']
	t2_e2 = ens2.variables['tmp2m']
	t2_e3 = ens3.variables['tmp2m']
	t2_e4 = ens4.variables['tmp2m']
	t2_e5 = ens5.variables['tmp2m']
	t2_e6 = ens6.variables['tmp2m']
	t2_e7 = ens7.variables['tmp2m']
	t2_e8 = ens8.variables['tmp2m']
	p2_e1 = ens1.variables['pressfc']
	p2_e2 = ens2.variables['pressfc']
	p2_e3 = ens3.variables['pressfc']
	p2_e4 = ens4.variables['pressfc']
	p2_e5 = ens5.variables['pressfc']
	p2_e6 = ens6.variables['pressfc']
	p2_e7 = ens7.variables['pressfc']
	p2_e8 = ens8.variables['pressfc']
 
	rh2_e1 = []
	rh2_e2 = []
	rh2_e3 = []
	rh2_e4 = []
	rh2_e5 = []
	rh2_e6 = []
	rh2_e7 = []
	rh2_e8 = []
	for i in range(0, max_i):
		rh2_e1.append(100*(q2_e1[i, ixCFS, iyCFS]/(379.90516/p2_e1[i, ixCFS, iyCFS] * exp(17.29*((t2_e1[i, ixCFS, iyCFS] - 273.15)/(t2_e1[i, ixCFS, iyCFS] - 35.86))))))
		rh2_e2.append(100*(q2_e2[i, ixCFS, iyCFS]/(379.90516/p2_e2[i, ixCFS, iyCFS] * exp(17.29*((t2_e2[i, ixCFS, iyCFS] - 273.15)/(t2_e2[i, ixCFS, iyCFS] - 35.86))))))
		rh2_e3.append(100*(q2_e3[i, ixCFS, iyCFS]/(379.90516/p2_e3[i, ixCFS, iyCFS] * exp(17.29*((t2_e3[i, ixCFS, iyCFS] - 273.15)/(t2_e3[i, ixCFS, iyCFS] - 35.86))))))
		rh2_e4.append(100*(q2_e4[i, ixCFS, iyCFS]/(379.90516/p2_e4[i, ixCFS, iyCFS] * exp(17.29*((t2_e4[i, ixCFS, iyCFS] - 273.15)/(t2_e4[i, ixCFS, iyCFS] - 35.86))))))
		rh2_e5.append(100*(q2_e5[i, ixCFS, iyCFS]/(379.90516/p2_e5[i, ixCFS, iyCFS] * exp(17.29*((t2_e5[i, ixCFS, iyCFS] - 273.15)/(t2_e5[i, ixCFS, iyCFS] - 35.86))))))
		rh2_e6.append(100*(q2_e6[i, ixCFS, iyCFS]/(379.90516/p2_e6[i, ixCFS, iyCFS] * exp(17.29*((t2_e6[i, ixCFS, iyCFS] - 273.15)/(t2_e6[i, ixCFS, iyCFS] - 35.86))))))
		rh2_e7.append(100*(q2_e7[i, ixCFS, iyCFS]/(379.90516/p2_e7[i, ixCFS, iyCFS] * exp(17.29*((t2_e7[i, ixCFS, iyCFS] - 273.15)/(t2_e7[i, ixCFS, iyCFS] - 35.86))))))
		rh2_e8.append(100*(q2_e8[i, ixCFS, iyCFS]/(379.90516/p2_e8[i, ixCFS, iyCFS] * exp(17.29*((t2_e8[i, ixCFS, iyCFS] - 273.15)/(t2_e8[i, ixCFS, iyCFS] - 35.86))))))

	max_j = max_i // 4
	dia = iz // 4
	data = []
	rh_e1 = []
	rh_e2 = []
	rh_e3 = []
	rh_e4 = []
	rh_e5 = []
	rh_e6 = []
	rh_e7 = []
	rh_e8 = []
	for i in range(dia, max_j):
		rh_e1.append(rh2_e1[argmin(rh2_e1[b:a]) + b])
		rh_e2.append(rh2_e2[argmin(rh2_e2[b:a]) + b])
		rh_e3.append(rh2_e3[argmin(rh2_e3[b:a]) + b])
		rh_e4.append(rh2_e4[argmin(rh2_e4[b:a]) + b])
		rh_e5.append(rh2_e5[argmin(rh2_e5[b:a]) + b])
		rh_e6.append(rh2_e6[argmin(rh2_e6[b:a]) + b])
		rh_e7.append(rh2_e7[argmin(rh2_e7[b:a]) + b])
		rh_e8.append(rh2_e8[argmin(rh2_e8[b:a]) + b])

		if rh2_e1[argmin(rh2_e1[b:a]) + b] < 1.5:
			rh_e1.append(0)	
		if rh2_e2[argmin(rh2_e2[b:a]) + b] < 1.5:
			rh_e2.append(0)	
		if rh2_e3[argmin(rh2_e3[b:a]) + b] < 1.5:
			rh_e3.append(0)
		if rh2_e4[argmin(rh2_e4[b:a]) + b] < 1.5:
			rh_e4.append(0)
		if rh2_e5[argmin(rh2_e5[b:a]) + b] < 1.5:
			rh_e5.append(0)
		if rh2_e6[argmin(rh2_e6[b:a]) + b] < 1.5:
			rh_e6.append(0)
		if rh2_e7[argmin(rh2_e7[b:a]) + b] < 1.5:
			rh_e7.append(0)
		if rh2_e8[argmin(rh2_e8[b:a]) + b] < 1.5:
			rh_e8.append(0)
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
		if 80 < rh_e1[i] <= 90:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * rh_e1[i])
		elif rh_e1[i] > 90:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * rh_e1[i])
		elif rh_e1[i]<= 80: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * rh_e1[i])

		if 80 < rh_e2[i] <= 90:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * rh_e2[i])
		elif rh_e2[i] > 90:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * rh_e2[i])
		elif rh_e2[i]<= 80: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * rh_e2[i])		

		if 80 < rh_e3[i] <= 90:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * rh_e3[i])
		elif rh_e3[i] > 90:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * rh_e3[i])
		elif rh_e3[i]<= 80: 
			prob_g[i] += 0.175 #verde
	
		if 80 < rh_e4[i] <= 90:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * rh_e4[i])
		elif rh_e4[i] > 90:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * rh_e4[i])
		elif rh_e4[i]<= 80: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * rh_e4[i])
## dia 2
		if 80 < rh_e5[i] <= 90:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * rh_e5[i])
		elif rh_e5[i] > 90:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * rh_e5[i])
		elif rh_e5[i]<= 80: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * rh_e5[i])
	
		if 80 < rh_e6[i] <= 90:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * rh_e6[i])
		elif rh_e6[i] > 90:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * rh_e6[i])
		elif rh_e6[i]<= 80: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * rh_e6[i])
		
		if 80 < rh_e7[i] <= 90:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * rh_e7[i])
		elif rh_e7[i] > 90:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * rh_e7[i])
		elif rh_e7[i]<= 80: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * rh_e7[i])
		
		if 80 < rh_e8[i] <= 90:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * rh_e8[i])
		elif rh_e8[i] > 90:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * rh_e8[i])
		elif rh_e8[i]<= 80: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * rh_e8[i])	

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
			if val[i] > 90:			
				cor[i] = 3
				prob[i] = 0.3
			elif val[i]<= 80:
				cor[i] = 1
				prob[i] = 0.3
			else:
				cor[i] = 2
				prob[i] = 0.3
	return(data, prob, cor, val, max_j)
