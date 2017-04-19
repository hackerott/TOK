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
#	GFS
def gfs(ixGFS, iyGFS, GFSfile, date0):
	GFS_radiacao = GFSfile.variables['dswrfsfc']
	time = GFSfile.variables['time']  
	max_i = len(time)
	radiacaoG = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	diaG_min = np.full((max_i+1,1),-999.9)
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz 
 
	for i in range(0, max_i):
		radiacaoG[i] = (GFS_radiacao[i, ixGFS, iyGFS])
		if radiacaoG[i] < 0.02:
			radiacaoG[i] = 0
	maxx = max_i // 24
	dia = iz // 24
	accu = 0
	tota = 0
	index = []
	cor = []
	for i in range(dia, maxx):
		diaG_max[i] = sum(radiacaoG[b:a])
		if diaG_max[i] < 0:
			diaG_max[i] = 0	
		accu += diaG_max[i]
		tota += 1
		b = 24 + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(days = i )
		index.append(d1.day) 
		if med > 2000:
			cor.append('y') = 2 #amarelo
		elif med > 1000:
			cor.append('r') #vermelho
		else :
			cor.append('g') #verde
	lim_y = max(diaG_max) + 1
	med = accu / tota
#	index = np.arange(len(maxx))		
	diaG_max[0] = med 

	return(diaG_max, index, cor, lim_y)
#################################################################################
#	WRF
def wrf(ixWRF, iyWRF, WRFfile, date0):
	WRF_radiacao = WRFfile.variables['SWDOWN']
	time = WRFfile.variables['Times']  
	max_i = len(time)

	radiacaoG = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	diaG_min = np.full((max_i+1,1),-999.9)
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz 
	for i in range(0, max_i):
		radiacaoG[i] = WRF_radiacao[i, ixWRF, iyWRF]
		if radiacaoG[i] < 0.02:
			radiacaoG[i] = 0
	maxx = max_i // 24
	dia = iz // 24
	accu = 0
	tota = 0
	index = []
	cor = []
	for i in range(dia, maxx):
		diaG_max[i] = sum(radiacaoG[b:a])
		if diaG_max[i] < 0:
			diaG_max[i] = 0	
		accu += diaG_max[i]
		tota += 1
		b = 24 + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(days = i )
		index.append(d1.day) 
		if  diaG_max[i] > 2000:
			cor.append('y') #amarelo
		elif  diaG_max[i] > 1000:
			cor.append('r') #vermelho
		else :
			cor.append('g') #verde
	lim_y = max(diaG_max) + 1
	med = accu / tota
#	index = np.arange(len(maxx))		
	diaG_max[0] = med 

	return(diaG_max, index, cor, lim_y)
#################################################################################
