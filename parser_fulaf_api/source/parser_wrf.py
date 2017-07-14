#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

################################################################################
##Creates the acumulated preciptation per location 
def DATA_get(ix, iy, wrf_file, date0, date1):
	WRFfile = netCDF4.Dataset(wrf_file, 'r')
	WRF_rain_ncu, WRF_lats, WRF_lons = _get_rain_WRF(WRFfile)
	date_i, date_f = _get_date_WRF(date0, date1, WRFfile)

	lat = WRF_lats[ix, iy]
	lon = WRF_lons[ix, iy]
	out = WRF_rain_ncu[date_f, ix, iy] - WRF_rain_ncu[date_i, ix, iy]

	return(out, date1, lat, lon)

def _get_date_WRF(date0, date1, WRFfile):
	WRF_ts	= WRFfile.variables['Times']
#	date_i	= WRF_ts.index(date0)
#	date_f	= WRF_ts.index(date1)
	date = []
	for t in WRF_ts:
		t = str(t)
		t = t.replace("'", "").replace(" ", "").replace("\n", "").replace("[", "").replace("]", "")
		t1 = datetime.datetime.strptime(str(t), '%Y-%m-%d_%H:%M:%S')
		date.append(t1)
	date_i	= date.index(date0)
	date_f	= date.index(date1)
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
