#!/usr/bin/python
# coding: utf-8

import numpy as np
import sys
import datetime

#######################################
import lat_lon

################################################################################
##Creates the array with all data and dates from station files 
def DATA_get(station_file, station, path2, path3):

	raw_data = np.genfromtxt(station_file, delimiter=";",skip_header=500, skip_footer=11)

	station_self	= raw_data[:,0]
	year		= raw_data[:,1]
	month		= raw_data[:,2]
	day		= raw_data[:,3]
	hour		= raw_data[:,4]
	data		= raw_data[:,5]

	lat_raw, lon_raw = lat_lon.LATLON_get(path3, path2, station)
	station 	= int(station)
	out	= []
	date	= []
	lat	= []
	lon	= []
	for i in range(0, len(raw_data)):
		if station_self[i] == station and np.invert(np.isnan(data[i])):
			if data[i] < 0:
				data[i] = 0
			out.append(data[i])
			date_self = '%.0f%.0f%.0f%.0f' % (year[i], month[i], day[i], hour[i])
#			print datetime.datetime.strptime(date_self, '%Y%m%d%H')
			date.append(datetime.datetime.strptime(date_self, '%Y%m%d%H'))			
			lat.append(lat_raw)
			lon.append(lon_raw)
	return(out, date, lat, lon)

################################################################################
## Not used, for interpolation off station data to a grid 
def DATA_plot(out_raw, max_x, max_y):
	station = out_raw[:, 2]
	x	= out_raw[:, 3]
	y	= out_raw[:, 4]
	station_grid = [[np.nan]*max_y]*max_x	
	for i in range(0, len(out_raw)):
		station_grid[x[i]][y[i]] = station[i]
	return(station_grid)
