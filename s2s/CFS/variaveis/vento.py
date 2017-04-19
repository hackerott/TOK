#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan, mean

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
		
	uvento_e1 = ens1.variables['ugrd10m']
	uvento_e2 = ens2.variables['ugrd10m']
	uvento_e3 = ens3.variables['ugrd10m']
	uvento_e4 = ens4.variables['ugrd10m']
	uvento_e5 = ens5.variables['ugrd10m']
	uvento_e6 = ens6.variables['ugrd10m']
	uvento_e7 = ens7.variables['ugrd10m']
	uvento_e8 = ens8.variables['ugrd10m']
	vvento_e1 = ens1.variables['vgrd10m']
	vvento_e2 = ens2.variables['vgrd10m']
	vvento_e3 = ens3.variables['vgrd10m']
	vvento_e4 = ens4.variables['vgrd10m']
	vvento_e5 = ens5.variables['vgrd10m']
	vvento_e6 = ens6.variables['vgrd10m']
	vvento_e7 = ens7.variables['vgrd10m']
	vvento_e8 = ens8.variables['vgrd10m']
	
	vento_e1	= []
	vento_e2	= []
	vento_e3	= []
	vento_e4	= [] 
	vento_e5	= []
	vento_e6	= []
	vento_e7	= []
	vento_e8	= []

	for i in range(0, max_i):
		vento_e1.append(sqrt(power(uvento_e1[i, ixCFS, iyCFS], 2) + power(vvento_e1[i, ixCFS, iyCFS], 2)))
		vento_e2.append(sqrt(power(uvento_e2[i, ixCFS, iyCFS], 2) + power(vvento_e2[i, ixCFS, iyCFS], 2)))
		vento_e3.append(sqrt(power(uvento_e3[i, ixCFS, iyCFS], 2) + power(vvento_e3[i, ixCFS, iyCFS], 2)))
		vento_e4.append(sqrt(power(uvento_e4[i, ixCFS, iyCFS], 2) + power(vvento_e4[i, ixCFS, iyCFS], 2)))

		vento_e5.append(sqrt(power(uvento_e5[i, ixCFS, iyCFS], 2) + power(vvento_e5[i, ixCFS, iyCFS], 2)))
		vento_e6.append(sqrt(power(uvento_e6[i, ixCFS, iyCFS], 2) + power(vvento_e6[i, ixCFS, iyCFS], 2)))
		vento_e7.append(sqrt(power(uvento_e7[i, ixCFS, iyCFS], 2) + power(vvento_e7[i, ixCFS, iyCFS], 2)))
		vento_e8.append(sqrt(power(uvento_e8[i, ixCFS, iyCFS], 2) + power(vvento_e8[i, ixCFS, iyCFS], 2)))
		

	max_j = max_i // 4
	dia = iz // 4
	data = []
	prob_g	= [0] * max_j
	prob_r	= [0] * max_j
	prob_y	= [0] * max_j
	prob	= []
	val_g	= [0] * max_j
	val_r	= [0] * max_j
	val_y	= [0] * max_j
	val	= []
	cor	= []
	

################################################################################	
	if iz == 0:
		a = 4
		b = iz
	else:
		a = iz + 4
		b = iz
	c = b + 4 
	d = a + 4	
	for i in range(dia, max_j):
		if a > max_i:
			break
		resp_e1 = vento_e1[b+argmax(vento_e1[b:a])]
		resp_e2 = vento_e2[b+argmax(vento_e2[b:a])]
		resp_e3 = vento_e3[b+argmax(vento_e3[b:a])]
		resp_e4 = vento_e4[b+argmax(vento_e4[b:a])]
		resp_e5 = vento_e5[b+argmax(vento_e5[b:a])]
		resp_e6 = vento_e6[b+argmax(vento_e6[b:a])]
		resp_e7 = vento_e7[b+argmax(vento_e7[b:a])]
		resp_e8 = vento_e8[b+argmax(vento_e8[b:a])]
		a += 4
		b += 4
		c += 4
		d += 4
################################################################################	
#	for i in range(dia, max_j):
	## dia 1
		if resp_e1 <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * resp_e1)
		elif resp_e1 >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * resp_e1)
		elif 1 < resp_e1 < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * resp_e1)

		if resp_e2 <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * resp_e2)
		elif resp_e2 >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * resp_e2)
		elif 1 < resp_e2 < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * resp_e2)		

		if resp_e3 <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * resp_e3)
		elif resp_e3 >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * resp_e3)
		elif 1 < resp_e3 < 10: 
			prob_g[i] += 0.175 #verde
	
		if resp_e4 <= 1:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * resp_e4)
		elif resp_e4 >= 10:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * resp_e4)
		elif 1 < resp_e4 < 10: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * resp_e4)
## dia 2
		if resp_e5 <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * resp_e5)
		elif resp_e5 >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * resp_e5)
		elif 1 < resp_e5 < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * resp_e5)
	
		if resp_e6 <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * resp_e6)
		elif resp_e6 >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * resp_e6)
		elif 1 < resp_e6 < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * resp_e6)
		
		if resp_e7 <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * resp_e7)
		elif resp_e7 >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * resp_e7)
		elif 1 < resp_e7 < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * resp_e7)
		
		if resp_e8 <= 1:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * resp_e8)
		elif resp_e8 >= 10:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * resp_e8)
		elif 1 < resp_e8 < 10: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * resp_e8)	

		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0) + datetime.timedelta(days = 10)
		data.append(d1)

	for i in range(dia, max_j):
		if   prob_y[i] > prob_r[i] and prob_y[i] > prob_g[i]:
			cor.append(2) 
			prob.append(prob_y[i])
			val.append(val_y[i]/prob_y[i])
		elif prob_r[i] > prob_y[i] and prob_r[i] > prob_g[i]:
			cor.append(3)
			prob.append(prob_r[i])
			val.append(val_r[i]/prob_r[i])
		elif prob_g[i] > prob_y[i] and prob_g[i] > prob_r[i]:
			cor.append(1)
			prob.append(prob_g[i])
			val.append(val_g[i]/prob_g[i])
		elif prob_y[i] == prob_r[i] and prob_y[i] > prob_g[i]:
			cor.append(2)
			prob.append(prob_y[i] + pro_g[i]/2)
			val.append((2.5*(val_y[i]/prob_y[i]) + 0.5*(val_g[i]/prob_g[i]))/3)
		elif prob_r[i] == prob_g[i] and prob_r[i] > prob_y[i]:
			cor.append(3)
			prob.append(prob_r[i] + prob_y[i]/2)
			val.append((2.5*(val_r[i]/prob_r[i]) + 0.5*(val_y[i]/prob_y[i]))/3)
		elif prob_g[i]  == prob_y[i] and prob_g[i] > prob_r[i]:
			cor.append(1)
			prob.append(prob_g[i] + prob_r[i]/2)
			val.append((2.5*(val_g[i]/prob_g[i]) + 0.5*(val_r[i]/prob_r[i]))/3)
		elif prob_y[i] == prob_r[i] and prob_y[i] < prob_g[i]:
			cor.append(1)
			prob.append(prob_g[i] + prob_y[i]/2)
			val.append((2.5*(val_g[i]/prob_g[i]) + 0.5*(val_y[i]/prob_y[i]))/3)
		elif prob_r[i] == prob_g[i] and prob_r[i] < prob_y[i]:
			cor.append(2)
			prob.append(prob_y[i] + prob_r/2)
			val.append((2.5*(val_y[i]/prob_y[i]) + 0.5*(val_r[i]/prob_r[i]))/3)
		elif prob_g[i]  == prob_y[i] and prob_g[i] < prob_r[i]:
			cor.append(3)
			prob.append(prob_r[i] + prob_g[i]/2)
			val.append((2.5*(val_r[i]/prob_r[i]) + 0.5*(val_g[i]/prob_g[i]))/3)
		else:
			val.append((val_r[i] + val_g[i] + val_y[i])/3)
			if val[i] <= 1:			
				cor.append(3)
				prob.append(0.3)
			elif val[i] <= 10:
				cor.append(1)
				prob.append(0.3)
			else:
				cor.append(2)
				prob.append(0.3)
	return(data, prob, cor, val, max_j)


