#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import math
import sys
#import calendar
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

###Umidade
def calendario(WRFfile, iz, ixWRF, iyWRF,  date0, utc0):
	time = WRFfile.variables['time']
	max_i = len(time)
	WRF_q2 = WRFfile.variables['Q2']
	WRF_pres = WRFfile.variables['PSFC']
	WRF_t2 = WRFfile.variables['T2']

	rh2W = np.empty((max_i_WRF,1))
#	tempW = np.empty((max_i_WRF,1))
    
	diaW_min = np.empty((max_i_WRF,1))
	corW = np.empty((max_i_WRF,1))

	for i in range(0, max_i_WRF):
		tempW = WRF_t2[i, ixWRF, iyWRF]
		a5 = 17.2693882 * (tempW - 273.15) / (tempW - 35.86)
		rh2W[i] = 100 * (WRF_q2[i, ixWRF, iyWRF] / ((379.90516 / WRF_pres[i, ixWRF, iyWRF]) * exp(a5)))
	if rh2W[i] < 0:
		rh2W[i] = 0
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz

	maxx = max_i % 24
	dia = iz % 24
	data = np.empty((maxx+1),1)
	for i in range(dia, maxx):
		i_min = argmin(rh2W[b:a]) 	
		diaW_min[i] = rh2W[i_min+b]	
		izW[i] = b
		b = 24 + utc0 + (i*24)
		a = a + 24
		if diaW_min[i] > 90:
			corW[i] = 2 #amarelo
		elif diaW_min[i] > 80:
			corW[i] = 2 #vermelho
		else :
			corW[i] = 1 #verde
		d1 = date1 + datetime.timedelta(hours = 6 + utc0) + datetime.timedelta(days = i) 
		data[i] = d1.strftime('%A, %d/%m/%Y')
	return(data, corW, diaW_min, maxx)

####################################################################################################################
##	Tabela

def tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0)
	time = WRFfile.variables['time']
	WRF_q2 = ncfile.variables['Q2']
	WRF_pres = ncfile.variables['PSFC'
	WRF_t2 = ncfile.variables['T2']
	rh2W = np.empty((max_i,1))
	tempW = np.empty((max_i,1))
	corW = np.empty((max_i,1))
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i	
	hora = np.empty((max_i,1))
	for i in range(iz, max_i):
		tempW[i] = WRF_t2[i, ixWRF, iyWRF]
		a5 = 17.2693882 * (tempk[i, ixWRF, iyWRF] - 273.15) / (tempk[i, ixWRF, iyWRF] - 35.86)
		rh2W[i] = 100 * (WRF_q2[i, ixWRF, iyWRF] / ((379.90516 / WRF_pres[i, ixWRF, iyWRF]) * exp(a5)))
		if rh2W[i] > 80:
			cor[i] = 2 #amarelo
		elif rh2W_max[i] > 90:
			cor[i] = 1 #vermelho
		else :
			cor[i] = 1 #verde
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
		hora[i] = d1.strftime('%d/%m %Hh')

	return(hora, corW, rh2W, max)

