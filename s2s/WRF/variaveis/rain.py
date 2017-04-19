#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

######Chuva

##		Calendario

def calendario(WRFfile, iz, ixWRF, iyWRF,  date0, utc0):
	WRF_chuva_cu = WRFfile.variables['RAINC']
	WRF_chuva_ncu = WRFfile.variables['RAINNC']
	time = WRFfile.variables['time']  
	max_i = len(time)

	chuvaW = np.empty((max_i+1,1))
	diaW_max = np.empty((max_i+1,1))
	corW = np.empty((max_i+1,1))

	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz
 
	for i in range(0, max_i):
		chuvaW[i] = (WRF_chuva_cu[i, ixWRF, iyWRF] +  WRF_chuva_ncu[i, ixWRF, iyWRF]) - (WRF_chuva_cu[i - 1, ixWRF, iyWRF] + WRF_chuva_ncu[i - 1, ixWRF, iyWRF])

		if chuvaW[i] < 0.02:
			chuvaW[i] = 0
	maxx = max_i % 24
	dia = iz % 24
	data = np.empty((maxx+1),1)
	for i in range(dia, maxx):
		diaW_max[i] = sum(chuvaW[b:a])
		if diaW_max[i] < 0:
			diaW_max[i] = 0	
		if diaW_max[i] > 1:
			corW[i] = 2 #amarelo
		elif diaW_max[i] > 10:
			corW[i] = 3 #vermelho
		else :
			corW[i] = 1 #verde
			
		b = 24 + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data[i] = d1.strftime('%A, %d/%m/%Y')

	return(data, corW, diaW_max, maxx)

####################################################################################################################
##		Tabela 

def tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0)
	time = WRFfile.variables['Times']
	max_i = len(time)
	time_step = 1

	WRF_chuva_cu = ncfile.variables['RAINC']
	WRF_chuva_ncu = ncfile.variables['RAINNC']
	chuvaW = [None]*max_i
	corW = [None]*max_i
	
	max = iz + 24
	if  iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = np.empty((max_i,1))
	for i in range (iz, max):
		chuvaW[i] = (WRF_chuva_cu[i, ixWRF, iyWRF] +  WRF_chuva_ncu[i, ixWRF, iyWRF]) - (WRF_chuva_cu[i - 1, ixWRF, iyWRF] + WRF_chuva_ncu[i - 1, ixWRF, iyWRF])
		if chuvaW[i] > 10:
			corW[i] = "RED" #amarelo
		elif chuvaW[i] > 0.1:
			corW[i] = "YELLOW"#vermelho
		else :
			corW[i] = "GREEN" #verde
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
		hora[i] = d1.strftime('%d/%m %Hh')

	return(hora, corW, chuvaW, max)

