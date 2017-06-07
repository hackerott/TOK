#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import timeit
import os

#######################################
import lat_lon
import parser_wrf
#######################################

def RAW_out(path4, station, date_self, date_wrf, data_station, data_wrf):
	header = '%s\n date; WRF; Station\n\n' % station
	out = []
	for i in range(0, len(data_wrf)+1):
		if len(data_station) <= 1 or len(data_wrf) <= 1 or len(date_wrf) <= 1:
			break
		out.append('%s; %s; %s' %(date_wrf[i], data_station[i], data_wrf[i])) 
	folder_path = '%s/%s' % (path4, date_self)
	if os.path.isdir(folder_path) == False:
		os.makedirs(folder_path)
	file_name_raw	= "%s/%s/%s_%s.csv" % (path4, date_self, date_self, station) #file name and path
	file_raw	= open(file_name_raw, 'a+')		
	file_raw.write(header)
	file_raw.write("\n".join(out))
	file_raw.close()
	eof = []
	return()

def STAT_out(path4, date_self, out, out_raw):
#	header		= "\n WRF_STD; Station_STD; WRF_Mean; Station_Mean; Bias; Error\n" 
	header		= "\n std_wrf, mean_wrf, std_station, mean_station, R, rmse, bias, Er+d/D\n"
	file_name_stat	= "%s/%s_stat.csv" % (path4, date_self) #file name and path 
	file_stat	= open(file_name_stat, 'a+')
	file_stat.write(header)
	file_stat.write(out)
	file_stat.close()
	file_name_raw	= "%s/%s_raw.csv" % (path4, date_self) #file name and path 
	file_raw	= open(file_name_raw, 'a+')
	header_raw		= "\n Date; WRF; Station\n" 
	file_raw.write(header)
	file_raw.write("\n".join(out_raw))
	file_raw.close()

	eof = True
	return(eof)

def TIME_out(path2, station_self):
	start = timeit.default_timer()

	ix_self, iy_self = lat_lon.WRF_get(path2, 10, 10)
	data_wrf_self, date_wrf_self, lat_self, lon_self = parser_wrf.DATA_get(path2, ix_self, iy_self, 20161122, 20161122)
	stop = timeit.default_timer()
	total_runs = len(station_self) 
	run_time = (stop - start) * (total_runs)
	return(run_time, total_runs)

