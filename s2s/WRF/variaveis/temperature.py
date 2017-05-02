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

###Temperatura

def calendario(WRFfile, iz, ixWRF, iyWRF,  date0, utc0):
	time = WRFfile.variables['time']
	WRF_t2 = WRFfile.variables['T2']
	max_i = len(time)
 	tempW = np.empty((max_i,1))
	diaW_max = np.empty((max_i,1))
	diaW_min = np.empty((max_i,1))
	corW = np.empty((max_i,1))
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz
	for i in range(0, max_i):
		tempW[i] = WRF_t2[i, ixWRF, iyWRF] - 273.15
	maxx = max_i % 24
	dia = iz % 24
	data = np.empty((maxx+1),1)
	for i in range(dia, maxx):
		i_min = argmin(tempW[b:a]) 	
		diaW_min[i] = tempW[i_min+b]	
		i_max = argmax(tempW[b:a]) 	
		diaW_max[i] = tempW[i_max+b]	
		izW[i] = b
		if diaW_max[i] > 30:
			corW[i] = 3 #vermelho
		elif diaW_max[i] < 23:
			corW[i] = 1 #verde
		else :
			corW[i] = 2 #amarelo
		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data[i] = d1.strftime('%A, %d/%m/%Y')


	return(data, corW, diaW_min, diaW_max, maxx) 


####################################################################################################################


def tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0)
	time = WRFfile.variables['time']
	WRF_t2 = WRFfile.variables['T2']
	max_i = len(time)
	tempW = np.empty((max_i,1))
	corW = [None]*max_i
	
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = np.empty((max_i,1))
	for i in range (iz, max):
		tempW[i] = WRF_t2[i, ixWRF, iyWRF] - 273.15
		if tempW[i] > 30:
			corW[i] = "RED"
		elif tempW[i] < 23:
			corW[i] = "GREEN" #verde
		else:
			corW[i] = "YELLOW" #amarelo

		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
		hora[i] = d1.strftime('%d/%m %Hh')

	return(hora, corW, tempW, max)



