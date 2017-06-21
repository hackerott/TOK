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
	GFS_temp = GFSfile.variables['tmp2m']
	GFS_q2   = GFSfile.variables['spfh2m']
	GFS_pres = GFSfile.variables['pressfc']
	time = GFSfile.variables['time']  
	max_i = len(time)
	umidadeG = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	diaG_min = np.full((max_i+1,1),-999.9)
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz 
 
	for i in range(0, max_i):

		umidadeG[i] = 100 * (GFS_q2[i, ixGFS, iyGFS] / ((379.90516 / GFS_pres[i, ixGFS, iyGFS]) * exp(17.2693882 * (GFS_temp[i, ixGFS, iyGFS] - 273.15) / (GFS_temp[i, ixGFS, iyGFS] - 35.86))


	maxx = max_i // 24
	dia = iz // 24
	accu = 0
	tota = 0
	index = []
	cor = []
	for i in range(dia, maxx):
		diaG_max[i] = max(umidadeG[b:a])
		diaG_mim[i] = min(umidadeG[b:a])
		accu += diaG_max[i] + diaG_min[i]
		tota += 2
		b = 24 + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(days = i )
		index.append(d1.day) 
	lim_y = max(diaG_max) + 1
	med = accu / tota
#	index = np.arange(len(maxx))		
	diaG_max[0] = med 

	return(diaG_max, diaG_min, index, cor, lim_y)
#################################################################################
#	WRF
def wrf(ixWRF, iyWRF, WRFfile, date0):
	WRF_temp = WRFfile.variables['T2']
	WRF_q2   = WRFfile.variables['Q2']
	WRF_pres = WRFfile.variables['PSFC']
	time = WRFfile.variables['Times']  
	max_i = len(time)
	umidadeG = np.empty((max_i+1,1))
	diaG_max = np.empty((max_i+1,1))
	diaG_min = np.full((max_i+1,1),-999.9)
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz 
	for i in range(0, max_i):
		umidadeG[i] = 100 * (WRF_q2[i, ixWRF, iyWRF] / ((379.90516 / WRF_pres[i, ixWRF, iyWRF]) * exp(17.2693882 * (WRF_temp[i, ixWRF, iyWRF] - 273.15) / (WRF_temp[i, ixWRF, iyWRF] - 35.86))
	maxx = max_i // 24
	dia = iz // 24
	accu = 0
	tota = 0
	index = []
	cor = []
	for i in range(dia, maxx):
		diaG_max[i] = max(umidadeG[b:a])
		diaG_min[i] = min(umidadeG[b:a])
		accu += diaG_max[i] + diaG_min[i]
		tota += 2
		b = 24 + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(days = i )
		index.append(d1.day) 
	lim_y = max(diaG_max) + 1
	med = accu / tota
#	index = np.arange(len(maxx))		
	diaG_max[0] = med 

	return(diaG_max, index, cor, lim_y)
#################################################################################
