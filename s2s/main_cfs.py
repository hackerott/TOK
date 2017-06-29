#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cgi
import datetime
# import os
# import numpy as np
# import netCDF4
# import math
# import sys
# import cgitb
# import calendar
# import json
# import base64

# from math import pi
# from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan
#######################################
# S2S imports
import var_cfs
import lat_lon
import calendar
import card
import prob_area
import prob_time
import json_out

#######################################
##	GET form			
form = cgi.FieldStorage()
					
lat 	= form.getvalue("lat")	
lon 	= form.getvalue("lon")	
utc 	= form.getvalue("utc")	
var 	= form.getvalue("var")	
date 	= form.getvalue("date")
model 	= form.getvalue("tipo")
#token 	= form.getvalue("token")
#cid 	= form.getvalue("id")

#######################################
##Form treatment
#ip  	= os.environ["REMOTE_ADDR"]
date0	= datetime.datetime.strptime(date, '%Y%m%d')
date1	= date0 - datetime.timedelta(days =1)
lat0	= float(lat)
lon0	= float(lon)
utc0	= int(utc)

#######################################
"""
Validation will be inserted after, using flask to genarete a session token

"""
#====> validadtion here

###############################################################################
## get files, lat_lon, id and limits
ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8 = cfs_var._get_FILE(date0, date1)
ix_cfs, iy_cfs = lat_lon.CFS_grab(ens1, lat, lon)
var_id = cfs_var._get_ID(var)
PRO, TOP, BOT = cfs_var._get_LIM(var)

###############################################################################
##
if var_id == 1 :
	var_raw1 = cfs_var._get_rain(var, ens1)
	var_raw2 = cfs_var._get_rain(var, ens2)	
	var_raw3 = cfs_var._get_rain(var, ens3)
	var_raw4 = cfs_var._get_rain(var, ens4)
	var_raw5 = cfs_var._get_rain(var, ens5)
	var_raw6 = cfs_var._get_rain(var, ens6)
	var_raw7 = cfs_var._get_rain(var, ens7)
	var_raw8 = cfs_var._get_rain(var, ens8)
	time  	 = cfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 2:
	var_rawa1, var_rawb1 = cfs_var._get_wind(var, ens1)
	var_rawa2, var_rawb2 = cfs_var._get_wind(var, ens2)
	var_rawa3, var_rawb3 = cfs_var._get_wind(var, ens3)
	var_rawa4, var_rawb4 = cfs_var._get_wind(var, ens4)
	var_rawa5, var_rawb5 = cfs_var._get_wind(var, ens5)
	var_rawa6, var_rawb6 = cfs_var._get_wind(var, ens6)
	var_rawa7, var_rawb7 = cfs_var._get_wind(var, ens7)
	var_rawa8, var_rawb8 = cfs_var._get_wind(var, ens8)
	time  	 = cfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 3:
	var_raw1 = cfs_var._get_temperature(var, ens1)
	var_raw2 = cfs_var._get_temperature(var, ens2)
	var_raw3 = cfs_var._get_temperature(var, ens3)
	var_raw4 = cfs_var._get_temperature(var, ens4)
	var_raw5 = cfs_var._get_temperature(var, ens5)
	var_raw6 = cfs_var._get_temperature(var, ens6)
	var_raw7 = cfs_var._get_temperature(var, ens7)
	var_raw8 = cfs_var._get_temperature(var, ens8)
	time  	 = cfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 4:
	var_raw1 = cfs_var._get_radiation(var, ens1)
	var_raw2 = cfs_var._get_radiation(var, ens2)
	var_raw3 = cfs_var._get_radiation(var, ens3)
	var_raw4 = cfs_var._get_radiation(var, ens4)
	var_raw5 = cfs_var._get_radiation(var, ens5)
	var_raw6 = cfs_var._get_radiation(var, ens6)
	var_raw7 = cfs_var._get_radiation(var, ens7)
	var_raw8 = cfs_var._get_radiation(var, ens8)
	time  	 = cfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 5:
	var_raw1 = cfs_var._get_humidity(var, ens1)
	var_raw2 = cfs_var._get_humidity(var, ens2)
	var_raw3 = cfs_var._get_humidity(var, ens3)
	var_raw4 = cfs_var._get_humidity(var, ens4)
	var_raw5 = cfs_var._get_humidity(var, ens5)
	var_raw6 = cfs_var._get_humidity(var, ens6)
	var_raw7 = cfs_var._get_humidity(var, ens7)
	var_raw8 = cfs_var._get_humidity(var, ens8)
	time  	 = cfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 6:
	rain1, speed1, direction1, radiation1, temperature1, humidity1 = cfs_var._get_all(var, ens1)
	rain2, speed2, direction2, radiation2, temperature2, humidity2 = cfs_var._get_all(var, ens2)
	rain3, speed3, direction3, radiation3, temperature3, humidity3 = cfs_var._get_all(var, ens3)
	rain4, speed4, direction4, radiation4, temperature4, humidity4 = cfs_var._get_all(var, ens4)
	rain5, speed5, direction5, radiation5, temperature5, humidity5 = cfs_var._get_all(var, ens5)
	rain6, speed6, direction6, radiation6, temperature6, humidity6 = cfs_var._get_all(var, ens6)
	rain7, speed7, direction7, radiation7, temperature7, humidity7 = cfs_var._get_all(var, ens7)
	rain8, speed8, direction8, radiation8, temperature8, humidity8 = cfs_var._get_all(var, ens8)
	time  	 = cfs_var._get_time('time', ens1)
	if model == "calendar":
		date1, prob1, color1, value1, maxi1, mini1, fig1 = calendar.DATA_cfs_calendar(rain1, rain2, rain3, rain4, rain5, rain6, rain7, rain8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date2, prob2, color2, value2, maxi2, mini2, fig2 = calendar.DATA_cfs_calendar(speed1, speed2, speed3, speed4, speed5, speed6, speed7, speed8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date3, prob3, color3, value3, maxi3, mini3, fig3 = calendar.DATA_cfs_calendar(temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, temperature7, temperature8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date4, prob4, color4, value4, maxi4, mini4, fig4 = calendar.DATA_cfs_calendar(radiation1, radiation2, radiation3, radiation4, radiation5, radiation6, radiation7, radiation8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date5, prob5, color5, value5, maxi5, mini5, fig5 = calendar.DATA_cfs_calendar(humidity1, humidity2, humidity3, humidity4, humidity5, humidity6, humidity7, humidity8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)

	elif model == "card":
		date1, prob1, color1, value1, maxi1, mini1, fig1 = card.DATA_cfs_card(rain1, rain2, rain3, rain4, rain5, rain6, rain7, rain8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date2, prob2, color2, value2, maxi2, mini2, fig2 = card.DATA_cfs_card(speed1, speed2, speed3, speed4, speed5, speed6, speed7, speed8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date3, prob3, color3, value3, maxi3, mini3, fig3 = card.DATA_cfs_card(temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, temperature7, temperature8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date4, prob4, color4, value4, maxi4, mini4, fig4 = card.DATA_cfs_card(radiation1, radiation2, radiation3, radiation4, radiation5, radiation6, radiation7, radiation8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date5, prob5, color5, value5, maxi5, mini5, fig5 = card.DATA_cfs_card(humidity1, humidity2, humidity3, humidity4, humidity5, humidity6, humidity7, humidity8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)

	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

	date	= [date1, date2, date3, date4, date5]
	prob	= [prob1, prob2, prob3, prob4, prob5]
	color	= [color1, color2, color3, color4, color5]
	value	= [value1, value2, value3, value4, value5]
	maxi	= [maxi1, maxi2, maxi3, maxi4, maxi5]
	mini	= [mini1, mini2, mini3, mini4, mini5]
	fig		= [fig1, fig2, fig3, fig4, fig5]

else:
	success = json_out._get_ERROR(var_id, model)
	exit(1)

success = json_out._get_OUT(date, prob, color, value, maxi, mini, fig, model)

if success == True:
	exit(0)
else:
	exit(1)