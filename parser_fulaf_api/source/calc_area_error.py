#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

################################################################################
##
def _get_accumulated_rain(wrf, iz, ix, iy):
	inic = iz-24
	if inic < 0:
		inic = 0
	rain1 = []
	for i in range(inic, iz):
		if i == 0:
			rain1.append(wrf[i, ix, iy])
		else:
			rain1.append(wrf[i, ix, iy] - wrf[i-1, ix, iy])

	rain = sum(rain1[0:23])

	return(rain)
################################################################################
##
def _get_area_error(wrf, station, jz, iz, ix, iy, search):
	ix_max = wrf.shape[1]
	iy_max = wrf.shape[2]
	ix_min = 0
	iy_min = 0

	max_sta = max(station)
	max_wrf = max(wrf[:, ix, iy])
	max_	= max(max_sta, max_wrf)
	error = []	
	if (ix + search) <= ix_max and (ix - search) >= ix_min:
		if (iy + search) <= iy_max and (iy - search) >= iy_min:
			for i in range(int(ix - search), int(ix + search)):
				for j in range(int(iy - search), int(iy + search)):
					rain = _get_accumulated_rain(wrf, iz, i, j)
					error_a = (np.divide(np.absolute(rain - station[jz]), max_)) 
					error_d = np.sqrt(((i-ix)**2 + (j-iy)**2)) / search
					error.append(0.5*error_a + 0.5*error_d)
#	print error
	return(error)

################################################################################
##
def DATA_get(wrf_file, ix, iy, station, date0, date1, date_station):

	date1 =  datetime.datetime.strptime(date1, '%Y%m%d%H')

	WRFfile = netCDF4.Dataset(wrf_file, 'r')

	WRF_rain_ncu	= WRFfile.variables['RAINNC']
	time		= WRFfile.variables['Times']  
	resolution	= getattr(WRFfile, 'DX')

	max_i	= len(time)
	max_s	= len(station)
	search	= 12000//resolution
	error = []	
	for j in range(0, max_s):
		for i in range(0, max_i):
			d1 = datetime.datetime.strptime(str(date0), '%Y%m%d%H') + datetime.timedelta(hours= i)
			d2 = date_station[j]
			if d1 == date1 and d2 == date1:
				erro = _get_area_error(WRF_rain_ncu, station, j, i, ix, iy, search)
				error.append(min(erro))

	return(error)
