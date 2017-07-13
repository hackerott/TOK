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
#	for i in range(inic, iz):
#		if i == 0:
#			rain1.append(wrf[i, ix, iy])
#		else:
#			rain1.append(wrf[i, ix, iy] - wrf[i-1, ix, iy])

#	rain = sum(rain1[0:23])
	# print rain, iz
	rain = wrf[iz, ix, iy] - wrf[inic, ix, iy]
	return(rain)
################################################################################
##
def _get_area_error(wrf, station, jz, iz, ix, iy, search, gaus_test):
	ix_max = wrf.shape[1]
	iy_max = wrf.shape[2]
	ix_min = 0
	iy_min = 0
	a = int(search) + ix
	try:
		max_wrf = max(wrf[iz, ix:a, iy:a])
	except:
		max_wrf = np.amax(wrf[iz, ix:a, iy:a])	
	try:
		max_	= max(station[jz], max_wrf)
	except:
		max_	= station[jz] 
	er = []
	ed = []
	di = []
	if (ix + search) <= ix_max and (ix - search) >= ix_min:
		if (iy + search) <= iy_max and (iy - search) >= iy_min:
			for i in range(int(ix - search), int(ix + search)):
				for j in range(int(iy - search), int(iy + search)):
					rain = _get_accumulated_rain(wrf, iz, i, j)
					error_a = (np.divide(np.absolute(rain - station[jz]), max_)) 
					error_d = np.sqrt(((i-ix)**2 + (j-iy)**2)) / search
					dist = np.sqrt(((100-ix)**2 + (100-iy)**2))
					if np.invert(np.isnan(error_d)): 
						if np.invert(np.isnan(error_a)): 
							er.append(error_a)
							ed.append(error_d)
							di.append(dist)
	
	r = min(er)
	d = ed[np.argmin(er)]
	out = (r + d) / 2 
	rain_ = _get_accumulated_rain(wrf, iz, ix, iy)
	error_a = (np.divide(np.absolute(rain_ - station[jz]), max_))
	if out >= error_a:
		out = error_a
	out = np.subtract(1, out)

	if gaus_test == "True":
		out_2 = "%s; %s; %s; %s; %s; %s; %s;\n" %(ix, iy, rain_, station[jz], np.subtract(1, error_a), out, di[np.argmin(er)])
		return(out, out_2)

	return(out)

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
				erro = _get_area_error(WRF_rain_ncu, station, j, i, ix, iy, search, "False")
#				error.append(min(erro))
				error.append(erro)	
	return(error)

def DATA_get_gaus(rain_c, wrf_file, ix, iy, station, date0, date1, date_station):

	date1 =  datetime.datetime.strptime(date1, '%Y%m%d%H')

	WRFfile = netCDF4.Dataset(wrf_file, 'r')

#	WRF_rain_ncu	= WRFfile.variables['RAINNC']
	time		= WRFfile.variables['Times']  
	resolution	= getattr(WRFfile, 'DX')

	max_i	= len(time)
	max_s	= len(station)
	search	= 12000//resolution
	error = []
	out_f = []	
	for j in range(0, max_s):
		for i in range(0, max_i):
			d1 = datetime.datetime.strptime(str(date0), '%Y%m%d%H') + datetime.timedelta(hours= i)
			d2 = date_station[j]
			if d1 == date1 and d2 == date1:
				erro, out = _get_area_error(rain_c, station, j, i, ix, iy, search, "True")
#				error.append(min(erro))
				error.append(erro)	
	 			out_f.append(out)
	return(error, out_f)
