#!/usr/bin/env python
#-*- coding:utf-8 -*-
import cgi
import datetime
import json
import numpy as np

#######################################
# S2S imports
import wrf_var
import grid_select
import lat_lon
import scalendar
import card
import table
import prob_area
import prob_time
import json_output
import astro_tz
import cond_figures
import units
import colors
import meteogram
import gcard
import interpol
import grid_select
#######################################
##	GET form			
form = cgi.FieldStorage()
					
lat 	= form.getvalue("lat")	
lon 	= form.getvalue("lon")	
#utc 	= form.getvalue("utc")	
var 	= form.getvalue("var")	
unit 	= form.getvalue("unit")
model 	= form.getvalue("model")
#######################################
##Form treatment
#ip  	= os.environ["REMOTE_ADDR"]
lat0	= float(lat)
lon0	= float(lon)
grid = grid_select._get_GRID(lat0, lon0, 'WRF')
try:
	utc 	= form.getvalue("utc")	
	utc0	= int(utc)
except:
	utc0 = astro_tz._get_timezone(lat0, lon0)
#######################################
## get files, lat_lon, id and limits
ens1, ens2, date0 = wrf_var._get_FILE(grid)
ix_wrf, iy_wrf = lat_lon.WRF_grab(ens1, lat0, lon0)
var_id = wrf_var._get_ID(var)
PRO, TOP, BOT = wrf_var._get_LIM(var)
success = True
###############################################################################
##
if var_id == 1 :
	var_raw1 = wrf_var._get_rain(var, ens1)
	var_raw2 = wrf_var._get_rain(var, ens2)	
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, alert, value, maxi, mini = scalendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	elif model == "card":
		date, prob, alert, value, maxi, mini, c = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, alert, value, maxi, mini = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_wrf_gcard(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 
	value, date = interpol._get_wrf_days(value, date)

elif var_id == 2:
	var_rawa1, var_rawb1 = wrf_var._get_wind(var, ens1)
	var_rawa2, var_rawb2 = wrf_var._get_wind(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, alert, value, maxi, mini = scalendar.DATA_wrf_calendar(var_rawa1, var_rawa2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
		value1, date = interpol._get_wrf_days(value, date)
		value2, date = interpol._get_wrf_days(var_rawb1[:, ix_wrf, iy_wrf], date)
		for i in range(0, min(len(value1), len(value2))):
			value[i] = [value1[i], value2[i]]
		value = np.array(value)
	elif model == "card":
		date, prob, alert, value, maxi, mini, c = card.DATA_wrf_card(var_rawa1, var_rawa2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
		value = [value, int(var_rawb1[c, ix_wrf, iy_wrf])]
	elif model == "table":
		date, prob, alert, value, maxi, mini = table.DATA_wrf_table(var_rawa1, var_rawa2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
		value1, date = interpol._get_wrf_days(value, date)
		value2, date = interpol._get_wrf_days(var_rawb1[:, ix_wrf, iy_wrf], date)
		for i in range(0, min(len(value1), len(value2))):
			value[i] = [value1[i], value2[i]]
		value = np.array(value)
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_wrf_gcard(var_rawa1, var_rawa2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

elif var_id == 3:
	var_raw1 = wrf_var._get_temperature(var, ens1)
	var_raw2 = wrf_var._get_temperature(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, alert, value, maxi, mini = scalendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
		value, date = interpol._get_wrf_days(value, date)
	elif model == "card":
		date, prob, alert, value, maxi, mini, c = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
		value, date = interpol._get_wrf_days(value, date)
	elif model == "table":
		date, prob, alert, value, maxi, mini = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
		value, date = interpol._get_wrf_days(value, date)
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_wrf_gcard(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 

elif var_id == 4:
	var_raw1 = wrf_var._get_radiation(var, ens1)
	var_raw2 = wrf_var._get_radiation(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, alert, value, maxi, mini = scalendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	elif model == "card":
		date, prob, alert, value, maxi, mini, c = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, alert, value, maxi, mini = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_wrf_gcard(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 
	value, date = interpol._get_wrf_days(value, date)

elif var_id == 5:
	var_raw1 = wrf_var._get_humidity(var, ens1)
	var_raw2 = wrf_var._get_humidity(var, ens2)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, alert, value, maxi, mini = scalendar.DATA_wrf_calendar(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	elif model == "card":
		date, prob, alert, value, maxi, mini, c = card.DATA_wrf_card(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, alert, value, maxi, mini = table.DATA_wrf_table(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "gcard":
		date, prob, alert, value, maxi, mini = gcard.DATA_wrf_gcard(var_raw1, var_raw2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 
	value, date = interpol._get_wrf_days(value, date)

elif var_id == 6:
	var_rawa1, var_rawb1 = wrf_var._get_figure(var, ens1, ix_wrf, iy_wrf)
	var_rawa2, var_rawb2 = wrf_var._get_figure(var, ens2, ix_wrf, iy_wrf)
	time  	 = wrf_var._get_time('time', ens1)
	if model == "calendar":
		date, prob, alert, value1, maxi, mini = scalendar.DATA_wrf_calendar(var_rawa1, var_rawa2, time, ix_wrf, iy_wrf, date0, utc0, 0.75, 0.25, 0.5, var_id)
		date, prob, alert, value2, maxi, mini = scalendar.DATA_wrf_calendar(var_rawb1, var_rawb2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	elif model == "card":
		date, prob, alert, value1, maxi, mini, c = card.DATA_wrf_card(var_rawa1, var_rawa2, time, ix_wrf, iy_wrf, date0, utc0, 0.75, 0.25, 0.5)	
		date, prob, alert, value2, maxi, mini, c = card.DATA_wrf_card(var_rawb1, var_rawb2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)	
	elif model == "table":
		date, prob, alert, value1, maxi, mini = table.DATA_wrf_table(var_rawa1, var_rawa2, time, ix_wrf, iy_wrf, date0, utc0, 0.75, 0.25, 0.5)
		date, prob, alert, value2, maxi, mini = table.DATA_wrf_table(var_rawb1, var_rawb2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO)
	elif model == "gcard":
		date, prob, alert, value1, maxi, mini = gcard.DATA_wrf_gcard(var_rawa1, var_rawa2, time, ix_wrf, iy_wrf, date0, utc0, 0.75, 0.25, 0.5, var_id)
		date, prob, alert, value2, maxi, mini = gcard.DATA_wrf_gcard(var_rawb1, var_rawb2, time, ix_wrf, iy_wrf, date0, utc0, TOP, BOT, PRO, var_id)
	else:
		success, dic = json_output._get_ERROR(var_id, model) 
	value1, date = interpol._get_wrf_days(value1, date)
	value2, date = interpol._get_wrf_days(value2, date)
	sunset, sunrise = astro_tz._get_sun(lat0, lon0, utc0)
	value = cond_figures.DATA_cond_figure(value1, value2, date, sunset, sunrise)

else:
	if model == "meteo":
		time  	 = wrf_var._get_time('time', ens1)
		clou1, pres1, temp1, humi1, rain1, wind1, direction1, dew1, cape1, gust1 = wrf_var._get_meteo('meteo', ens1, ix_wrf, iy_wrf)
		clou2, pres2, temp2, humi2, rain2, wind2, direction2, dew2, cape2, gust2 = wrf_var._get_meteo('meteo', ens2, ix_wrf, iy_wrf)
		date, prob, alert, value, maxi, mini = meteogram.DATA_wrf_meteo(temp1, temp2, wind1, wind2, humi1, humi2, clou1, clou2,
														 rain1, rain2, pres1, pres2, cape1, cape2, dew1, dew2, time, ix_wrf, iy_wrf, date0, utc0, 12)
	else:
		success, dic = json_output._get_ERROR(var_id, model)

if success == False:
	print "Content-type: application/json\n\n"
	print json.dumps(dic)
	exit(1)

else:
	if unit  == "imperial":
		value, cur = units._get_imperial(value, var_id)
		maxi, cur = units._get_imperial(maxi, var_id)
		mini, cur = units._get_imperial(mini, var_id)
	else:
		value, cur = units._get_metric(value, var_id)
		maxi, cur = units._get_metric(maxi, var_id)
		mini, cur = units._get_metric(mini, var_id)

	alert = colors._get_ALERT(alert)
	color = colors._get_WRF(prob)
	success, dic = json_output._get_OUT(date, prob, alert, color, value, maxi, mini, model, var_id, cur)
	print "Content-type: application/json\n\n"
	print json.dumps(dic)
	exit(0)
