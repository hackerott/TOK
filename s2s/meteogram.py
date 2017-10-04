#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
#from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan, mean

#######################################
import prob_area
import prob_time
# import figure
#######################################
"""
Each variable should have botton and top limits to calculate the alert level, as also the limit for indecision, where the alert color should be truncated (ex: whem max prob is below X%, set color to y).
del the arrays is a bad bad way for preserving memmory. Quick and dirt fix for memory overflow
 
"""
###############################################################################
#GFS
def DATA_gfs_meteo(temp1, temp2, wind1, wind2, humi1, humi2, cloud1, cloud2, rain1, rain2,
					pres1, pres2, cape1, cape2, dew1, dew2, time, ixGFS, iyGFS, date0, utc0, iz):
	max_i = len(time)
	# del time
	prob_t_g1, prob_t_r1, prob_t_y1, temp_t1, max_t1, min_t1	= prob_time._get_TIMEP(temp1, temp2, time, iz, ixGFS, iyGFS, 27, 20)
	prob_a_g1, prob_a_r1, prob_a_y1, temp_a1, max_a1, min_a1	= prob_area._get_AREAP(temp1, time, ixGFS, iyGFS, 27, 20)
	temp_p = np.divide(np.add(np.multiply(temp_t1, 2), temp_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1 
	del temp_t1, temp_a1, temp1, temp2
	prob_t_g1, prob_t_r1, prob_t_y1, wind_t1, max_t1, min_t1	= prob_time._get_TIMEP(wind1, wind2, time, iz, ixGFS, iyGFS, 7, 2)
	prob_a_g1, prob_a_r1, prob_a_y1, wind_a1, max_a1, min_a1	= prob_area._get_AREAP(wind1, time, ixGFS, iyGFS, 7, 2)
	wind_p = np.divide(np.add(np.multiply(wind_t1, 2), wind_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del wind_t1, wind_a1, wind1, wind2
	prob_t_g1, prob_t_r1, prob_t_y1, humi_t1, max_t1, min_t1	= prob_time._get_TIMEP(humi1, humi2, time, iz, ixGFS, iyGFS, 0.3, 0.7)
	prob_a_g1, prob_a_r1, prob_a_y1, humi_a1, max_a1, min_a1	= prob_area._get_AREAP(humi1, time, ixGFS, iyGFS, 0.3, 0.7)
	humi_p = np.divide(np.add(np.multiply(humi_t1, 2), humi_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del humi_t1, humi_a1, humi1, humi2
	prob_t_g1, prob_t_r1, prob_t_y1, cloud_t1, max_t1, min_t1	= prob_time._get_TIMEP(cloud1, cloud2, time, iz, ixGFS, iyGFS, 0.7, 0.5)
	prob_a_g1, prob_a_r1, prob_a_y1, cloud_a1, max_a1, min_a1	= prob_area._get_AREAP(cloud1, time, ixGFS, iyGFS, 0.7, 0.5)
	cloud_p = np.divide(np.add(np.multiply(cloud_t1, 2), cloud_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del cloud_t1, cloud_a1, cloud1, cloud2
	prob_t_g1, prob_t_r1, prob_t_y1, rain_t1, max_t1, min_t1	= prob_time._get_TIMEP(rain1, rain2, time, iz, ixGFS, iyGFS, 10, 0.5)
	prob_a_g1, prob_a_r1, prob_a_y1, rain_a1, max_a1, min_a1	= prob_area._get_AREAP(rain1, time, ixGFS, iyGFS, 10, 0.5)
	rain_p = np.divide(np.add(np.multiply(rain_t1, 2), rain_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del rain_t1, rain_a1, rain1, rain2
	prob_t_g1, prob_t_r1, prob_t_y1, pres_t1, max_t1, min_t1	= prob_time._get_TIMEP(pres1, pres2, time, iz, ixGFS, iyGFS, 1000, 900)
	prob_a_g1, prob_a_r1, prob_a_y1, pres_a1, max_a1, min_a1	= prob_area._get_AREAP(pres1, time, ixGFS, iyGFS, 1000, 900)
	pres_p = np.divide(np.add(np.multiply(pres_t1, 2), pres_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del pres_t1, pres_a1, pres1, pres2
	prob_t_g1, prob_t_r1, prob_t_y1, dew_t1, max_t1, min_t1		= prob_time._get_TIMEP(dew1, dew2, time, iz, ixGFS, iyGFS, 18, 8)
	prob_a_g1, prob_a_r1, prob_a_y1, dew_a1, max_a1, min_a1		= prob_area._get_AREAP(dew1, time, ixGFS, iyGFS, 18, 8)
	dew_p = np.divide(np.add(np.multiply(dew_t1, 2), dew_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del dew_t1, dew_a1, dew1, dew2

	# prob_t_g1, prob_t_r1, prob_t_y1, cape_t1, max_t1, min_t1	= prob_time._get_TIMEP(cape1, cape2, time, iz, ixGFS, iyGFS, TOP, BOT)
	# prob_a_g1, prob_a_r1, prob_a_y1, cape_a1, max_a1, min_a1	= prob_area._get_AREAP(cape1, time, ixGFS, iyGFS, TOP, BOT)
	# prob_t_g1, prob_t_r1, prob_t_y1, gust_t1, max_t1, min_t1	= prob_time._get_TIMEP(gust1, gust2, time, iz, ixGFS, iyGFS, TOP, BOT)
	# prob_a_g1, prob_a_r1, prob_a_y1, gust_a1, max_a1, min_a1	= prob_area._get_AREAP(gust1, time, ixGFS, iyGFS, TOP, BOT)

	date	= []
	value	= []
	b = 0
	cape = 'null'
	gust = 'null'
	for i in range(0, max_i):
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = i) + datetime.timedelta(hours = utc0)
		date.append(d1)
		try:
			value.append([int(temp_p[i]*10)/10.0, int(wind_p[i]*10)/10.0, int(humi_p[i]*10)/10.0, int(cloud_p[i]*100), int(rain_p[i]*10)/10.0, int(pres_p[i]*10)/10.0, int(dew_p[i]*10)/10.0, cape, gust])
		except:
			value.append([temp_p[i], wind_p[i], humi_p[i], cloud_p[i], rain_p[i], pres_p[i], dew_p[i], cape, gust])	
	del temp_p, wind_p, humi_p, cloud_p, rain_p, pres_p, dew_p, cape, gust
	return(date, 'null', 'null', value, 'null', 'null')

###############################################################################
#WRF
def DATA_wrf_meteo(temp1, temp2, wind1, wind2, humi1, humi2, cloud1, cloud2, rain1, rain2,
					pres1, pres2, cape1, cape2, dew1, dew2, time, ixWRF, iyWRF, date0, utc0, iz):
	max_i = len(time)
	# del time
	prob_t_g1, prob_t_r1, prob_t_y1, temp_t1, max_t1, min_t1	= prob_time._get_TIMEP(temp1, temp2, time, iz, ixWRF, iyWRF, 27, 20)
	prob_a_g1, prob_a_r1, prob_a_y1, temp_a1, max_a1, min_a1	= prob_area._get_AREAP(temp1, time, ixWRF, iyWRF, 27, 20)
	temp_p = np.divide(np.add(np.multiply(temp_t1, 2), temp_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1 
	del temp_t1, temp_a1, temp1, temp2
	prob_t_g1, prob_t_r1, prob_t_y1, wind_t1, max_t1, min_t1	= prob_time._get_TIMEP(wind1, wind2, time, iz, ixWRF, iyWRF, 7, 2)
	prob_a_g1, prob_a_r1, prob_a_y1, wind_a1, max_a1, min_a1	= prob_area._get_AREAP(wind1, time, ixWRF, iyWRF, 7, 2)
	wind_p = np.divide(np.add(np.multiply(wind_t1, 2), wind_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del wind_t1, wind_a1, wind1, wind2
	prob_t_g1, prob_t_r1, prob_t_y1, humi_t1, max_t1, min_t1	= prob_time._get_TIMEP(humi1, humi2, time, iz, ixWRF, iyWRF, 0.3, 0.7)
	prob_a_g1, prob_a_r1, prob_a_y1, humi_a1, max_a1, min_a1	= prob_area._get_AREAP(humi1, time, ixWRF, iyWRF, 0.3, 0.7)
	humi_p = np.divide(np.add(np.multiply(humi_t1, 2), humi_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del humi_t1, humi_a1, humi1, humi2
	prob_t_g1, prob_t_r1, prob_t_y1, cloud_t1, max_t1, min_t1	= prob_time._get_TIMEP(cloud1, cloud2, time, iz, ixWRF, iyWRF, 0.7, 0.5)
	prob_a_g1, prob_a_r1, prob_a_y1, cloud_a1, max_a1, min_a1	= prob_area._get_AREAP(cloud1, time, ixWRF, iyWRF, 0.7, 0.5)
	cloud_p = np.divide(np.add(np.multiply(cloud_t1, 2), cloud_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del cloud_t1, cloud_a1, cloud1, cloud2
	prob_t_g1, prob_t_r1, prob_t_y1, rain_t1, max_t1, min_t1	= prob_time._get_TIMEP(rain1, rain2, time, iz, ixWRF, iyWRF, 10, 0.5)
	prob_a_g1, prob_a_r1, prob_a_y1, rain_a1, max_a1, min_a1	= prob_area._get_AREAP(rain1, time, ixWRF, iyWRF, 10, 0.5)
	rain_p = np.divide(np.add(np.multiply(rain_t1, 2), rain_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del rain_t1, rain_a1, rain1, rain2
	prob_t_g1, prob_t_r1, prob_t_y1, pres_t1, max_t1, min_t1	= prob_time._get_TIMEP(pres1, pres2, time, iz, ixWRF, iyWRF, 1000, 900)
	prob_a_g1, prob_a_r1, prob_a_y1, pres_a1, max_a1, min_a1	= prob_area._get_AREAP(pres1, time, ixWRF, iyWRF, 1000, 900)
	pres_p = np.divide(np.add(np.multiply(pres_t1, 2), pres_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del pres_t1, pres_a1, pres1, pres2
	prob_t_g1, prob_t_r1, prob_t_y1, dew_t1, max_t1, min_t1		= prob_time._get_TIMEP(dew1, dew2, time, iz, ixWRF, iyWRF, 18, 8)
	prob_a_g1, prob_a_r1, prob_a_y1, dew_a1, max_a1, min_a1		= prob_area._get_AREAP(dew1, time, ixWRF, iyWRF, 18, 8)
	dew_p = np.divide(np.add(np.multiply(dew_t1, 2), dew_a1), 3)
	del prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1, prob_a_g1, prob_a_r1, prob_a_y1, max_a1, min_a1
	del dew_t1, dew_a1, dew1, dew2

	# prob_t_g1, prob_t_r1, prob_t_y1, cape_t1, max_t1, min_t1	= prob_time._get_TIMEP(cape1, cape2, time, iz, ixWRF, iyWRF, TOP, BOT)
	# prob_a_g1, prob_a_r1, prob_a_y1, cape_a1, max_a1, min_a1	= prob_area._get_AREAP(cape1, time, ixWRF, iyWRF, TOP, BOT)
	# prob_t_g1, prob_t_r1, prob_t_y1, gust_t1, max_t1, min_t1	= prob_time._get_TIMEP(gust1, gust2, time, iz, ixWRF, iyWRF, TOP, BOT)
	# prob_a_g1, prob_a_r1, prob_a_y1, gust_a1, max_a1, min_a1	= prob_area._get_AREAP(gust1, time, ixWRF, iyWRF, TOP, BOT)

	date	= []
	value	= []
	b = 0
	cape = 'null'
	gust = 'null'
	for i in range(0, max_i):
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = i) + datetime.timedelta(hours = utc0)
		date.append(d1)
		try:
			value.append([int(temp_p[i]*10)/10.0, int(wind_p[i]*10)/10.0, int(humi_p[i]*10)/10.0, int(cloud_p[i]*100), int(rain_p[i]*10)/10.0, int(pres_p[i]*10)/10.0, int(dew_p[i]*10)/10.0, cape, gust])
		except:
			value.append([temp_p[i], wind_p[i], humi_p[i], cloud_p[i], rain_p[i], pres_p[i], dew_p[i], cape, gust])	

	del temp_p, wind_p, humi_p, cloud_p, rain_p, pres_p, dew_p, cape, gust
	return(date, 'null', 'null', value, 'null', 'null')

###############################################################################