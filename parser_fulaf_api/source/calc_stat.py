#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import sys
import datetime

################################################################################
## Calculate RMSE
def get_RMSE(station, model):
	rmse = []
	for i in range( 0, len(model)):
		rmse.append(np.sqrt((model[i] - station[i])**2))
	rmse = np.mean(rmse)
	return(rmse)

################################################################################
## BIAS
def get_BIAS(station, model):
	bias = []
	for i in range( 0, len(model)):
		bias.append(model[i] - station[i])
	bias = np.mean(bias)
	return(bias)

################################################################################
## AREA ERROR
def get_AREA(data):
#	area = []
#	for i in range( 0, len(data)):
#		area.append(min(data[i]))
	area = np.nanmean(data)
	return(area)

################################################################################
## Organize the data arrays
def ARRAY_split(variable):
	var = []
	for i in range(0, len(variable)):
		a = np.array(variable[i])
		b = variable[i]
		if a.size > 1:
			for j in range(0, len(a)):
				var.append(b[j])
		else:
			var.append(a)
#		print var[i]
	return(var)

################################################################################
## Organize the data by date and location before running statiscs
def DATA_get(data_wrf, data_station, date_wrf, date_station, lat_s, lon_s, lat_w, lon_w, date_tgt, ampl_error):
	max_w = len(data_wrf)
	max_s = len(data_station)
	max_i = min(max_w, max_s)
	raw_date	= []
	raw_wrf		= []
	raw_station	= []
	raw_lat		= []
	raw_lon		= []
	raw_err		= []
	print "Syncing locations..."
	for j in range(0, max_w):
		for i in range(0, max_s):
			if np.invert(np.isnan(data_wrf[j])): 
				if np.invert(np.isnan(data_station[i])): 
					if np.invert(np.isnan(ampl_error[i])): 
						if date_station[i] == date_wrf[j]:
	 						if lat_s[i] == lat_w[j] and lon_s[i] == lon_w[j]:
								raw_station.append(data_station[i])
								raw_date.append(date_station[i])
								raw_wrf.append(data_wrf[j])
								raw_lat.append(lat_w[j])
								raw_lon.append(lon_w[j])
								raw_err.append(ampl_error[i])
#							print raw_station[-1], raw_wrf[-1] 
	max_r	= len(raw_wrf)
	rmse	= []
	bias	= []
	out_d 	= []
	wrf	= []
	sta	= []
	lat	= [] 
	lon	= []
	err	= []

#	good	= []
	print "Syncing dates..."
	date_tgt =  datetime.datetime.strptime(date_tgt, '%Y%m%d%H')
	for i in range(0, max_r):
		if raw_date[i] == date_tgt:
			sta.append(raw_station[i])
			wrf.append(raw_wrf[i])
			lat.append(raw_lat[i])
			lon.append(raw_lon[i])
			err.append(raw_err[i])
			out_d.append('%s,%s,%s,%s,%s' %(raw_lat[i], raw_lon[i], raw_wrf[i], raw_station[i], raw_err[i]))
#			print wrf[-1], sta[-1]
#			if rmse[i]/raw_station[i] < 0.2:
#				good.append(1)	
#			else:
#				good.append(0)

## Statistics
	print "Preparing results..."
#	out_d		= np.unique(out_d)
	std_station	= np.std(raw_station)
	std_wrf		= np.std(raw_wrf)
	# pearsoncor	= np.corrcoef(raw_station, raw_wrf)
	# R		= pearsoncor[0]
	R = [np.nan, 0]
	mean_station	= np.mean(raw_station)
	mean_wrf	= np.mean(raw_wrf)
	rmse		= get_RMSE(raw_station, raw_wrf)
	bias		= get_BIAS(raw_station, raw_wrf)
	area_error	= get_AREA(err)

	out 		= '%s, %s, %s, %s, %s, %s, %s, %s'  % (std_wrf, mean_wrf, std_station, mean_station, R[0], rmse, bias, area_error) #line to be printed
	return(out, out_d, sta, wrf, lat, lon, err)

################################################################################
## Parallel pre processing
def DATA_get_paralel(data_out, date_tgt):
	data_pd		= pd.DataFrame(data_out)
	data_np		= np.array(data_pd.values)

	data_station	= ARRAY_split(data_np[:, 0])
	data_wrf	= ARRAY_split(data_np[:, 1])
#	for i in range(0, len(data_wrf)):
#		print data_wrf[i]
	date_station	= ARRAY_split(data_np[:, 2])
	date_wrf	= ARRAY_split(data_np[:, 3])
	lat_wrf 	= ARRAY_split(data_np[:, 4])
	lon_wrf 	= ARRAY_split(data_np[:, 5])
	lat_station 	= ARRAY_split(data_np[:, 6])
	lon_station 	= ARRAY_split(data_np[:, 7])
	ampl_error	= ARRAY_split(data_np[:, 8])
	ampl_error	= ARRAY_split(ampl_error)

	out, out_raw, raw_station, raw_wrf, raw_lat, raw_lon, raw_area = DATA_get(data_wrf, data_station, date_wrf, date_station, lat_station, lon_station, lat_wrf, lon_wrf, date_tgt, ampl_error)
	return(out, out_raw, raw_station, raw_wrf, raw_lat, raw_lon, raw_area)
