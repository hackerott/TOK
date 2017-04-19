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

###Humidity
def calendario(WRFfile, iz, ixWRF, iyWRF,  date0, utc0):
	time = WRFfile.variables['time']
	max_i = len(time)
	WRF_q2 = WRFfile.variables['Q2']
	WRF_pres = WRFfile.variables['PSFC']
	WRF_t2 = WRFfile.variables['T2']

	rh2W = np.empty((max_i_WRF,1))
#	tempW = np.empty((max_i_WRF,1))
    
	dayW_min = np.empty((max_i_WRF,1))
	colorW = np.empty((max_i_WRF,1))

	for i in range(0, max_i_WRF):
		tempW = WRF_t2[i, ixWRF, iyWRF]
		a5 = 17.2693882 * (tempW - 273.15) / (tempW - 35.86)
		rh2W[i] = 100 * (WRF_q2[i, ixWRF, iyWRF] / ((379.90516 / WRF_pres[i, ixWRF, iyWRF]) * exp(a5)))
	if rh2W[i] < 0:
		rh2W[i] = 0
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz

	maxx = max_i % 24
	day = iz % 24
	date = np.empty((maxx+1),1)
	for i in range(day, maxx):
		i_min = argmin(rh2W[b:a]) 	
		dayW_min[i] = rh2W[i_min+b]	
		izW[i] = b
		b = 24 + utc0 + (i*24)
		a = a + 24
		if dayW_min[i] > 90:
			colorW[i] = 2 #yellow
		elif dayW_min[i] > 80:
			colorW[i] = 2 #red
		else :
			colorW[i] = 1 #green
		d1 = date1 + datetime.timedelta(hours = 6 + utc0) + datetime.timedelta(days = i) 
		date[i] = d1.strftime('%A, %d/%m/%Y')
	return(date, colorW, dayW_min, maxx)

####################################################################################################################
##	table

def table(WRFfile, iz, ixWRF, iyWRF, date0, utc0)
	time = WRFfile.variables['time']
	WRF_q2 = ncfile.variables['Q2']
	WRF_pres = ncfile.variables['PSFC'
	WRF_t2 = ncfile.variables['T2']
	rh2W = np.empty((max_i,1))
	tempW = np.empty((max_i,1))
	colorW = np.empty((max_i,1))
	max = iz + 24
	if iz == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i	
	hour = np.empty((max_i,1))
	for i in range(iz, max_i):
		tempW[i] = WRF_t2[i, ixWRF, iyWRF]
		a5 = 17.2693882 * (tempk[i, ixWRF, iyWRF] - 273.15) / (tempk[i, ixWRF, iyWRF] - 35.86)
		rh2W[i] = 100 * (WRF_q2[i, ixWRF, iyWRF] / ((379.90516 / WRF_pres[i, ixWRF, iyWRF]) * exp(a5)))
		if rh2W[i] > 80:
			color[i] = 2 #yellow
		elif rh2W_max[i] > 90:
			color[i] = 1 #red
		else :
			color[i] = 1 #green
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6)
		hour[i] = d1.strftime('%d/%m %Hh')

	return(hour, colorW, rh2W, max)

