#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cgi
import datetime
import json
import numpy as np

import wrf_var
import gfs_var
import cfs_var

import lat_lon
import calendar
import card
import prob_area
import prob_time
import json_output
import astro_tz
#######################################
##	GET form			
form = cgi.FieldStorage()
					
lat 	= form.getvalue("lat")	
lon 	= form.getvalue("lon")
lat0	= float(lat)
lon0	= float(lon)

#######################################'
## Check WRF available variables
def _check_wrf():
	ens1, ens2, date0 = wrf_var._get_FILE()
	w_rain = wrf_var._get_rain('chuva', ens2)
	w_wind, w_dire = wrf_var._get_wind('vento', ens2)
	w_temp = wrf_var._get_temperature('temp', ens2)
	w_radi = wrf_var._get_radiation('radiacao', ens2)
	w_humi = wrf_var._get_humidity('umidade', ens2)

	if type(w_rain) is np.ndarray:
		w_rain = True
	else:
		w_rain = False
	if type(w_wind) is np.ndarray:
		w_wind = True
	else:
		w_wind = False
	if type(w_temp) is np.ndarray:
		w_temp = True
	else:
		w_temp = False
	if type(w_radi) is np.ndarray:
		w_radi = True
	else:
		w_radi = False
	if type(w_humi) is np.ndarray:
		w_humi = True
	else:
		w_humi = False
	out = [w_rain, w_wind, w_temp, w_radi,  w_humi]	
	return out
#######################################
## Check GFS available variables
def _check_gfs():
	ens1, ens2, date0 = gfs_var._get_FILE()
	g_rain = gfs_var._get_rain('chuva', ens2)
	g_wind, g_dire = gfs_var._get_wind('vento', ens2)
	g_temp = gfs_var._get_temperature('temp', ens2)
	g_radi = gfs_var._get_radiation('radiacao', ens2)
	g_humi = gfs_var._get_humidity('umidade', ens2)

	if type(g_rain) is np.ndarray:
		g_rain = True
	else:
		g_rain = False
	if type(g_wind) is np.ndarray:
		g_wind = True
	else:
		g_wind = False
	if type(g_temp) is np.ndarray:
		g_temp = True
	else:
		g_temp = False
	if type(g_radi) is np.ndarray:
		g_radi = True
	else:
		g_radi = False
	if type(g_humi) is np.ndarray:
		g_humi = True
	else:
		g_humi = False
	out = [g_rain, g_wind, g_temp, g_radi,  g_humi]	
	return out
#######################################
## Check CFS available variables
def _check_cfs():
	ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, date0 = cfs_var._get_FILE()
	c_rain = cfs_var._get_rain('chuva', ens5)
	c_wind, c_dire = cfs_var._get_wind('vento', ens5)
	c_temp = cfs_var._get_temperature('temp', ens5)
	c_radi = cfs_var._get_radiation('radiacao', ens5)
	c_humi = cfs_var._get_humidity('umidade', ens5)

	
	if type(c_rain) is np.ndarray:
		c_rain = True
	else:
		c_rain = False
	if type(c_wind) is np.ndarray:
		c_wind = True
	else:
		c_wind = False
	if type(c_temp) is np.ndarray:
		c_temp = True
	else:
		c_temp = False
	if type(c_radi) is np.ndarray:
		c_radi = True
	else:
		c_radi = False
	if type(c_humi) is np.ndarray:
		c_humi = True	
	else:
		c_humi = False

	out = [c_rain, c_wind, c_temp, c_radi,  c_humi]	
	return out
#######################################
## Check if lat_lon is inside forecast area
def _check_point(lat0, lon0):

	out = True
	return out
#######################################
## Get timezone
utc = astro_tz._get_timezone(lat0, lon0)

## Get sun set and rise
sun_rise, sun_set = astro_tz._get_sun(lat0, lon0, utc)

## Get variables availeble
'''
Needs some kind of paralelism, or async operation, gfs and cfs takes more then 5 seconds
'''
w_out = _check_wrf()
g_out = _check_gfs()
c_out = _check_cfs()

## Get point valid
point = _check_point(lat0, lon0)
#######################################
## Get output json
success, dic = json_output._get_AUX(utc, sun_set, sun_rise, point, w_out, g_out, c_out) 

print "Content-type: application/json\n\n"
print json.dumps(dic)
exit(0)