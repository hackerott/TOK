#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

################################################################################
##Creates the acumulated preciptation per location 
def DATA_get(ix, iy, WRF_rain_ncu, WRF_lat, WRF_lon, date_i, date_f):
	lat = WRF_lat[ix, iy]
	lon = WRF_lon[ix, iy]
	out = WRF_rain_ncu[date_f, ix, iy] - WRF_rain_ncu[date_i, ix, iy]

	return(out, date_f, lat, lon)

def _get_date_WRF(date0, date1, WRFfile):
	date1	= datetime.datetime.strptime(str(date1), '%Y%m%d%H')
	date0	= datetime.datetime.strptime(str(date0), '%Y%m%d%H')
	WRF_ts	= WRFfile.variables['Times']
	date_i	= WRF_ts.index(date0)
	date_f	= WRF_ts.index(date1)

	return(date_i, date_f)

def _get_rain_WRF(WRFfile):
	WRF_rain_ncu	= WRFfile.variables['RAINNC']
	WRF_lat		= WRFfile.variables['XLAT_M'] 
	WRF_lon		= WRFfile.variables['XLONG_M'] 

	return(WRF_rain_ncu, WRF_lat, WRF_lon)

################################################################################
##Not used, to create a uniform grid with accumulated precipitation 
def DATA_plot(wrf_file):
 	WRFfile = netCDF4.Dataset(wrf_file, 'r')
	WRF_rain_ncu	= WRFfile.variables['RAINNC']
  
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
