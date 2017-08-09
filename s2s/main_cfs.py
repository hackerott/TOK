#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cgi
import datetime
import json
# import os
# import numpy as np
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
import cfs_var
import lat_lon
import calendar
import card
import prob_area
import prob_time
import json_output
import astro_tz
import cond_figures
import units
import color
#######################################
##	GET form			
form = cgi.FieldStorage()
					
lat 	= form.getvalue("lat")	
lon 	= form.getvalue("lon")	
#utc 	= form.getvalue("utc")	
var 	= form.getvalue("var")	
unit 	= form.getvalue("unit")
model 	= form.getvalue("model")
#token 	= form.getvalue("token")
#cid 	= form.getvalue("id")

#######################################
##Form treatment
#ip  	= os.environ["REMOTE_ADDR"]
# date0	= datetime.datetime.strptime(date, '%Y%m%d') #add diference from now_date to start_date 
# date1	= date0 - datetime.timedelta(days =1) #add diference from now_date to start_date
lat0	= float(lat)
lon0	= float(lon)
try:
	utc 	= form.getvalue("utc")	
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
ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, date0 = cfs_var._get_FILE()
ix_cfs, iy_cfs = lat_lon.CFS_grab(ens1, lat0, lon0)
var_id = cfs_var._get_ID(var)
PRO, TOP, BOT = cfs_var._get_LIM(var)
success = True
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
		date, prob, alert, value, maxi, mini = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_output._get_ERROR(var_id, model) 
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
		date, prob, alert, value, maxi, mini = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		for i in range(0, len(value)):
			value[i] = [value[i], int(var_rawb1[i, ix_cfs, iy_cfs])]
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
		value = [value, int(var_rawb1[i, ix_cfs, iy_cfs])]
		
	else:
		success = json_output._get_ERROR(var_id, model) 
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
		date, prob, alert, value, maxi, mini = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

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
		date, prob, alert, value, maxi, mini = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

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
		date, prob, alert, value, maxi, mini = calendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

elif var_id == 6:
	var_rawa1, var_rawb1 = cfs_var._get_figure(var, ens1)
	var_rawa2, var_rawb2 = cfs_var._get_figure(var, ens2)
	var_rawa3, var_rawb3 = cfs_var._get_figure(var, ens3)
	var_rawa4, var_rawb4 = cfs_var._get_figure(var, ens4)
	var_rawa5, var_rawb5 = cfs_var._get_figure(var, ens5)
	var_rawa6, var_rawb6 = cfs_var._get_figure(var, ens6)
	var_rawa7, var_rawb7 = cfs_var._get_figure(var, ens7)
	var_rawa8, var_rawb8 = cfs_var._get_figure(var, ens8)
	time  	 = cfs_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, alert, value1, maxi, mini = calendar.DATA_cfs_calendar(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, 0.75, 0.25, 0.5)
		date, prob, alert, value2, maxi, mini = calendar.DATA_cfs_calendar(var_rawb1, var_rawb2, var_rawb3, var_rawb4, var_rawb5, var_rawb6, var_rawb7, var_rawb8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, alert, value1, maxi, mini, i = calendar.DATA_cfs_card(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, 0.75, 0.25, 0.5)
		date, prob, alert, value2, maxi, mini, i = calendar.DATA_cfs_card(var_rawb1, var_rawb2, var_rawb3, var_rawb4, var_rawb5, var_rawb6, var_rawb7, var_rawb8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 
	sunset, sunrise = astro_tz._get_sun(lat0, lon0, utc0)
	value = cond_figures.DATA_cond_figure(value1, value2, date, sunset, sunrise)
	
elif var_id == 7:
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
		date1, prob1, alert1, value1, maxi1, mini1 = calendar.DATA_cfs_calendar(rain1, rain2, rain3, rain4, rain5, rain6, rain7, rain8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date2, prob2, alert2, value2, maxi2, mini2 = calendar.DATA_cfs_calendar(speed1, speed2, speed3, speed4, speed5, speed6, speed7, speed8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date3, prob3, alert3, value3, maxi3, mini3 = calendar.DATA_cfs_calendar(temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, temperature7, temperature8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date4, prob4, alert4, value4, maxi4, mini4 = calendar.DATA_cfs_calendar(radiation1, radiation2, radiation3, radiation4, radiation5, radiation6, radiation7, radiation8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date5, prob5, alert5, value5, maxi5, mini5 = calendar.DATA_cfs_calendar(humidity1, humidity2, humidity3, humidity4, humidity5, humidity6, humidity7, humidity8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)

	elif model == "card":
		date1, prob1, alert1, value1, maxi1, mini1, i = card.DATA_cfs_card(rain1, rain2, rain3, rain4, rain5, rain6, rain7, rain8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date2, prob2, alert2, value2, maxi2, mini2, i = card.DATA_cfs_card(speed1, speed2, speed3, speed4, speed5, speed6, speed7, speed8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date3, prob3, alert3, value3, maxi3, mini3, i = card.DATA_cfs_card(temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, temperature7, temperature8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date4, prob4, alert4, value4, maxi4, mini4, i = card.DATA_cfs_card(radiation1, radiation2, radiation3, radiation4, radiation5, radiation6, radiation7, radiation8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		date5, prob5, alert5, value5, maxi5, mini5, i = card.DATA_cfs_card(humidity1, humidity2, humidity3, humidity4, humidity5, humidity6, humidity7, humidity8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)

	else:
		success, dic = json_output._get_ERROR(var_id, model) 

	date	= [date1, date2, date3, date4, date5]
	prob	= [prob1, prob2, prob3, prob4, prob5]
	alert	= [alert1, alert2, alert3, alert4, alert5]
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
	if unit  == "imperial":
		value, cur = units._get_imperial(value, var_id)
	else:
		value, cur = units._get_metric(value, var_id)

	alert = color._get_ALERT(alert)
	color = color._get_CFS(prob)
	success, dic = json_output._get_OUT(date, prob, alert, color, value, maxi, mini, model, var_id, cur)
	print "Content-type: application/json\n\n"
	print json.dumps(dic)
	exit(0)
