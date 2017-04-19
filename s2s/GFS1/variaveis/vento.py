#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import math
import sys
import calendar
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

###Vento

def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	GFS_u = GFSfile.variables['ugrd10m']
	GFS_v = GFSfile.variables['vgrd10m']
	max_i = len(time) 	
	r2d = 45.0/np.arctan(1.0)
	ventoG		= []
	dirG		= []
	corG		= []
	diaG_max	= []
	dirG_max	= []
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz
	for i in range(0, max_i):
		vp = GFS_v[i, ixGFS, iyGFS]
		up = GFS_u[i, ixGFS, iyGFS]
		dirG.append(np.arctan2(up, vp) * r2d + 180)
		ventoG.append(np.sqrt(np.power(up,2) + np.power(vp,2)))
	maxx = max_i // 24
	dia = iz // 24
	data = []
	for i in range(dia, maxx):
		i_max = np.argmax(ventoG[b:a]) 	
		diaG_max.append(ventoG[i_max+b])
		dirG_max.append(dirG[i_max+b])	
		if diaG_max[i] > 8:
			corG.append(3) #vermelho
		elif diaG_max[i] > 5:
			corG.append(2) #amarelo
		else:
			corG.append(1) #verde

		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data.append(d1)
	return(data, corG, diaG_max, dirG_max, maxx)

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0):
	
	time = GFSfile.variables['time']
	max_i = len(time)
	time_step = 1

	GFS_u = GFSfile.variables['ugrd10m']
	GFS_v = GFSfile.variables['vgrd10m']
	ventoG = np.empty((max_i,1))
	dirG = np.empty((max_i,1))
	corG = [None]*max_i
	r2d = 45.0/np.arctan(1.0)
	z = iz
	max = z + 24
	if z == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = []
	for i in range (z, max):
		vp = GFS_v[i, ixGFS, iyGFS]
		up = GFS_u[i, ixGFS, iyGFS]
		dirG[i] = np.arctan2(up, vp) * r2d + 180
		ventoG[i] = np.sqrt(np.power(up,2) + np.power(vp,2))

	        if ventoG[i] > 15:
       			corG[i] = 16 #660a11
       		elif 14 <= ventoG[i] < 15:
       			corG[i] = 15 #a01621
		elif 13 <= ventoG[i] < 14:
			corG[i] = 14 #c71b2b
		elif 12 <= ventoG[i] < 13:
			corG[i] = 13 #d9352f
		elif 11 <= ventoG[i] < 12:
			corG[i] = 12 #e75533
		elif 10 <= ventoG[i] < 11:
			corG[i] = 11 #f18140
		elif  9 <= ventoG[i] < 10:
			corG[i] = 10 #f4b455
		elif  8 <= ventoG[i] <  9:
			corG[i] = 9  #f8e76c
		elif  7 <= ventoG[i] <  8:
			corG[i] = 8  #b3d260
		elif  6 <= ventoG[i] <  7:
			corG[i] = 7  #6fbe55
		elif  5 <= ventoG[i] <  6:
			corG[i] = 6  #50aa6e
		elif  4 <= ventoG[i] <  5:
			corG[i] = 5  #4f9b9e
		elif  3 <= ventoG[i] <  4:
			corG[i] = 4  #5897cc
		elif  2 <= ventoG[i] <  3:
			corG[i] = 3  #7ab6de
		elif  1 <= ventoG[i] <  2:
			corG[i] = 2  #9dd6f3
		elif  0 <= ventoG[i] <  1:
			corG[i]	= 1  #d7effb
		else:
			corG[i] = -999.9
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6) 
		hora.append(d1)
			
	return(hora, corG, ventoG, dirG, max)

