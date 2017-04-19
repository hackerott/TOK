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

def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	GFS_chuva = GFSfile.variables['acpcpsfc']
	time = GFSfile.variables['time']  
	max_i = len(time)

	chuvaG = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	diaG_min = np.full((max_i+1,1),-999.9)
	corG = np.empty((max_i+1,1))

	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz 
 
	for i in range(0, max_i):
		chuvaG[i] = (GFS_chuva[i, ixGFS, iyGFS])

		if chuvaG[i] < 0.02:
			chuvaG[i] = 0
	maxx = max_i // 24
	dia = iz // 24
#	data = np.array((maxx+1,1))
	data = [None]*(maxx+1)
	for i in range(dia, maxx):
		diaG_max[i] = sum(chuvaG[b:a])
		if diaG_max[i] < 0:
			diaG_max[i] = 0	
		if diaG_max[i] > 1:
			corG[i] = 2 #amarelo
		elif diaG_max[i] > 10:
			corG[i] = 3 #vermelho
		else :
			corG[i] = 1 #verde
			
		b = 24 + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data[i] = d1

	return(data, corG, diaG_min, diaG_max, maxx)

##		Tabela 

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0):
	time = GFSfile.variables['Times']
	max_i = len(time)
	time_step = 1

	GFS_chuva = ncfile.variables['acpcpsfc']
	chuvaG = [None]*max_i
	corG = [None]*max_i
	
	max = iz + 24
	if  iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = []

for i in range (iz, max):
		chuvaG[i] = GFS_chuva[i, ixGFS, iyGFS]
		if chuvaG[i] > 37:
			corG[i] = 11
		elif 29 <= chuvaG[i] < 37:
			corG[i] = 10
		elif 22 <= chuvaG[i] < 29:
			corG[i] = 9
		elif 16 <= chuvaG[i] < 22:
			corG[i] = 8
		elif 11 <= chuvaG[i] < 16:
			corG[i] = 7
		elif 7 <= chuvaG[i] < 11:
			corG[i] = 6
		elif 4 <= chuvaG[i] < 7:
			corG[i] = 5
		elif 2 <= chuvaG[i] < 4:
			corG[i] = 4
		elif 1 <= chuvaG[i] < 2:
			corG[i] = 3
		elif 0.1 <= chuvaG[i] < 1:
			corG[i] = 2
		elif 0 <= chuvaG[i] < 0.1:
			corG[i] = 1
		else :
			corG[i] = -999.9
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
		hora.append(d1)

	return(hora, corG, chuvaG, max)

