#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cgi
import datetime
import json
import numpy as np
# import os
# import netCDF4
# import math
# import sys
# import cgitb
# import calendar
# import base64

# from math import pi
# from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan
#######################################
# S2S imports
import gfs_var
import lat_lon
import calendar
import card
import table
import prob_area
import prob_time
import json_output
import astro_tz
import cond_figures
#######################################
##	GET form			
form = cgi.FieldStorage()
					
lat 	= form.getvalue("lat")	
lon 	= form.getvalue("lon")	
utc 	= form.getvalue("utc")	
var 	= form.getvalue("var")	
#date 	= form.getvalue("date")
model 	= form.getvalue("model")
#token 	= form.getvalue("token")
#cid 	= form.getvalue("id")

#######################################
##Form treatment
#ip  	= os.environ["REMOTE_ADDR"]
#date0	= datetime.datetime.strptime(date, '%Y%m%d')
#date1	= date0 - datetime.timedelta(days =1)
lat0	= float(lat)
lon0	= float(lon)
try:
	utc0	= int(utc)
except:
	utc0 = astro_tz._get_timezone(lat0, lon0)

#######################################
"""
Validation will be inserted after, using flask to genarete a session token

"""
#====> validadtion here

###############################################################################
## get files, lat_lon, id and limits
ens1, ens2, date0 = gfs_var._get_FILE()
ix_gfs, iy_gfs = lat_lon.GFS_grab(ens1, lat0, lon0)
var_id = gfs_var._get_ID(var)
PRO, TOP, BOT = gfs_var._get_LIM(var)

###############################################################################
##
if var_id == 1 :
	var_raw1 = gfs_var._get_rain(var, ens1)
	var_raw2 = gfs_var._get_rain(var, ens2)	
	time  	 = gfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini = calendar.DATA_gfs_calendar(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, c = card.DATA_gfs_card(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

elif var_id == 2:
	var_rawa1, var_rawb1 = gfs_var._get_wind(var, ens1)
	var_rawa2, var_rawb2 = gfs_var._get_wind(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini = calendar.DATA_gfs_calendar(var_rawa1, var_rawa2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		for i in range(0, len(value)):
			value[i] = [value[i], int(var_rawb1[i, ix_gfs, iy_gfs])]
	elif model == "card":
		date, prob, color, value, maxi, mini, c = card.DATA_gfs_card(var_rawa1, var_rawa2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
		value = [value, int(var_rawb1[c, ix_gfs, iy_gfs])]
	elif model == "table":
		date, prob, color, value, maxi, mini = table.DATA_gfs_table(var_rawa1, var_rawa2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
		for i in range(0, len(value)):
			value[i] = [value[i], int(var_rawb1[i, ix_gfs, iy_gfs])]
		value = np.array(value)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

elif var_id == 3:
	var_raw1 = gfs_var._get_temperature(var, ens1)
	var_raw2 = gfs_var._get_temperature(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini = calendar.DATA_gfs_calendar(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, c = card.DATA_gfs_card(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

elif var_id == 4:
	var_raw1 = gfs_var._get_radiation(var, ens1)
	var_raw2 = gfs_var._get_radiation(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini = calendar.DATA_gfs_calendar(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, c = card.DATA_gfs_card(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

elif var_id == 5:
	var_raw1 = gfs_var._get_humidity(var, ens1)
	var_raw2 = gfs_var._get_humidity(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini = calendar.DATA_gfs_calendar(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, c = card.DATA_gfs_card(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success, dic = json_output._get_ERROR(var_id, model) 


elif var_id == 6:
	var_rawa1, var_rawb1 = gfs_var._get_figure(var, ens1)
	var_rawa2, var_rawb2 = gfs_var._get_figure(var, ens2)
	time  	 = cfs_var._get_time('time', ens1)
	var_rawa1 = np.max(var_rawa1, axis=0) 
	var_rawa2 = np.max(var_rawa2, axis=0) 
	if model == "calendar":
		date, prob, color, value1, maxi, mini = calendar.DATA_gfs_calendar(var_rawa1, var_rawa2, time, ix_gfs, iy_gfs, date0, utc0, 0.75, 0.25, 0.5)
		date, prob, color, value2, maxi, mini = calendar.DATA_gfs_calendar(var_rawb1, var_rawb2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value1, maxi, mini, c = card.DATA_gfs_card(var_rawa1, var_rawa2, time, ix_gfs, iy_gfs, date0, utc0, 0.75, 0.25, 0.5)	
		date, prob, color, value2, maxi, mini, c = card.DATA_gfs_card(var_rawb1, var_rawb2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value1, maxi, mini = table.DATA_gfs_table(var_rawa1, var_rawa2, time, ix_gfs, iy_gfs, date0, utc0, 0.75, 0.25, 0.5)
		date, prob, color, value2, maxi, mini = table.DATA_gfs_table(var_rawb1, var_rawb2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 
	sunset, sunrise = astro_tz._get_sun(lat0, lon0, utc0)
	value = cond_figures.DATA_cond_figure(value1, value2, date, sunset, sunrise)

elif var_id == 7:
	rain1, speed1, direction1, radiation1, temperature1, humidity1 = gfs_var._get_all(var, ens1)
	rain2, speed2, direction2, radiation2, temperature2, humidity2 = gfs_var._get_all(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	if model == "calendar":
		date1, prob1, color1, value1, maxi1, mini1 = calendar.DATA_gfs_calendar(rain1, rain2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date2, prob2, color2, value2, maxi2, mini2 = calendar.DATA_gfs_calendar(speed1, speed2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date3, prob3, color3, value3, maxi3, mini3 = calendar.DATA_gfs_calendar(temperature1, temperature2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date4, prob4, color4, value4, maxi4, mini4 = calendar.DATA_gfs_calendar(radiation1, radiation2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date5, prob5, color5, value5, maxi5, mini5 = calendar.DATA_gfs_calendar(humidity1, humidity2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date1, prob1, color1, value1, maxi1, mini1 = card.DATA_gfs_card(rain1, rain2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date2, prob2, color2, value2, maxi2, mini2 = card.DATA_gfs_card(speed1, speed2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date3, prob3, color3, value3, maxi3, mini3 = card.DATA_gfs_card(temperature1, temperature2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date4, prob4, color4, value4, maxi4, mini4 = card.DATA_gfs_card(radiation1, radiation2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date5, prob5, color5, value5, maxi5, mini5 = card.DATA_gfs_card(humidity1, humidity2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	elif model == "table":
		date1, prob1, color1, value1, maxi1, mini1 = table.DATA_gfs_table(rain1, rain2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date2, prob2, color2, value2, maxi2, mini2 = table.DATA_gfs_table(speed1, speed2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date3, prob3, color3, value3, maxi3, mini3 = table.DATA_gfs_table(temperature1, temperature2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date4, prob4, color4, value4, maxi4, mini4 = table.DATA_gfs_table(radiation1, radiation2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
		date5, prob5, color5, value5, maxi5, mini5 = table.DATA_gfs_table(humidity1, humidity2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

	date	= [date1, date2, date3, date4, date5]
	prob	= [prob1, prob2, prob3, prob4, prob5]
	color	= [color1, color2, color3, color4, color5]
	value	= [value1, value2, value3, value4, value5]
	maxi	= [maxi1, maxi2, maxi3, maxi4, maxi5]
	mini	= [mini1, mini2, mini3, mini4, mini5]

else:
	success, dic = json_output._get_ERROR(var_id, model)
	# print "Content-type: application/json\n\n"
	# print json.dumps(dic)
	# exit(1)

if success == False:
	print "Content-type: application/json\n\n"
	print json.dumps(dic)
	exit(1)

else:
	success, dic = json_output._get_OUT(date, prob, color, value, maxi, mini, model, var_id)
	print "Content-type: application/json\n\n"
	print json.dumps(dic)
	exit(0)
