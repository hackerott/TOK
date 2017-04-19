#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import numpy.core.defchararray as np_f
from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

################################################################################
##Locate the near grid point
def WRF_get(wrf_file, lat0, lon0):
	WRFfile = netCDF4.Dataset(wrf_file, 'r')
	latWRF = WRFfile.variables['XLAT_M']
	lonWRF = WRFfile.variables['XLONG_M']	
	rad_factor = pi/180.0
	latvals = latWRF[::] * rad_factor
	lonvals = lonWRF[::] * rad_factor
	ny ,nx = latvals.shape
	lat0_rad = lat0 * rad_factor
	lon0_rad = lon0 * rad_factor
	clat, clon = cos(latvals), cos(lonvals)
	slat, slon = sin(latvals), sin(lonvals)
	delX = cos(lat0_rad) * cos(lon0_rad) - clat * clon
	delY = cos(lat0_rad) * sin(lon0_rad) - clat * slon
#	delZ = sin(lat0_rad) - slat;
#	dist_sq = delX**2 + delY**2 + delZ**2
	dist_sq = delX**2 + delY**2
	minindex_1d = dist_sq.argmin()
#	iz_min, ix_min, iy_min = np.unravel_index( minindex_1d, latvals.shape)
	ix_min, iy_min = np.unravel_index( minindex_1d, latvals.shape)
	WRFfile.close
	return(ix_min, iy_min)
################################################################################
##Get near lat lon on grid from station location
def STATION_get(lat_lon_file, wrf_file, station):
	raw_stations_name = np.genfromtxt(lat_lon_file, delimiter=", ", skip_header=1, dtype=str)
	raw_stations_data = np.genfromtxt(lat_lon_file, delimiter=", ", skip_header=1)
	station_self	= raw_stations_name[:,0]
	station_self	= np_f.replace(station_self, 'SN', '')
	lon_self	= raw_stations_data[:,1]
	lat_self	= raw_stations_data[:,2]
	for i in range(0, len(station_self)):
		if station == station_self[i]: 
			ix, iy = WRF_get(wrf_file, lat_self[i], lon_self[i])
			break
	return(ix, iy)
################################################################################
##Get grid lat lon for station
def LATLON_get(lat_lon_file, wrf_file, station):
	raw_stations_name = np.genfromtxt(lat_lon_file, delimiter=", ", skip_header=1, dtype=str)
	raw_stations_data = np.genfromtxt(lat_lon_file, delimiter=", ", skip_header=1)
	station_self	= raw_stations_name[:,0]
	station_self	= np_f.replace(station_self, 'SN', '')
	lon_self	= raw_stations_data[:,1]
	lat_self	= raw_stations_data[:,2]
	for i in range(0, len(station_self)):
		if station == station_self[i]: 
			ix, iy = WRF_get(wrf_file, lat_self[i], lon_self[i])
			break
	WRFfile		= netCDF4.Dataset(wrf_file, 'r')
	WRF_lat		= WRFfile.variables['XLAT_M'] 
	WRF_lon		= WRFfile.variables['XLONG_M'] 
	lat = WRF_lat[ix, iy]
	lon = WRF_lon[ix, iy]
	WRFfile.close
	return(lat, lon)
