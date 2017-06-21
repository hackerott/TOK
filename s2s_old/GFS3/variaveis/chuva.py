#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, poGer, sqrt, exp, arctan2, argmin, argmax, arctan

######Chuva

##		Calendario

def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	GFS_chuva_cu = GFSfile.variables['RAINC']
	GFS_chuva_ncu = GFSfile.variables['RAINNC']
	time = GFSfile.variables['time']  
	max_i = len(time)

	chuvaG = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	corG = np.empty((max_i+1,1))

	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz
 
	for i in range(0, max_i):
		chuvaG[i] = (GFS_chuva_cu[i, ixGFS, iyGFS] +  GFS_chuva_ncu[i, ixGFS, iyGFS]) - (GFS_chuva_cu[i - 1, ixGFS, iyGFS] + GFS_chuva_ncu[i - 1, ixGFS, iyGFS])

		if chuvaG[i] < 0.02:
			chuvaG[i] = 0
	for i in range(0, 9):
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
		data[i] = d1.strftime('%A, %d/%m/%Y')

	return(d1, corG, diaG_max, 9)

##		Tabela 

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
	time = GFSfile.variables['Times']
	max_i = len(time)
	time_step = 1

	GFS_chuva_cu = ncfile.variables['RAINC']
	GFS_chuva_ncu = ncfile.variables['RAINNC']
	chuvaG = [None]*max_i
	corG = [None]*max_i
	
	max = iz + 24
	if  iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = np.empty((max_i,1))
	for i in range (iz, max):
		chuvaG[i] = (GFS_chuva_cu[i, ixGFS, iyGFS] +  GFS_chuva_ncu[i, ixGFS, iyGFS]) - (GFS_chuva_cu[i - 1, ixGFS, iyGFS] + GFS_chuva_ncu[i - 1, ixGFS, iyGFS])
		if chuvaG[i] > 10:
			corG[i] = "RED" #amarelo
		elif chuvaG[i] > 0.1:
			corG[i] = "YELLOW"#vermelho
		else :
			corG[i] = "GREEN" #verde
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
		hora[i] = d1.strftime('%d/%m %Hh')

	return(hora, corG, chuvaG, max)

