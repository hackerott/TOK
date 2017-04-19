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
	c = b + 4
	d = a + 4	
		
	tempk_e1 = ens1.variables['tmp2m']
	tempk_e2 = ens2.variables['tmp2m']
	tempk_e3 = ens3.variables['tmp2m']
	tempk_e4 = ens4.variables['tmp2m']
	tempk_e5 = ens5.variables['tmp2m']
	tempk_e6 = ens6.variables['tmp2m']
	tempk_e7 = ens7.variables['tmp2m']
	tempk_e8 = ens8.variables['tmp2m']
	tempk1 = [0] * max_i
	tempk2 = [0] * max_i
	tempk3 = [0] * max_i
	tempk4 = [0] * max_i
	tempk5 = [0] * max_i
	tempk6 = [0] * max_i
	tempk7 = [0] * max_i
	tempk8 = [0] * max_i

	for i in range(0, max_i):
		tempk1[i] = tempk_e1[i, ixCFS, iyCFS]
		tempk2[i] = tempk_e2[i, ixCFS, iyCFS]
		tempk3[i] = tempk_e3[i, ixCFS, iyCFS]
		tempk4[i] = tempk_e4[i, ixCFS, iyCFS]
		tempk5[i] = tempk_e5[i, ixCFS, iyCFS]
		tempk6[i] = tempk_e6[i, ixCFS, iyCFS]
		tempk7[i] = tempk_e7[i, ixCFS, iyCFS]
		tempk8[i] = tempk_e8[i, ixCFS, iyCFS]

	max_j = max_i // 4
	dia = iz // 4
#	data = [None]*(max_j+1)
	data = []
	if iz == 0:
		a = 4
		b = iz
	else:
		a = iz + 4
		b = iz
	c = b + 4 
	d = a + 4	
################################################################################	
	temp1 = [0] * max_j
	temp2 = [0] * max_j
	temp3 = [0] * max_j
	temp4 = [0] * max_j
	temp5 = [0] * max_j
	temp6 = [0] * max_j
	temp7 = [0] * max_j
	temp8 = [0] * max_j
	temp_min1 = [0] * max_j
	temp_min2 = [0] * max_j
	temp_min3 = [0] * max_j
	temp_min4 = [0] * max_j
	temp_min5 = [0] * max_j
	temp_min6 = [0] * max_j
	temp_min7 = [0] * max_j
	temp_min8 = [0] * max_j
	temp_max1 = [0] * max_j
	temp_max2 = [0] * max_j
	temp_max3 = [0] * max_j
	temp_max4 = [0] * max_j
	temp_max5 = [0] * max_j
	temp_max6 = [0] * max_j
	temp_max7 = [0] * max_j
	temp_max8 = [0] * max_j
	resp_e1 = [0] * max_j
	resp_e2 = [0] * max_j
	resp_e3 = [0] * max_j
	resp_e4 = [0] * max_j
	resp_e5 = [0] * max_j
	resp_e6 = [0] * max_j
	resp_e7 = [0] * max_j
	resp_e8 = [0] * max_j
	prob_y = [0.0] * max_j
	prob_r = [0.0] * max_j
	prob_g = [0.0] * max_j
	prob   = [0.0] * max_j
	val_y = [0] * max_j
	val_r = [0] * max_j
	val_g = [0] * max_j
	val   = [0] * max_j
	cor   = [0] * max_j

	for i in range(0, max_j):
		temp1[i]     = mean(tempk1[b:a]) - 273.15
		temp_min1[i] = tempk1[b + argmin(tempk1[b:a])] - 273.15
		temp_max1[i] = tempk1[b + argmax(tempk1[b:a])] - 273.15

		temp2[i]  = mean(tempk2[b:a]) - 273.15
		temp_min2[i] = tempk2[b + argmin(tempk2[b:a])] - 273.15
		temp_max2[i] = tempk2[b + argmax(tempk2[b:a])] - 273.15

		temp3[i]  = mean(tempk3[b:a]) - 273.15
		temp_min3[i] = tempk3[b + argmin(tempk3[b:a])] - 273.15
		temp_max3[i] = tempk3[b + argmax(tempk3[b:a])] - 273.15

		temp4[i] = mean(tempk4[b:a]) - 273.15
		temp_min4[i] = tempk4[b + argmin(tempk4[b:a])] - 273.15
		temp_max4[i] = tempk4[b + argmax(tempk4[b:a])] - 273.15

		temp5[i] = mean(tempk5[c:d]) - 273.15
		temp_min5[i] = tempk5[b + argmin(tempk5[c:d])] - 273.15
		temp_max5[i] = tempk5[b + argmax(tempk5[c:d])] - 273.15

		temp6[i] = mean(tempk6[c:d]) - 273.15
		temp_min6[i] = tempk6[b + argmin(tempk6[c:d])] - 273.15
		temp_max6[i] = tempk6[b + argmax(tempk6[c:d])] - 273.15

		temp7[i] = mean(tempk7[c:d]) - 273.15
		temp_min7[i] = tempk7[b + argmin(tempk7[c:d])] - 273.15
		temp_max7[i] = tempk7[b + argmax(tempk7[c:d])] - 273.15

		temp8[i] = mean(tempk8[c:d]) - 273.15
		temp_min8[i] = tempk8[b + argmin(tempk8[c:d])] - 273.15
		temp_max8[i] = tempk8[b + argmax(tempk8[c:d])] - 273.15
		a += 4
		b += 4
		c += 4
		d += 4
		if a > max_i or d > max_i: 
			break
	for i in range(dia, max_j):
		resp_e1[i] = temp_max1[i]
		resp_e2[i] = temp_max2[i]
		resp_e3[i] = temp_max3[i]
		resp_e4[i] = temp_max4[i]
		resp_e5[i] = temp_max5[i]
		resp_e6[i] = temp_max6[i]
		resp_e7[i] = temp_max7[i]
		resp_e8[i] = temp_max8[i]


################################################################################	
	for i in range(dia, max_j):
	## dia 1
		if resp_e1[i] >= 23 and resp_e1[i] < 30:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * resp_e1[i])
		elif resp_e1[i] >= 30:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * resp_e1[i])
		elif 1 < resp_e1[i] < 23: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * resp_e1[i])
			
		if resp_e2[i] >= 23 and resp_e2[i] < 30:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * resp_e2[i])
		elif resp_e2[i] >= 30:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * resp_e2[i])
		elif 1 < resp_e2[i] < 23: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * resp_e2[i])		

		if resp_e3[i] >= 23 and resp_e3[i] < 30:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * resp_e3[i])
		elif resp_e3[i] >= 30:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * resp_e3[i])
		elif 1 < resp_e3[i] < 23: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * resp_e3[i])	

		if resp_e4[i] >= 23 and resp_e4[i] < 30:
			prob_y[i] += 0.175
			val_y[i] += (0.175 * resp_e4[i])
		elif resp_e4[i] >= 30:
			prob_r[i] += 0.175 #vermelho
			val_r[i] += (0.175 * resp_e4[i])
		elif 1 < resp_e4[i] < 23: 
			prob_g[i] += 0.175 #verde
			val_g[i] += (0.175 * resp_e4[i])
## dia 2
		if resp_e5[i] >= 23 and resp_e5[i] < 30:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * resp_e5[i])
		elif resp_e5[i] >= 30:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * resp_e5[i])
		elif 1 < resp_e5[i] < 23: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * resp_e5[i])

		if resp_e6[i] >= 23 and resp_e6[i] < 30:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * resp_e6[i])
		elif resp_e6[i] >= 30:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * resp_e6[i])
		elif 1 < resp_e6[i] < 23: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * resp_e6[i])
		
		if resp_e7[i] >= 23 and resp_e7[i] < 30:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * resp_e7[i])
		elif resp_e7[i] >= 30:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * resp_e7[i])
		elif 1 < resp_e7[i] < 23: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * resp_e7[i])
		
		if resp_e8[i] >= 23 and resp_e8[i] < 30:
			prob_y[i] += 0.075
			val_y[i] += (0.075 * resp_e8[i])
		elif resp_e8[i] >= 30:
			prob_r[i] += 0.075 #vermelho
			val_r[i] += (0.075 * resp_e8[i])
		elif 1 < resp_e8[i] < 23: 
			prob_g[i] += 0.075 #verde
			val_g[i] += (0.075 * resp_e8[i])	
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0) + + datetime.timedelta(days = 10)
#		data[i] = d1.strftime('%A, %d/%m/%Y')
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
			val[i] = (2.5*(val_g[i]/prob_g[i])) 
#+ 0.5*(val_r[i]/prob_r[i]))/3
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
			if val[i] >= 30:			
				cor[i] = 3
				prob[i] = 0.3
			elif val[i] < 23:
				cor[i] = 1
				prob[i] = 0.3
			else:
				cor[i] = 2
				prob[i] = 0.3
#		print "cor", cor[i],"prob", prob[i]*100,"val", val[i], "R", prob_r[i]*100, "G", prob_g[i]*100, "Y", prob_y[i]*100,  "I", i
#		print temp1[i], temp_max1[i], temp_min1[i]
#		print temp2[i], temp_max2[i], temp_min2[i]
#		print temp3[i], temp_max3[i], temp_min3[i]
#		print temp4[i], temp_max4[i], temp_min4[i]
#		print ""
#		print temp5[i], temp_max5[i], temp_min5[i]
#		print temp6[i], temp_max6[i], temp_min6[i]
#		print temp7[i], temp_max7[i], temp_min7[i]
#		print temp8[i], temp_max8[i], temp_min8[i]
#		print ""
#		print ""
#		print ""
				
	return(data, prob, cor, val, max_j)

