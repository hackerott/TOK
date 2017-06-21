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
	GFS_ventou = GFSfile.variables['ugrd10m']
	GFS_ventov = GFSfile.variables['vgrd10m']
	time = GFSfile.variables['time']  
	max_i = len(time)

	ventouG  = np.empty((max_i+1,1))
	ventovG  = np.empty((max_i+1,1))
	ventoG   = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	U        = np.full((max_i+1,1),-999.9)
	V        = np.full((max_i+1,1),-999.9)

	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz 
 
	for i in range(0, max_i):

		ventouG[i] = (GFS_ventou[i, ixGFS, iyGFS])
		ventovG[i] = (GFS_ventov[i, ixGFS, iyGFS])
		ventoG[i]  = sqrt((GFS_ventou[i, ixGFS, iyGFS])**2 + GFS_ventov[i, ixGFS, iyGFS])**2)

	maxx = max_i // 24
	dia = iz // 24
	accu = 0
	tota = 0
	index = []
	cor = []
	for i in range(dia, maxx):
		diaG_max[i] = np.mean(ventoG[b:a])
		U[i] = (np.mean(ventouG[b:a]) / (np.mean(ventovG[b:a]) + np.mean(ventouG[b:a]))) * 2
		V[i] = (np.mean(ventovG[b:a]) / (np.mean(ventovG[b:a]) + np.mean(ventouG[b:a]))) * 2
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
#	index = np.arange(len(maxx))		
	diaG_max[0] =  accu / tota 
	return(diaG_max, U, V, index, cor, lim_y)

#################################################################################
#	WRF
def wrf(ixWRF, iyWRF, WRFfile, date0):
	WRF_ventou = WRFfile.variables['U10']
	WRF_ventov = WRFfile.variables['V10']
	time = WRFfile.variables['Times']  
	max_i = len(time)

	ventoG   = np.empty((max_i+1,1))
	ventouG  = np.empty((max_i+1,1))
	ventovG  = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	U        = np.full((max_i+1,1),-999.9)
	V        = np.full((max_i+1,1),-999.9)
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz 
	for i in range(0, max_i):
		ventouG[i] = WRF_ventou[i, ixWRF, iyWRF]
		ventovG[i] = WRF_ventov[i, ixWRF, iyWRF]
		ventoG[i] = sqrt(WRF_ventou[i, ixWRF, iyWRF]**2 + WRF_ventov[i, ixWRF, iyWRF]**2)
		if ventoG[i] < 0.02:
			ventoG[i] = 0
	maxx = max_i // 24
	dia = iz // 24
	accu = 0
	tota = 0
	index = []
	for i in range(dia, maxx):
		diaG_max[i] = np.mean(ventoG[b:a])
		U[i] = (np.mean(ventouG[b:a]) / (np.mean(ventovG[b:a]) + np.mean(ventouG[b:a]))) * 2
		V[i] = (np.mean(ventovG[b:a]) / (np.mean(ventovG[b:a]) + np.mean(ventouG[b:a]))) * 2
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

	return(diaG_max, U, V, index, cor, lim_y)

#################################################################################

