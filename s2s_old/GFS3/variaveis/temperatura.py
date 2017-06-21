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

###Temperatura

def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	GFS_t2 = GFSfile.variables['T2']
	max_i = len(time)
 	tempG = np.empty((max_i,1))
	diaG_max = np.empty((max_i,1))
	diaG_min = np.empty((max_i,1))
	corG = np.empty((max_i,1))
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz
	for i in range(0, max_i):
		tempG[i] = GFS_t2[i, ixGFS, iyGFS] - 273.15
	dia = iz % 24
	data = np.empty((9+1),1)
	for i in range(0, 9):
		i_min = argmin(tempG[b:a]) 	
		diaG_min[i] = tempG[i_min+b]	
		i_max = argmax(tempG[b:a]) 	
		diaG_max[i] = tempG[i_max+b]	
		izG[i] = b
		if diaG_max[i] > 30:
			corG[i] = 3 #vermelho
		elif diaG_max[i] < 23:
			corG[i] = 1 #verde
		else :
			corG[i] = 2 #amarelo
		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data[i] = d1.strftime('%A, %d/%m/%Y')


	return(d1, corG, diaG_min, diaG_max, 9) 

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
	time = GFSfile.variables['time']
	GFS_t2 = GFSfile.variables['T2']
	max_i = len(time)
	tempG = np.empty((max_i,1))
	corG = [None]*max_i
	
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = np.empty((max_i,1))
	for i in range (iz, max):
		tempG[i] = GFS_t2[i, ixGFS, iyGFS] - 273.15
		if tempG[i] > 30:
			corG[i] = "RED"
		elif tempG[i] < 23:
			corG[i] = "GREEN" #verde
		else:
			corG[i] = "YELLOG" #amarelo

	d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
	hora[i] = d1.strftime('%d/%m %Hh')

	return(hora, corG, tempG, max)



