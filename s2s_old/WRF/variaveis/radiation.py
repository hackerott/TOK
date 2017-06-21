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

##	Radiação


def calendario(WRFfile, iz, ixWRF, iyWRF,  date0, utc0):
	time = WRFfile.variables['time']
	WRF_rad = WRFfile.variables['SWDOWN']
	max_i = len(time)
	radW = np.empty((max_i_WRF,1))
	diaW = np.empty((max_i_WRF,1))
	corW = np.empty((max_i_WRF,1))
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz

	for i in range(0, max_i):
		radW[i] = WRF_rad[i, ixWRF, iyWRF]
		a = int(18)
		b = int(0)
	maxx = max_i % 24
	dia = iz % 24
	data = np.empty((maxx+1),1)
	for i in range(dia, maxx):
		diaW[i] = sum(radW[b:a]) / (a-b)
		izW[i] = b
		b = int(24 + utc0 + (i*24))
		a = int(a + 24)
		if diaW[i] < 200:
			corW[i] = 3 #vermelho
		elif diaW[i] < 260:
			corW[i] = 2 #amarelo
		else:
			corW[i] = 1 #verde

		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data[i] = d1.strftime('%A, %d/%m/%Y')

	return(data, corW, diaW, maxx)

####################################################################################################################
##	Tabela

def tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0)
	WRF_rad = ncfile.variables['SWDOWN']
	radW = np.empty((max_i,1))
	corW = np.empty((max_i,1))
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i	
	hora = np.empty((max_i,1))
	for i in range(0, max_i):
		radW[i] = WRF_rad[i, ixWRF, iyWRF]
		if radW[i] < 2000:
			cor[i] = 2 #amarelo
		elif radW[i] < 1000:
			cor[i] = 1 #vermelho
		else:
			cor[i] = 1 #verde
	d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
	hora[i] = d1.strftime('%d/%m %Hh')

	return(hora, corW, rh2W, max)


