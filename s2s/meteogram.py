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
 
"""
###############################################################################
#GFS
def DATA_gfs_meteo(temp1, temp2, wind1, wind2, humi1, humi2, cloud1, cloud2, rain1, rain2,
					pres1, pres2, cape1, cape2, dew1, dew2, time, ixGFS, iyGFS, date0, utc0):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, temp_t1, max_t1, min_t1	= prob_time._get_TIMEP(temp1, temp2, time, 24, ixGFS, iyGFS, 27, 20)
	prob_a_g1, prob_a_r1, prob_a_y1, temp_a1, max_a1, min_a1	= prob_area._get_AREAP(temp1, time, ixGFS, iyGFS, 27, 20)
	prob_t_g1, prob_t_r1, prob_t_y1, wind_t1, max_t1, min_t1	= prob_time._get_TIMEP(wind1, wind2, time, 24, ixGFS, iyGFS, 7, 2)
	prob_a_g1, prob_a_r1, prob_a_y1, wind_a1, max_a1, min_a1	= prob_area._get_AREAP(wind1, time, ixGFS, iyGFS, 7, 2)
	prob_t_g1, prob_t_r1, prob_t_y1, humi_t1, max_t1, min_t1	= prob_time._get_TIMEP(humi1, humi2, time, 24, ixGFS, iyGFS, 0.3, 0.7)
	prob_a_g1, prob_a_r1, prob_a_y1, humi_a1, max_a1, min_a1	= prob_area._get_AREAP(humi1, time, ixGFS, iyGFS, 0.3, 0.7)
	prob_t_g1, prob_t_r1, prob_t_y1, cloud_t1, max_t1, min_t1	= prob_time._get_TIMEP(cloud1, cloud2, time, 24, ixGFS, iyGFS, 0.7, 0.5)
	prob_a_g1, prob_a_r1, prob_a_y1, cloud_a1, max_a1, min_a1	= prob_area._get_AREAP(cloud1, time, ixGFS, iyGFS, 0.7, 0.5)
	prob_t_g1, prob_t_r1, prob_t_y1, rain_t1, max_t1, min_t1	= prob_time._get_TIMEP(rain1, rain2, time, 24, ixGFS, iyGFS, 10, 0.5)
	prob_a_g1, prob_a_r1, prob_a_y1, rain_a1, max_a1, min_a1	= prob_area._get_AREAP(rain1, time, ixGFS, iyGFS, 10, 0.5)
	prob_t_g1, prob_t_r1, prob_t_y1, pres_t1, max_t1, min_t1	= prob_time._get_TIMEP(pres1, pres2, time, 24, ixGFS, iyGFS, 1000, 900)
	prob_a_g1, prob_a_r1, prob_a_y1, pres_a1, max_a1, min_a1	= prob_area._get_AREAP(pres1, time, ixGFS, iyGFS, 1000, 900)
	prob_t_g1, prob_t_r1, prob_t_y1, dew_t1, max_t1, min_t1		= prob_time._get_TIMEP(dew1, dew2, time, 24, ixGFS, iyGFS, 18, 8)
	prob_a_g1, prob_a_r1, prob_a_y1, dew_a1, max_a1, min_a1		= prob_area._get_AREAP(dew1, time, ixGFS, iyGFS, 18, 8)
	# prob_t_g1, prob_t_r1, prob_t_y1, cape_t1, max_t1, min_t1	= prob_time._get_TIMEP(cape1, cape2, time, 24, ixGFS, iyGFS, TOP, BOT)
	# prob_a_g1, prob_a_r1, prob_a_y1, cape_a1, max_a1, min_a1	= prob_area._get_AREAP(cape1, time, ixGFS, iyGFS, TOP, BOT)
	# prob_t_g1, prob_t_r1, prob_t_y1, gust_t1, max_t1, min_t1	= prob_time._get_TIMEP(gust1, gust2, time, 24, ixGFS, iyGFS, TOP, BOT)
	# prob_a_g1, prob_a_r1, prob_a_y1, gust_a1, max_a1, min_a1	= prob_area._get_AREAP(gust1, time, ixGFS, iyGFS, TOP, BOT)

	prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1 = 'null', 'null', 'null', 'null', 'null'
	date	= []
	value	= []
	b = 0
	for i in range(0, max_i):
		temp	= ((2*temp_t1	+	temp_a1)/3)
		wind	= ((2*wind_t1	+	wind_a1)/3)
		humi	= ((2*humi_t1	+	humi_a1)/3)
		cloud	= ((2*cloud_t1	+	cloud_a1)/3)
		rain	= ((2*rain_t1	+	rain_a1)/3)
		pres	= ((2*pres_t1	+	pres_a1)/3)
		dew		= ((2*dew_t1	+	dew_a1)/3)
		# cape	= ((2*cape_t1	+	cape_a1)/3)
		# cape	= ((2*gust_t1	+	gust_a1)/3)
		cape = 'null'
		gust = 'null'
		if b <= max_i - 24:
			d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = b) + datetime.timedelta(hours = utc0)
			b += 1
		else:
			d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = b) + datetime.timedelta(hours = utc0)
			b += 4
		date.append(d1)
		value.append([temp, wind, humi, cloud, rain, pres, dew, cape, gust])
		
	return(date, 'null', 'null', value, 'null', 'null')

###############################################################################
#WRF
def DATA_wrf_meteo(temp1, temp2, wind1, wind2, humi1, humi2, cloud1, cloud2, rain1, rain2,
					pres1, pres2, cape1, cape2, dew1, dew2, time, ixGFS, iyGFS, date0, utc0, TOP, BOT, PRO):
	max_i = len(time)
	prob_t_g1, prob_t_r1, prob_t_y1, temp_t1, max_t1, min_t1	= prob_time._get_TIMEP(temp1, temp2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, temp_a1, max_a1, min_a1	= prob_area._get_AREAP(temp1, time, ixGFS, iyGFS, TOP, BOT)
	prob_t_g1, prob_t_r1, prob_t_y1, wind_t1, max_t1, min_t1	= prob_time._get_TIMEP(wind1, wind2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, wind_a1, max_a1, min_a1	= prob_area._get_AREAP(wind1, time, ixGFS, iyGFS, TOP, BOT)
	prob_t_g1, prob_t_r1, prob_t_y1, humi_t1, max_t1, min_t1	= prob_time._get_TIMEP(humi1, humi2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, humi_a1, max_a1, min_a1	= prob_area._get_AREAP(humi1, time, ixGFS, iyGFS, TOP, BOT)
	prob_t_g1, prob_t_r1, prob_t_y1, cloud_t1, max_t1, min_t1	= prob_time._get_TIMEP(cloud1, cloud2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, cloud_a1, max_a1, min_a1	= prob_area._get_AREAP(cloud1, time, ixGFS, iyGFS, TOP, BOT)
	prob_t_g1, prob_t_r1, prob_t_y1, rain_t1, max_t1, min_t1	= prob_time._get_TIMEP(rain1, rain2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, rain_a1, max_a1, min_a1	= prob_area._get_AREAP(rain1, time, ixGFS, iyGFS, TOP, BOT)
	prob_t_g1, prob_t_r1, prob_t_y1, pres_t1, max_t1, min_t1	= prob_time._get_TIMEP(pres1, pres2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, pres_a1, max_a1, min_a1	= prob_area._get_AREAP(pres1, time, ixGFS, iyGFS, TOP, BOT)
	prob_t_g1, prob_t_r1, prob_t_y1, dew_t1, max_t1, min_t1		= prob_time._get_TIMEP(dew1, dew2, time, 24, ixGFS, iyGFS, TOP, BOT)
	prob_a_g1, prob_a_r1, prob_a_y1, dew_a1, max_a1, min_a1		= prob_area._get_AREAP(dew1, time, ixGFS, iyGFS, TOP, BOT)
	# prob_t_g1, prob_t_r1, prob_t_y1, cape_t1, max_t1, min_t1	= prob_time._get_TIMEP(cape1, cape2, time, 24, ixGFS, iyGFS, TOP, BOT)
	# prob_a_g1, prob_a_r1, prob_a_y1, cape_a1, max_a1, min_a1	= prob_area._get_AREAP(cape1, time, ixGFS, iyGFS, TOP, BOT)
	# prob_t_g1, prob_t_r1, prob_t_y1, gust_t1, max_t1, min_t1	= prob_time._get_TIMEP(gust1, gust2, time, 24, ixGFS, iyGFS, TOP, BOT)
	# prob_a_g1, prob_a_r1, prob_a_y1, gust_a1, max_a1, min_a1	= prob_area._get_AREAP(gust1, time, ixGFS, iyGFS, TOP, BOT)

	prob_t_g1, prob_t_r1, prob_t_y1, max_t1, min_t1 = 'null', 'null', 'null', 'null', 'null'
	date	= []
	value	= []
	for i in range(0, max_i):
		temp	= ((2*temp_t1	+	temp_a1)/3)
		wind	= ((2*wind_t1	+	wind_a1)/3)
		humi	= ((2*humi_t1	+	humi_a1)/3)
		cloud	= ((2*cloud_t1	+	cloud_a1)/3)
		rain	= ((2*rain_t1	+	rain_a1)/3)
		pres	= ((2*pres_t1	+	pres_a1)/3)
		dew		= ((2*dew_t1	+	dew_a1)/3)
		# cape	= ((2*cape_t1	+	cape_a1)/3)
		# cape	= ((2*gust_t1	+	gust_a1)/3)
		cape = 'null'
		gust = 'null'
		d1 = date0 + datetime.timedelta(hours = 0) + datetime.timedelta(hours = i) + datetime.timedelta(hours = utc0)

		date.append(d1)
		value.append([temp, wind, humi, cloud, rain, pres, dew, cape, gust])

	return(date, 'null', 'null', value, 'null', 'null')

###############################################################################