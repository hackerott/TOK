#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cgi
import datetime
import json
import numpy as np
#######################################
# S2S imports
import cfs_var
import lat_lon
import scalendar
import card
import prob_area
import prob_time
import json_output
import astro_tz
import cond_figures
import units
import colors
import gcard
import grid_select
# import meteogram
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
lat0	= float(lat)
lon0	= float(lon)
grid = grid_select._get_GRID(lat0, lon0, 'CFS')
try:
	utc 	= form.getvalue("utc")	
	utc0	= int(utc)
except:
	utc0 = astro_tz._get_timezone(lat0, lon0)
#######################################
## get files, lat_lon, id and limits
ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, date0 = cfs_var._get_FILE(grid)
ix_cfs, iy_cfs = lat_lon.CFS_grab(ens1, lat0, lon0)
var_id = cfs_var._get_ID(var)
PRO, TOP, BOT = cfs_var._get_LIM(var)
success = True
#######################################
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
		date, prob, alert, value, maxi, mini = scalendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_cfs_gcard(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
	else:
		success = json_output._get_ERROR(var_id, model) 

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
		date, prob, alert, value, maxi, mini = scalendar.DATA_cfs_calendar(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
		for i in range(0, len(value)):
			value[i] = [value[i], int(var_rawb1[i, ix_cfs, iy_cfs])]
		value = np.array(value)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
		value = [value, int(var_rawb1[i, ix_cfs, iy_cfs])]
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_cfs_gcard(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
	else:
		success = json_output._get_ERROR(var_id, model) 

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
		date, prob, alert, value, maxi, mini = scalendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_cfs_gcard(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
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
		date, prob, alert, value, maxi, mini = scalendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_cfs_gcard(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
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
		date, prob, alert, value, maxi, mini = scalendar.DATA_cfs_calendar(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
	elif model == "card":
		date, prob, alert, value, maxi, mini, i = card.DATA_cfs_card(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)	
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_cfs_gcard(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
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
		date, prob, alert, value1, maxi, mini = scalendar.DATA_cfs_calendar(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, 0.75, 0.25, 0.5, var_id)
		date, prob, alert, value2, maxi, mini = scalendar.DATA_cfs_calendar(var_rawb1, var_rawb2, var_rawb3, var_rawb4, var_rawb5, var_rawb6, var_rawb7, var_rawb8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
		sunset, sunrise = astro_tz._get_sun(lat0, lon0, utc0)
		value = cond_figures.DATA_cond_figure(value1, value2, date, sunset, sunrise)
	elif model == "card":
		date, prob, alert, value1, maxi, mini, i = card.DATA_cfs_card(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, 0.75, 0.25, 0.5)
		date, prob, alert, value2, maxi, mini, i = card.DATA_cfs_card(var_rawb1, var_rawb2, var_rawb3, var_rawb4, var_rawb5, var_rawb6, var_rawb7, var_rawb8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO)
		sunset, sunrise = astro_tz._get_sun(lat0, lon0, utc0)
		value = cond_figures.DATA_cond_figure(value1, value2, date, sunset, sunrise)
	elif model == "gcard":
		date, prob, alert, value1, maxi, mini = gcard.DATA_cfs_gcard(var_rawa1, var_rawa2, var_rawa3, var_rawa4, var_rawa5, var_rawa6, var_rawa7, var_rawa8, time, ix_cfs, iy_cfs, date0, utc0, 0.75, 0.25, 0.5, var_id)
		date, prob, alert, value2, maxi, mini = gcard.DATA_cfs_gcard(var_rawb1, var_rawb2, var_rawb3, var_rawb4, var_rawb5, var_rawb6, var_rawb7, var_rawb8, time, ix_cfs, iy_cfs, date0, utc0, TOP, BOT, PRO, var_id)
		sunset, sunrise = astro_tz._get_sun(lat0, lon0, utc0)
		value = cond_figures.DATA_cond_figure(value1, value2, date, sunset, sunrise)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 
else:
	success, dic = json_output._get_ERROR(var_id, model)

if success == False:
	print "Content-type: application/json\n\n"
	print json.dumps(dic)
	exit(1)

else:
	print "Content-type: application/json\n\n"
	if unit  == "imperial":
		value, cur = units._get_imperial(value, var_id)
		maxi, cur = units._get_imperial(maxi, var_id)
		mini, cur = units._get_imperial(mini, var_id)
	else:
		value, cur = units._get_metric(value, var_id)
		maxi, cur = units._get_metric(maxi, var_id)
		mini, cur = units._get_metric(mini, var_id)
	alert = colors._get_ALERT(alert)
	color = colors._get_CFS(prob)
	success, dic = json_output._get_OUT(date, prob, alert, color, value, maxi, mini, model, var_id, cur)
	print json.dumps(dic)
	exit(0)