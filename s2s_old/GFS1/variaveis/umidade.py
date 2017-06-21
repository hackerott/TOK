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
def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	max_i = len(time)
	GFS_q2 = GFSfile.variables['spfh2m']
	GFS_pres = GFSfile.variables['pressfc']
	GFS_t2 = GFSfile.variables['tmp2m']
	rh2G = np.empty((max_i,1))

    
	diaG_min = np.empty((max_i,1))
	diaG_max = np.full((max_i,1), -999.9)
	corG = np.empty((max_i,1))

	for i in range(0, max_i):
		tempG = GFS_t2[i, ixGFS, iyGFS]
		a5 = 17.2693882 * (tempG - 273.15) / (tempG - 35.86)
		rh2G[i] = 100 * (GFS_q2[i, ixGFS, iyGFS] / ((379.90516 / GFS_pres[i, ixGFS, iyGFS]) * exp(a5)))
	if rh2G[i] < 0:
		rh2G[i] = 0
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz

#	for i in range(0, max_i):
#		radG[i] = GFS_rad[i, ixGFS, iyGFS]
#		a = int(18)
#		b = int(0)
	maxx = max_i // 24
	dia = iz // 24
	data = []
	for i in range(dia, maxx):
		i_min = argmin(rh2G[b:a]) 	
		diaG_min[i] = rh2G[i_min+b]	
#		izG[i] = b
		b = 24 + utc0 + (i*24)
		a = a + 24
		if diaG_min[i] > 90:
			corG[i] = 2 #amarelo
		elif diaG_min[i] > 80:
			corG[i] = 2 #vermelho
		else :
			corG[i] = 1 #verde
		d1 = date0 + datetime.timedelta(hours = 6 + utc0) + datetime.timedelta(days = i) 
		data.append(d1)
	return(data, corG, diaG_min, diaG_max, maxx)

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0):
	time = GFSfile.variables['time']
	max_i = len(time)
	GFS_q2 = GFSfile.variables['spfh2m']
	GFS_pres = GFSfile.variables['pressfc']
	GFS_t2 = GFSfile.variables['tmp2m']
	rh2G = np.empty((max_i,1))
	corG = np.empty((max_i,1))
	max = iz + 24
	hora = []
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i	
	for i in range(iz, max_i):
		tempG[i] = GFS_t2[i, ixGFS, iyGFS]
		a5 = 17.2693882 * (tempk[i, ixGFS, iyGFS] - 273.15) / (tempk[i, ixGFS, iyGFS] - 35.86)
		rh2G_max[i] = 100 * (GFS_q2[i, ixGFS, iyGFS] / ((379.90516 / GFS_pres[i, ixGFS, iyGFS]) * exp(a5)))
		if rh2G_max[i] >= 95:
			cor[i] = 17 #amarelo
		elif 90 <= rh2G_max[i] < 95:
			cor[i] = 16 #vermelho
		elif 85 <= rh2G_max[i] < 90:
			cor[i] = 15
		elif 80 <= rh2G_max[i] < 85:
			cor[i] = 14
		elif 75 <= rh2G_max[i] < 80:
			cor[i] = 13
		elif 70 <= rh2G_max[i] < 75:
			cor[i] = 12
		elif 65 <= rh2G_max[i] < 70:
			cor[i] = 11
		elif 60 <= rh2G_max[i] < 65:
			cor[i] = 10
		elif 55 <= rh2G_max[i] < 60:
			cor[i] = 9
		elif 50 <= rh2G_max[i] < 55:
			cor[i] = 8
		elif 45 <= rh2G_max[i] < 50:
			cor[i] = 7
		elif 40 <= rh2G_max[i] < 45:
			cor[i] = 6
		elif 35 <= rh2G_max[i] < 40:
			cor[i] = 5
		elif 30 <= rh2G_max[i] < 35:
			cor[i] = 4
		elif 25 <= rh2G_max[i] < 30:
			cor[i] = 3
		elif 20 <= rh2G_max[i] < 25:
			cor[i] = 2
		elif rh2G_max[i] < 20:
			cor[i] = 1
		else :
			cor[i] = -999.9
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
		hora.append(d1)

	return(hora, cor, rh2G_max, max)


