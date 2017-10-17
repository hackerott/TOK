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

from scipy import polyfit, polyval
#######################################
# S2S imports
import gfs_var
import cfs_var
import lat_lon
import grid_select
import astro_tz
import prob_area
import prob_time
import table
import interpol
import ridge
# import calendar
# import card
# import json_output
# import cond_figures
# import units
# import colors
# import meteogram
# import gcard
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
g_ens1, g_ens2, date0 = gfs_var._get_FILE(grid)
c_ens1, c_ens2, c_ens3, c_ens4, c_ens5, c_ens6, c_ens7, c_ens8, date1 = cfs_var._get_FILE(grid)
ix_gfs, iy_gfs = lat_lon.GFS_grab(g_ens1, lat0, lon0)
ix_cfs, iy_cfs = lat_lon.GFS_grab(c_ens1, lat0, lon0)
var_id = gfs_var._get_ID(var)
PRO, TOP, BOT = gfs_var._get_LIM(var)
success = True
###############################################################################
##Rain
if var_id == 1 :
	var_raw1 = gfs_var._get_rain(var, g_ens1)
	var_raw2 = gfs_var._get_rain(var, g_ens2)	
	time  	 = gfs_var._get_time('time', g_ens1)
	g_date, prob, alert, g_value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	var_raw1 = cfs_var._get_rain(var, c_ens1)
	var_raw2 = cfs_var._get_rain(var, c_ens2)	
	var_raw3 = cfs_var._get_rain(var, c_ens3)
	var_raw4 = cfs_var._get_rain(var, c_ens4)
	var_raw5 = cfs_var._get_rain(var, c_ens5)
	var_raw6 = cfs_var._get_rain(var, c_ens6)
	var_raw7 = cfs_var._get_rain(var, c_ens7)
	var_raw8 = cfs_var._get_rain(var, c_ens8)
	time  	 = cfs_var._get_time('time', c_ens1)
	c_date, prob, alert, c_value, maxi, mini = table.DATA_cfs_table(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date1, utc0, TOP, BOT, PRO, var_id)
	del prob, alert, maxi, mini
	del var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time
##Temperature
elif var_id == 3:
	var_raw1 = gfs_var._get_temperature(var, g_ens1)
	var_raw2 = gfs_var._get_temperature(var, g_ens2)
	time  	 = gfs_var._get_time('time', g_ens1)
	date, prob, alert, value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	g_date, prob, alert, g_value, maxi, mini = table.DATA_gfs_table(var_raw1, var_raw2, time, ix_gfs, iy_gfs, date0, utc0, TOP, BOT, PRO)
	var_raw1 = cfs_var._get_temperature(var, c_ens1)
	var_raw2 = cfs_var._get_temperature(var, c_ens2)	
	var_raw3 = cfs_var._get_temperature(var, c_ens3)
	var_raw4 = cfs_var._get_temperature(var, c_ens4)
	var_raw5 = cfs_var._get_temperature(var, c_ens5)
	var_raw6 = cfs_var._get_temperature(var, c_ens6)
	var_raw7 = cfs_var._get_temperature(var, c_ens7)
	var_raw8 = cfs_var._get_temperature(var, c_ens8)
	time  	 = cfs_var._get_time('time', c_ens1)
	c_date, prob, alert, c_value, maxi, mini = table.DATA_cfs_table(var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time, ix_cfs, iy_cfs, date1, utc0, TOP, BOT, PRO, var_id)
	del prob, alert, maxi, mini
	del var_raw1, var_raw2, var_raw3, var_raw4, var_raw5, var_raw6, var_raw7, var_raw8, time

g_value, g_date = interpol._get_gfs_days(g_value, g_date)
###############################################################################
'''
Creates the raw series, concataneting gfs and cfs time series
'''
date_raw	= []
value_raw	= []
for i in range(0, len(g_date)+len(c_date)):
	if i < len(g_date):
		value_raw.append(g_value[i])
		date_raw.append(g_date[i])
	else:
		value_raw.append(c_value[(i-len(g_date))])
		date_raw.append(c_date[(i-len(g_date))])

series_x = np.arange(len(date_raw))
for i in range(0, len(series_x)):
	d = date_raw[i] - date_raw[0]
	series_x[i] = d.days*24 + d.seconds//3600

###############################################################################
'''
Creates days mean(temp) and accumulated(rain)
'''
date_mean    = []
value_mean   = []
a = 0
b = 24
c = 0
d = 4
for i in range(0, len(g_date)+len(c_date)):
	if var_id == 3:
		if b <= (len(g_date)-24):
			value_mean.append(np.nanmean(g_value[a:b]))
			date_mean.append(g_date[b])
			a += 24
			b += 24
		else:
			value_mean.append(np.nanmean(c_value[c:d]))
			date_mean.append(c_date[d])
			c += 4
			d += 4
			if d >= len(c_date):
				break
	else:
		if b <= (len(g_date)-24):
			value_mean.append(np.nansum(g_value[a:b]))
			date_mean.append(g_date[b])
			a += 24
			b += 24
		else:
			value_mean.append(np.nansum(c_value[c:d]))
			date_mean.append(c_date[d])
			c += 4
			d += 4
			if d >= len(c_date):
				break
mean_x = np.arange(len(date_mean))
for i in range(0, len(mean_x)):
	d = date[i] - date[0]
	mean_x[i] = d.days*24 + d.seconds//3600

###############################################################################
'''
Creates polinomial model
'''
value_pol = polyfit(series_x, value_raw, 99) #100 is the limit without blowing memory
pol = np.poly1d(value_pol)
level = pol.order
value_pol = polyval(value_pol, series_x)
##Forecast
fore_pol_x = np.arange(mean_x[-1]//2, (240+mean_x[-1]), 6)
fore_pol = pol(fore_pol_x)

###############################################################################
'''
Creates ridge model
'''
rid = ridge.RidgeRegressor()
rid.fit(series_x, value_raw)
fore_rid = rid.predict(fore_pol_x)

###############################################################################
'''
Plots
'''
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

lim_yt = (max(value) + 1)
lim_yb = (min(value) - 1)
lim_x = (series_x[-1] - 1)
index = series_x   
indexM = mean_x
plt.figure(var, figsize=(9, 6))
plt.title(titulo(var))
plt.ylabel(label_y(var))
plt.plot(mean_x[:-2], value[:-2], color='black', label='Data')   
plt.scatter(mean_x[:-2], value[:-2], color='black')
#plt.plot(series_x[:len(series_x)//1.25], value_pol[:len(series_x)//1.25], color='red')
plt.scatter(fore_pol_x, fore_pol, color='green')
plt.plot(fore_pol_x, fore_pol, color='green', label='Poly Forecast')
plt.scatter(fore_pol_x, fore_rid, color='blue')
plt.plot(fore_pol_x, fore_rid, color='blue', label='Ridge Forecast')

plt.ylim(lim_yb, lim_yt)
plt.xlim(0, lim_x)
plt.xlabel(level)
plt.legend()
buf = io.BytesIO()   
plt.savefig(buf, dpi=200, format='png')
###############################################################################
'''
Create a html page with plot image
'''
print """Content-type: text/html\n\n
        <html>
        <title>Tempo Ok! %s </title>
        <body>
        <img src="data:image/png;base64,%s"/>
        </body></html>"""  % (var, base64.encodestring(buf.getvalue()))

buf.close()
exit(0)