#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cgi
import datetime

#######################################
# S2S imports
import var_wrf
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

#######################################
##Form treatment
#ip  	= os.environ["REMOTE_ADDR"]
date0	= datetime.datetime.strptime(date, '%Y%m%d')
date1	= date0 - datetime.timedelta(hours =12)
lat0	= float(lat)
lon0	= float(lon)
utc0	= int(utc)

#######################################
## get files, lat_lon, id and limits
ens1, ens2 = wrf_var._get_FILE(date0, date1)
ix_wrf, iy_wrf = lat_lon.wrf_grab(ens1, lat, lon)
var_id = wrf_var._get_ID(var)
PRO, TOP, BOT = wrf_var._get_LIM(var)

###############################################################################
##
if var_id == 1 :
	var_raw1 = wrf_var._get_rain(var, ens1)
	var_raw2 = wrf_var._get_rain(var, ens2)	
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value, maxi, mini, fig = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 2:
	var_rawa1, var_rawb1 = wrf_var._get_wind(var, ens1)
	var_rawa2, var_rawb2 = wrf_var._get_wind(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		for i in range(0, len(value)):
			value[i] = value[i], var_rawb1[i, ix_wrf, iy_wrf]
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
		for i in range(0, len(value)):
			value[i] = value[i], var_rawb1[i, ix_wrf, iy_wrf]
	elif model == "table":
		date, prob, color, value, maxi, mini, fig = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
		for i in range(0, len(value)):
			value[i] = value[i], var_rawb1[i, ix_wrf, iy_wrf]
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 3:
	var_raw1 = wrf_var._get_temperature(var, ens1)
	var_raw2 = wrf_var._get_temperature(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value, maxi, mini, fig = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 4:
	var_raw1 = wrf_var._get_radiation(var, ens1)
	var_raw2 = wrf_var._get_radiation(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value, maxi, mini, fig = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 5:
	var_raw1 = wrf_var._get_humidity(var, ens1)
	var_raw2 = wrf_var._get_humidity(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, color, value, maxi, mini, fig = calendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
	elif model == "card":
		date, prob, color, value, maxi, mini, fig = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, color, value, maxi, mini, fig = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	else:
		success = json_out._get_ERROR(var_id, model) 
		exit(1)

elif var_id == 6:
	rain1, speed1, direction1, radiation1, temperature1, humidity1 = wrf_var._get_all(var, ens1)
	rain2, speed2, direction2, radiation2, temperature2, humidity2 = wrf_var._get_all(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date1, prob1, color1, value1, maxi1, mini1, fig1 = calendar.DATA_wrf_calendar(rain1, rain2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date2, prob2, color2, value2, maxi2, mini2, fig2 = calendar.DATA_wrf_calendar(speed1, speed2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date3, prob3, color3, value3, maxi3, mini3, fig3 = calendar.DATA_wrf_calendar(temperature1, temperature2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date4, prob4, color4, value4, maxi4, mini4, fig4 = calendar.DATA_wrf_calendar(radiation1, radiation2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date5, prob5, color5, value5, maxi5, mini5, fig5 = calendar.DATA_wrf_calendar(humidity1, humidity2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)

	elif model == "card":
		date1, prob1, color1, value1, maxi1, mini1, fig1 = card.DATA_wrf_card(rain1, rain2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date2, prob2, color2, value2, maxi2, mini2, fig2 = card.DATA_wrf_card(speed1, speed2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date3, prob3, color3, value3, maxi3, mini3, fig3 = card.DATA_wrf_card(temperature1, temperature2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date4, prob4, color4, value4, maxi4, mini4, fig4 = card.DATA_wrf_card(radiation1, radiation2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date5, prob5, color5, value5, maxi5, mini5, fig5 = card.DATA_wrf_card(humidity1, humidity2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)

	elif model == "table":
		date1, prob1, color1, value1, maxi1, mini1, fig1 = table.DATA_wrf_table(rain1, rain2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date2, prob2, color2, value2, maxi2, mini2, fig2 = table.DATA_wrf_table(speed1, speed2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date3, prob3, color3, value3, maxi3, mini3, fig3 = table.DATA_wrf_table(temperature1, temperature2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date4, prob4, color4, value4, maxi4, mini4, fig4 = table.DATA_wrf_table(radiation1, radiation2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
		date5, prob5, color5, value5, maxi5, mini5, fig5 = table.DATA_wrf_table(humidity1, humidity2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)

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