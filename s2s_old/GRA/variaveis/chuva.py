#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

#################################################################################
def gfs(ixGFS, iyGFS, GFSfile, date0):
	GFS_chuva = GFSfile.variables['acpcpsfc']
	time = GFSfile.variables['time']  
	max_i = len(time)

	chuvaG = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	diaG_min = np.full((max_i+1,1),-999.9)

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
	accu = 0
	tota = 0
	index = []
	cor = []
	for i in range(dia, maxx):
		diaG_max[i] = sum(chuvaG[b:a])
		if diaG_max[i] < 0:
			diaG_max[i] = 0	
		accu += diaG_max[i]
		tota += 1
		b = 24 + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(days = i )
		index.append(d1.day) 

		if  diaG_max > 1:
			cor.append('y') = 2 #amarelo
		elif diaG_max > 10:
			cor.append('r') #vermelho
		else :
			cor.append('g') #verde
	lim_y = max(diaG_max) + 1
	index = np.arange(len(maxx))		
	diaG_max[0] =  accu / tota 
	return(diaG_max, index, cor, lim_y)

#################################################################################

def wrf(ixWRF, iyWRF, WRFfile, date0):
	WRF_chuva = WRFfile.variables['RAINC']
	WRF_chuvan = WRFfile.variables['RAINNC']
	time = WRFfile.variables['Times']  
	max_i = len(time)

	chuvaG = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	diaG_min = np.full((max_i+1,1),-999.9)
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz 
	for i in range(0, max_i):
		chuvaG[i] = (WRF_chuva[i, ixWRF, iyWRF] + WRF_chuvan[i, ixWRF, iyWRF])
		if chuvaG[i] < 0.02:
			chuvaG[i] = 0
	maxx = max_i // 24
	dia = iz // 24
	accu = 0
	tota = 0
	index = []
	for i in range(dia, maxx):
		diaG_max[i] = sum(chuvaG[b:a])
		if diaG_max[i] < 0:
			diaG_max[i] = 0	
		accu += diaG_max[i]
		tota += 1
		b = 24 + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(days = i )
		index.append(d1.day) 
		if diaG_max > 1:
			cor.append('y') #amarelo
		elif diaG_max > 10:
			cor.append('r') #vermelho
		else :
			cor.append('g') #verde
	lim_y = max(diaG_max) + 1
	index = np.arange(len(maxx))		
	diaG_max[0] =  accu / tota 

	return(diaG_max, index, cor, lim_y)

#################################################################################

