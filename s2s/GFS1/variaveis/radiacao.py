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

def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	GFS_rad = GFSfile.variables['dswrfsfc']
	max_i = len(time)
	radG = np.empty((max_i,1))
	diaG_min = np.empty((max_i,1))
	diaG_max = np.full((max_i,1), -999.9)
	corG = np.empty((max_i,1))
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz

	for i in range(0, max_i):
		radG[i] = GFS_rad[i, ixGFS, iyGFS]
		a = int(18)
		b = int(0)
	maxx = max_i // 24
	dia = iz // 24
	data = []
	for i in range(dia, maxx):
		diaG_min[i] = sum(radG[b:a]) / (a-b)
#		izG[i] = b
		b = int(24 + utc0 + (i*24))
		a = int(a + 24)
		if diaG_min[i] < 200:
			corG[i] = 3 #vermelho
		elif diaG_min[i] < 260:
			corG[i] = 2 #amarelo
		else:
			corG[i] = 1 #verde

		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data.append(d1)

	return(data, corG, diaG_min, diaG_max, maxx)

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0):
	time = GFSfile.variables['time']
	GFS_rad = GFSfile.variables['dswrfsfc']
	radG = np.empty((max_i,1))
	corG = np.empty((max_i,1))
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i	
	hora = []

	for i in range(0, max_i):
		radG[i] = GFS_rad[i, ixGFS, iyGFS]

		if radG[i] >= 1100:
			corG[i] = 12
		elif 1000 <= radG[i] < 1100:
			corG[i] = 11
		elif 900 <= radG[i] < 1000:
			corG[i] = 10
		elif 800 <= radG[i] < 900:
			corG[i] = 9
		elif 700 <= radG[i] < 800:
			corG[i] = 8
		elif 600 <= radG[i] < 700:
			corG[i] = 7
		elif 500 <= radG[i] < 600:
			corG[i] = 6
		elif 400 <= radG[i] < 500:
			corG[i] = 5
		elif 300 <= radG[i] < 400:
			corG[i] = 4
		elif 200 <= radG[i] < 300:
			corG[i] = 3
		elif 100 <= radG[i] < 200:
			corG[i] = 2
		elif 0 <= radG[i] < 100:
			corG[i] = 1
		else:
			corG[i] = -999.9
	d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
	hora.append(d1)

	return(hora, corG, radG, max)



