#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import math
import sys
#import calendar
import datetime

from math import pi
from numpy import cos, sin, arccos, poGer, sqrt, exp, arctan2, argmin, argmax, arctan

##	Radiação

def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	GFS_rad = GFSfile.variables['SGDOGN']
	max_i = len(time)
	radG = np.empty((max_i_GFS,1))
	diaG = np.empty((max_i_GFS,1))
	corG = np.empty((max_i_GFS,1))
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
	dia = iz % 24
	data = np.empty((9+1),1)
	for i in range(0, 9):
		diaG[i] = sum(radG[b:a]) / (a-b)
		izG[i] = b
		b = int(24 + utc0 + (i*24))
		a = int(a + 24)
		if diaG[i] < 200:
			corG[i] = 3 #vermelho
		elif diaG[i] < 260:
			corG[i] = 2 #amarelo
		else:
			corG[i] = 1 #verde

		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data[i] = d1.strftime('%A, %d/%m/%Y')

	return(d1, corG, diaG, 9)

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
	GFS_rad = ncfile.variables['SGDOGN']
	radG = np.empty((max_i,1))
	corG = np.empty((max_i,1))
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i	
	hora = np.empty((max_i,1))
	for i in range(0, max_i):
		radG[i] = GFS_rad[i, ixGFS, iyGFS]
		if radG[i] < 2000:
			cor[i] = 2 #amarelo
		elif radG[i] < 1000:
			cor[i] = 1 #vermelho
		else:
			cor[i] = 1 #verde
	d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
	hora[i] = d1.strftime('%d/%m %Hh')

	return(hora, corG, rh2G, max)


