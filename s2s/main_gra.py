#!/usr/bin/env python
#-*- coding:utf-8 -*-
import cgi
import datetime
import io
import base64
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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
var 	= form.getvalue("var")	
unit 	= form.getvalue("unit")
model 	= form.getvalue("model")
#######################################
##Form treatment
#ip  	= os.environ["REMOTE_ADDR"]
lat0	= float(lat)
lon0	= float(lon)
grid = grid_select._get_GRID(lat0, lon0, 'GFS')
try:
	utc 	= form.getvalue("utc")	
	utc0	= int(utc)
except:
	utc0 = astro_tz._get_timezone(lat0, lon0)
###############################################################################
## get files, lat_lon, id and limits
ens1, ens2, date0 = gfs_var._get_FILE(grid)
ix_gfs, iy_gfs = lat_lon.GFS_grab(ens1, lat0, lon0)
var_id = gfs_var._get_ID(var)
PRO, TOP, BOT = gfs_var._get_LIM(var)
success = True
###############################################################################
if var_id == 1 :
	var_raw1 = gfs_var._get_rain(var, ens1)
	var_raw2 = gfs_var._get_rain(var, ens2)	
	time  	 = gfs_var._get_time('time', ens1)
	date, prob, alert, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	maxi_i,	date_i = interpol._get_gfs_days(maxi, date)
	mini_i,	date_i = interpol._get_gfs_days(mini, date)
	value_i,	date_i = interpol._get_gfs_days(value, date)

elif var_id == 2:
	var_rawa1, var_rawb1 = gfs_var._get_wind(var, ens1)
	var_rawa2, var_rawb2 = gfs_var._get_wind(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	date, prob, alert, value2, maxi, mini = table.DATA_gfs_table(var_rawb2, var_rawb2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)    
	date, prob, alert, value1, maxi, mini = table.DATA_gfs_table(var_rawa1, var_rawa2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	maxi_i,	date_i = interpol._get_gfs_days(maxi, date)
	mini_i,	date_i = interpol._get_gfs_days(mini, date)
	value_i, date_i = interpol._get_gfs_days(value1, date)
	value_i2, date_i2 = interpol._get_gfs_days(value2, date)

elif var_id == 3:
	var_raw1 = gfs_var._get_temperature(var, ens1)
	var_raw2 = gfs_var._get_temperature(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	date, prob, alert, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	maxi_i,	date_i = interpol._get_gfs_days(maxi, date)
	mini_i,	date_i = interpol._get_gfs_days(mini, date)
	value_i, date_i = interpol._get_gfs_days(value, date)

elif var_id == 4:
	var_raw1 = gfs_var._get_radiation(var, ens1)
	var_raw2 = gfs_var._get_radiation(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	date, prob, alert, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	maxi_i,	date_i = interpol._get_gfs_days(maxi, date)
	mini_i,	date_i = interpol._get_gfs_days(mini, date)
	value_i, date_i = interpol._get_gfs_days(value, date)

elif var_id == 5:
	var_raw1 = gfs_var._get_humidity(var, ens1)
	var_raw2 = gfs_var._get_humidity(var, ens2)
	time  	 = gfs_var._get_time('time', ens1)
	date, prob, alert, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	maxi_i,	date_i = interpol._get_gfs_days(maxi, date)
	mini_i,	date_i = interpol._get_gfs_days(mini, date)
	value_i, date_i = interpol._get_gfs_days(value, date)

else:
	time  	 = gfs_var._get_time('time', ens1)
	clou1, pres1, temp1, humi1, rain1, wind1, direction1, dew1, cape1, gust1 = gfs_var._get_meteo('meteo', ens1)
	clou2, pres2, temp2, humi2, rain2, wind2, direction2, dew2, cape2, gust2 = gfs_var._get_meteo('meteo', ens2)


def titulo(var1):
	return {
		'chuva'		: 'Chuva acumulada (mm)',
		'temp'		: 'Temperatura (C)',
		'radiacao'	: 'Radiacao  (w/m2)',
		'umidade'	: 'Umidade relativa (%)',
		'vento'		: 'Velocidade do Vento (m/s)'
		}.get(var1, 'Null')


def label_y(var1):
	return {
		'chuva'		: 'mm',
		'temperatura'	: 'C',
		'radiacao'	: 'w/m2',
		'umidade'	: '%',
		'vento'		: 'm/s'
		}.get(var1, 'Null')
lim_yt = (max(value_i) + 1)
lim_yb = (min(value_i) - 1)
# lim_yt = (max(maxi) + 1)
# lim_yb = (min(mini) - 1)
lim_x = (len(date) - 1)
index = np.arange(len(date))
index_i = np.arange(len(date_i))
index_o = np.arange(len(time))
plt.figure(var, figsize=(9, 6))
plt.title(titulo(var))
plt.ylabel(label_y(var))
plt.plot(index, value, color='black', label="S2S")
# plt.plot(index, maxi_i, '-', color='darkblue')
# plt.plot(index, mini_i, '-', color='darkgreen')
# plt.plot(index, maxi, color='blue' )
# plt.plot(index, mini, color='green')
plt.plot(index_i, value_i, color='green', label="S2S inter")
try:
	plt.plot(index_o, var_raw1, color='blue', label="Modelo")
except:
	plt.plot(index_o, var_rawa1, color='blue', label="Modelo")
plt.ylim(lim_yb, lim_yt)
plt.xlim(0, lim_x)
plt.legend(loc='lower right')

buf = io.BytesIO()   
plt.savefig(buf, dpi=200, format='png')
print """Content-type: text/html\n\n
        <html>
        <title>Tempo Ok! %s </title>
        <body>
        <img src="data:image/png;base64,%s"/>
        </body></html>"""  % (var, base64.encodestring(buf.getvalue()))

buf.close()
exit(0)
