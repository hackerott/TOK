#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import sys
import datetime
import netCDF4
import numpy.core.defchararray as np_f
import multiprocessing
from joblib import Parallel, delayed

#######################################
import parser_station
import parser_wrf
import parser_gaus
import lat_lon
import calc_stat
import output
import plot_map
import calc_area_error

#######################################
# Terminal imputs
path1 = (sys.argv[1]) #station_file
path2 = (sys.argv[2]) #wrf_file
path3 = (sys.argv[3]) #lat_lon_file
path4 = (sys.argv[4]) #output_path
date_start	= (sys.argv[5]) #model initial date
date_tgt	= (sys.argv[6]) #analises date
gaus_test	= (sys.argv[7]) #True or False to execute the tes with gaussian output from forecast
#######################################
# File read
raw_stations_name = np.genfromtxt(path3, delimiter= ", " ,skip_header=1, dtype=str)
raw_stations_data = np.genfromtxt(path3, delimiter=",",skip_header=1)
station_self	= raw_stations_name[:,0]
station_self	= np_f.replace(station_self, 'SN', '')
lon_self	= raw_stations_data[:,1]
lat_self	= raw_stations_data[:,2]
date0 = datetime.datetime.strptime(str(date_start), '%Y%m%d%H')
date1 = datetime.datetime.strptime(str(date_tgt), '%Y%m%d%H')
#######################################
# Time estimation and max tread count
#run_time, treads = output.TIME_out(path2, station_self)
mult = multiprocessing.cpu_count()
treads = len(station_self)
if treads >= mult * 2:
	treads = mult * 2
print "#######################################"
#print "\nexpected runtime: %.0f minutes %.0f seconds\n" % (run_time//60, (run_time%60))
print "\nRunning on %.0i treads\n" % (treads)
print "#######################################"
data_wrf	= []
date_wrf	= []
data_station	= []
date_station	= []
out		= []
################################################################################
## Call other func to obtain data per station
def DATA_get(station, gaus_test, header):
	if gaus_test == "False":
		# print "#####\nFALSE\n#####"
		data_station, date_station, lat_station, lon_station = parser_station.DATA_get(path1, station, path2, path3, date_tgt, header)
		if data_station:
			ix, iy = lat_lon.STATION_get(path3, path2, station)
			data_wrf, date_wrf, lat_wrf, lon_wrf = parser_wrf.DATA_get(ix, iy, path2, date0, date1)
			output.RAW_out(path4, station, date_tgt, date_wrf, data_station, data_wrf)
			ampl_error = calc_area_error.DATA_get(path2, ix, iy,  data_station, date_start, date_tgt, date_station)
			return(data_station, data_wrf, date_station, date_wrf, lat_wrf, lon_wrf, lat_station, lon_station, ampl_error)
		else:
			return(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan)	

	else:
		# print "#####\nTRUE\n#####"
		data_station, date_station, lat_station, lon_station = parser_station.DATA_get(STATIONfile, station, path2, path3, date_tgt)
		ampl = 15
		center = [100, 100]
		sig_x = 10
		sig_y = 10
		theta = 0

		if data_station:
			# print station
			ix, iy = lat_lon.STATION_get(path3, path2, station)
			rain_c, WRF_lat, WRF_lon = parser_gaus._get_gaus_wrf(path2, theta, sig_x, sig_y, ampl, center)
			data_wrf, rainc, date_wrf, lat_wrf, lon_wrf = parser_gaus.DATA_get_wrf(rain_c, ix, iy, date_start, date_tgt, WRF_lat, WRF_lon)
			ampl_error, out_area = calc_area_error.DATA_get_gaus(rainc, path2, ix, iy, data_station, date_start, date_tgt, date_station)
			output.RAW_out_gaus(path4, station, date_tgt, out_area)
			return(data_station, data_wrf, date_station, date_wrf, lat_wrf, lon_wrf, lat_station, lon_station, ampl_error)
		else:
			return(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan)	
################################################################################
## Header counter
with open(path1) as station_header:
	for header, line in enumerate(station_header, 1):
		if "St.no;Year;Mnth;Date;Time(UTC);RR_24" in line:
			break 

################################################################################
## For parallel processing
#STATIONfile = np.genfromtxt(path1, delimiter=";",skip_header=500, skip_footer=11)

data_out = (Parallel(n_jobs=treads, verbose=5)(delayed(DATA_get)(station, gaus_test, header) for station in station_self))

################################################################################
##Statistics
print "#######################################"
print "\nData aquisition finished, starting statistics...\n"
print "#######################################"
out, out_raw, raw_station, raw_wrf, raw_lat, raw_lon, raw_area = calc_stat.DATA_get_paralel(data_out, date_tgt)

################################################################################
##Plots
print "#######################################"
print "\nStatistics finished, rendering plots...\n"
print "#######################################"

rain_wrf, rain_station, lat, lon, lc, rc, area_erro = plot_map.DATA_get(raw_station, raw_wrf, raw_lat, raw_lon, raw_area)

plot_map.DATA_plot_scatter(rain_wrf, rain_station, lat, lon, lc, rc, path4, area_erro, path2, date0, date1)

eof = output.STAT_out(path4, date_tgt, out, out_raw)

if eof == True:
	print "#######################################"
	print "\nDone !\n"
	print "#######################################"
	exit(0)
else:
	print "#######################################"
	print "\nAn error has ocurred\n"
	print "#######################################"
	exit(1)

################################################################################
###### For serial processing 

##for station in station_self:
##	data_s, date_s, data_w, date_w = DATA_get(station, gaus_test)
##	for i in range(0, len(date_w)):
##		data_wrf.append(data_w[i])
##		date_wrf.append(date_w[i])
##	for i in range(0, len(date_s))
##		data_station.append(data_s[i])
##		date_station.append(date_s[i])

##data_wrf = np.asarray(data_wrf)
##print len(date_wrf), data_wrf

##out, out_raw= calc_stat.DATA_get(data_wrf, data_station, date_wrf, date_station)
##out.append('%s;%s;%s;%s' % (out_std, out_bias, out_mean, out_rmse))
##eof = output.STAT_out(path4, date_start, out)
################################################################################
