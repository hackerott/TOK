#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

################################################################################
##Creates the acumulated preciptation per location 
def DATA_get(wrf_file, ix, iy, date0, date1):
	date1 = datetime.datetime.strptime(str(date1), '%Y%m%d%H')
	WRFfile = netCDF4.Dataset(wrf_file, 'r')
	WRF_rain_ncu	= WRFfile.variables['RAINNC']
	time		= WRFfile.variables['Times']  
	WRF_lat		= WRFfile.variables['XLAT_M'] 
	WRF_lon		= WRFfile.variables['XLONG_M'] 
	max_i	= len(time)
	rain	= []		
	date	= []	
	for i in range(0, max_i):
		if i == 0:
			rain1 = WRF_rain_ncu[i, ix, iy]
#			rain2 = WRF_rain_ncu[i, ix+1, iy]
#			rain3 = WRF_rain_ncu[i, ix+1, iy+1]
#			rain4 = WRF_rain_ncu[i, ix, iy+1]

		else:
			rain1 = WRF_rain_ncu[i, ix, iy]		- WRF_rain_ncu[i - 1, ix, iy]
#			rain2 = WRF_rain_ncu[i, ix+1, iy]	- WRF_rain_ncu[i - 1, ix+1, iy]
#			rain3 = WRF_rain_ncu[i, ix+1, iy+1]	- WRF_rain_ncu[i - 1, ix+1, iy+1]
#			rain4 = WRF_rain_ncu[i, ix, iy+1]	- WRF_rain_ncu[i - 1, ix, iy+1]
#		rain_i = (rain1+rain2+rain3+rain4)/4
#		rain.append(rain_i)
		rain.append(rain1)
		d1 = datetime.datetime.strptime(str(date0), '%Y%m%d%H') + datetime.timedelta(hours= i)
		date.append(d1)

	
	max_j	= (max_i // 24) + 1
	out	= []
	date_f	= []
	lat	= []
	lon	= []
	a = 24
	b = 0

	for j in range(0, max_j):
#		if a > max_i:
#			break
		if date[b] == date1:
			out_self = sum(rain[b:a])
			if out_self < 0:
				out_self = 0
			out.append(out_self)
			date_f.append(date[b])
			lat.append(WRF_lat[ix, iy])
			lon.append(WRF_lon[ix, iy])
		b = a
		a += 24
	return(out, date_f, lat, lon)

################################################################################
##Not used, to create a uniform grid with accumulated precipitation 
def DATA_plot(wrf_file):
 	WRFfile = netCDF4.Dataset(wrf_file, 'r')
	WRF_rain_ncu	= WRFfile.variables['RAINNC']
	time		= WRFfile.variables['Times']  
	max_i	= len(time)//24
	a = 24
	b = 0
	max_xy = np.shape(WRF_rain_ncu)
	rain_grid = [[0]*max_xy[2]]*max_xy[1]
	for i in range(0, max_i):
		for j in range(0, max_xy[1]):
			for k in range(0, max_xy[2]): 
				rain_grid[j][k] = sum(WRF_rain_ncu[b:a, j, k]) #need a proper fix
		b = a
		a += 24
		if a > len(time):
			break		
	latWRF = WRFfile.variables['XLAT_M']
	lonWRF = WRFfile.variables['XLONG_M']
	return(rain_grid, max_xy[1], max_xy[2])
