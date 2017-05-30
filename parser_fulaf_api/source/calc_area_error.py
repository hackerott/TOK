#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

################################################################################
#def _get_accumulated_rain(wrf, iz, ix, iy, d1, d2):
#	a = 0
#	while d1 <= d2:
#		d1 = d1 + datetime.timedelta(hours= 1)
#		a += 1 
#	days = a//24
#	if days == 0:
#		inic = days
#	else:
#		inic = (days * 24) - 24
#	rain1 = []
#	for i in range(inic, inic+24):
def _get_accumulated_rain(wrf, iz, ix, iy):
	inic = iz-24
	if inic < 0:
		inic = 0
	rain1 = []
	for i in range(inic, iz):
		if i = 0:
			rain1.append(wrf[i, ix, iy])
		else:
			rain1.append(wrf[i, ix, iy] - wrf[i-1, ix, iy])

	rain = sum(rain1[0:23])

	return(rain)
################################################################################
#def _get_area_error(wrf, station, jz, iz, ix, iy, search, d1, d2):
def _get_area_error(wrf, station, jz, iz, ix, iy, search):
	ix_max = wrf.shape[1]
	iy_max = wrf.shape[2]
	ix_min = 0
	iy_min = 0

	max_sta = max(station)
	max_wrf = max(wrf[iz, ix, iy])
	max_	= max(max_sta, max_wrf)

	if (ix + search) <= ix_max and (ix - search) >= ix_min:
		if (iy + search) <= iy_max and (iy - search) >= iy_min:
			for i in range((ix - search), (ix + search)):
				for j in range((iy - search), (iy + search)):
#					rain = _get_accumulated_rain(wrf, iz, i, j, d1, d2)
					rain = _get_accumulated_rain(wrf, iz, i, j)
					error_a = (np.divide(np.absolute(rain - station[jz]), max_)) 
					error_d = np.sqrt(((i-ix)**2 + (j-iy)**2)) / search
					error.append(0.5*error_a + 0.5*error_d)
#	else:
#		if ix + search <= ix_max and ix - search >= ix_min:
#			if iy + search <= iy_max and iy - search >= iy_min:
#				for i in range((ix - search), (ix + search)):
#					for j in range((iy - search), (iy + search)):
#						error_a = (np.divide(np.absolute((wrf[iz, i, j] - wrf[iz-1, i, j])- station[jz]), max_)) 
#						error_d = np.sqrt(((i-ix)**2 + (j-iy)**2)) / search
#						error.append(0.5*error_a + 0.5*error_d)
	
	return(error)


################################################################################
def DATA_get(wrf_file, ix, iy, station, date0, date1, date_station):

	date1 =  datetime.datetime.strptime(date1, '%Y%m%d%H')

	WRFfile = netCDF4.Dataset(wrf_file, 'r')

	WRF_rain_ncu	= WRFfile.variables['RAINNC']
	time		= WRFfile.variables['Times']  
#	WRF_lat		= WRFfile.variables['XLAT_M'] 
#	WRF_lon		= WRFfile.variables['XLONG_M'] 
	resolution	= getattr(WRFfile, 'DX')

	max_i	= len(time)
	max_s	= len(station)
	search	= resolution//12000
	rain	= []		
	for j in range(0, max_i):
		for i in range(0, max_s):
			d1 = datetime.datetime.strptime(str(date0), '%Y%m%d%H') + datetime.timedelta(hours= i)
			d2 = date_station[j]
			if d1 == date1 and d2 == date1:
#				error_ = _get_area_error(wrf, station, j, i, ix, iy, search, date0, d2)
				error_ = _get_area_error(wrf, station, j, i, ix, iy, search)
				error.append(min(error_))


	max_j	= max_i // 24
	a = 24
	b = 0
	for i in range(0, max_j):
		if  a >= max_i:
			break
		error_final.append(np.mean(error[b,a]))  
		b = a
		a += 24

	return(error_final)


		





