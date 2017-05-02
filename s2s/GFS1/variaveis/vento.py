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

###wind

def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	GFS_u = GFSfile.variables['ugrd10m']
	GFS_v = GFSfile.variables['vgrd10m']
	max_i = len(time) 	
	r2d = 45.0/np.arctan(1.0)
	windG		= []
	dirG		= []
	colorG		= []
	dayG_max	= []
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
		windG.append(np.sqrt(np.power(up,2) + np.power(vp,2)))
	maxx = max_i // 24
	day = iz // 24
	data = []
	for i in range(day, maxx):
		i_max = np.argmax(windG[b:a]) 	
		dayG_max.append(windG[i_max+b])
		dirG_max.append(dirG[i_max+b])	
		if dayG_max[i] > 8:
			colorG.append(3) #vermelho
		elif dayG_max[i] > 5:
			colorG.append(2) #amarelo
		else:
			colorG.append(1) #verde

		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data.append(d1)
	return(data, colorG, dayG_max, dirG_max, maxx)

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0):
	
	time = GFSfile.variables['time']
	max_i = len(time)
	time_step = 1

	GFS_u = GFSfile.variables['ugrd10m']
	GFS_v = GFSfile.variables['vgrd10m']
	windG = np.empty((max_i,1))
	dirG = np.empty((max_i,1))
	colorG = [None]*max_i
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
		windG[i] = np.sqrt(np.power(up,2) + np.power(vp,2))

	        if windG[i] > 15:
       			colorG[i] = 16 #660a11
       		elif 14 <= windG[i] < 15:
       			colorG[i] = 15 #a01621
		elif 13 <= windG[i] < 14:
			colorG[i] = 14 #c71b2b
		elif 12 <= windG[i] < 13:
			colorG[i] = 13 #d9352f
		elif 11 <= windG[i] < 12:
			colorG[i] = 12 #e75533
		elif 10 <= windG[i] < 11:
			colorG[i] = 11 #f18140
		elif  9 <= windG[i] < 10:
			colorG[i] = 10 #f4b455
		elif  8 <= windG[i] <  9:
			colorG[i] = 9  #f8e76c
		elif  7 <= windG[i] <  8:
			colorG[i] = 8  #b3d260
		elif  6 <= windG[i] <  7:
			colorG[i] = 7  #6fbe55
		elif  5 <= windG[i] <  6:
			colorG[i] = 6  #50aa6e
		elif  4 <= windG[i] <  5:
			colorG[i] = 5  #4f9b9e
		elif  3 <= windG[i] <  4:
			colorG[i] = 4  #5897cc
		elif  2 <= windG[i] <  3:
			colorG[i] = 3  #7ab6de
		elif  1 <= windG[i] <  2:
			colorG[i] = 2  #9dd6f3
		elif  0 <= windG[i] <  1:
			colorG[i]	= 1  #d7effb
		else:
			colorG[i] = -999.9
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6) 
		hora.append(d1)
			
	return(hora, colorG, windG, dirG, max)

