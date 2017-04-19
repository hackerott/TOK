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

###Umidade
def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	max_i = len(time)
	GFS_q2 = GFSfile.variables['Q2']
	GFS_pres = GFSfile.variables['PSFC']
	GFS_t2 = GFSfile.variables['T2']

	rh2G = np.empty((max_i_GFS,1))
#    tempG = np.empty((max_i_GFS,1))
    
	diaG_min = np.empty((max_i_GFS,1))
	corG = np.empty((max_i_GFS,1))

	for i in range(0, max_i_GFS):
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

	for i in range(0, max_i):
		radG[i] = GFS_rad[i, ixGFS, iyGFS]
		a = int(18)
		b = int(0)
	dia = iz % 24
	data = np.empty((9+1),1)
	for i in range(0, 9):
		i_min = argmin(rh2G[b:a]) 	
		diaG_min[i] = rh2G[i_min+b]	
		izG[i] = b
		b = 24 + utc0 + (i*24)
		a = a + 24
		if diaG_min[i] > 90:
			corG[i] = 2 #amarelo
		elif diaG_min[i] > 80:
			corG[i] = 2 #vermelho
		else :
			corG[i] = 1 #verde
		d1 = date1 + datetime.timedelta(hours = 6 + utc0) + datetime.timedelta(days = i) 
		data[i] = d1.strftime('%A, %d/%m/%Y')
	return(d1, corG, diaG_min, 9)

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
	time = GFSfile.variables['time']
	GFS_q2 = ncfile.variables['Q2']
	GFS_pres = ncfile.variables['PSFC'
	GFS_t2 = ncfile.variables['T2']
	rh2G = np.empty((max_i,1))
	tempG = np.empty((max_i,1))
	corG = np.empty((max_i,1))
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i	
	hora = np.empty((max_i,1))
	for i in range(iz, max_i):
		tempG[i] = GFS_t2[i, ixGFS, iyGFS]
		a5 = 17.2693882 * (tempk[i, ixGFS, iyGFS] - 273.15) / (tempk[i, ixGFS, iyGFS] - 35.86)
		rh2G[i] = 100 * (GFS_q2[i, ixGFS, iyGFS] / ((379.90516 / GFS_pres[i, ixGFS, iyGFS]) * exp(a5)))
		if rh2G[i] > 80:
			cor[i] = 2 #amarelo
		elif rh2G_max[i] > 90:
			cor[i] = 1 #vermelho
		else :
			cor[i] = 1 #verde
	d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
	hora[i] = d1.strftime('%d/%m %Hh')

	return(hora, corG, rh2G, max)

