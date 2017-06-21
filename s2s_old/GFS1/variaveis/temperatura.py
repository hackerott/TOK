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

def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	GFS_t2 = GFSfile.variables['tmp2m']
	max_i = len(time)
 	tempG = np.empty((max_i,1))
	diaG_max = np.empty((max_i,1))
	diaG_min = np.empty((max_i,1))
	corG = np.empty((max_i,1))
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz
	for i in range(0, max_i):
		tempG[i] = GFS_t2[i, ixGFS, iyGFS] - 273.15
	maxx = max_i // 24
	dia = iz // 24
	data = [None]*(maxx+1)
	for i in range(dia, maxx):
		if a > max_i:
			break

		else:
			i_min = argmin(tempG[b:a]) 	
			diaG_min[i] = tempG[i_min+b]	
			i_max = argmax(tempG[b:a]) 	
			diaG_max[i] = tempG[i_max+b]	
			if diaG_max[i] > 30:
				corG[i] = 3 #vermelho
			elif diaG_max[i] < 23:
				corG[i] = 1 #verde
			else :
				corG[i] = 2 #amarelo
			b = iz + (i*24)
			a = a + 24
			d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
			data[i] = d1

	return(data, corG, diaG_min, diaG_max, maxx) 

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0):
	time = GFSfile.variables['time']
	GFS_t2 = GFSfile.variables['T2']
	max_i = len(time)
	tempG = np.empty((max_i,1))
	corG = [None]*max_i
	
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = []
	for i in range (iz, max):
		tempG[i] = GFS_t2[i, ixGFS, iyGFS] - 273.15
		if tempG[i] > 40:
			corG[i] = 15 #7d0006
		elif 36 <= tempG[i] < 40:
			corG[i] = 14 #a70039
		elif 32 <= tempG[i] < 36:
			corG[i] = 13 #f90018
		elif 28 <= tempG[i] < 32:
			corG[i] = 12 #fb982c
		elif 24 <= tempG[i] < 28:
			corG[i]	= 11 #fefe45
		elif 20 <= tempG[i] < 24:
			corG[i] = 10 #9fd436
		elif 16 <= tempG[i] < 20:
			corG[i] = 9  #17801b
		elif 12 <= tempG[i] < 16:
			corG[i] = 8  #7f7f1e
		elif  8 <= tempG[i] < 12:
			corG[i] = 7  #acacac
		elif  4 <= tempG[i] <  8:
			corG[i] = 6  #d7d7d7
		elif  0 <= tempG[i] <  4:
			corG[i] = 5  #89a3fb
		elif -4 <= tempG[i] <  0:
			corG[i] = 4  #4c4bf9
		elif -8 <= tempG[i] < -4:
			corG[i] = 3  #7e047d
		elif -12<= tempG[i] < -8:
			corG[i] = 2  #fdc4e1
		elif      tempG[i] < -12:
			corG[i] = 1  #fee6e6
		else:
			corG[i] = -999.9

		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
		hora.append(d1)

	return(hora, corG, tempG, max)



