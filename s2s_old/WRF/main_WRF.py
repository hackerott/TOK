#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import math
import sys
import cgi
import cgitb
import os
import calendar
import datetime
import json
import base64

import lat_lon
import variables
import mysql_access

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

#########################################
##      Reading form                    #
                                        #
form = cgi.FieldStorage()               #
                                        #
lat1 = form.getvalue("lat")             #
lon1 = form.getvalue("lon")             #
utc1 = form.getvalue("utc")             #
var1 = form.getvalue("var")             #
date1 = form.getvalue("data")           #
type1 = form.getvalue("tipo")           #
token1 = form.getvalue("token")         #
id1 = form.getvalue("id")               #
ip1  = os.environ["REMOTE_ADDR"]        #
                                        #
#########################################
#########################################################
##	init vars   					#
date0 = datetime.datetime.strptime(date1, '%Y%m%d')	#
lat0 = float(lat1)					#
lon0 = float(lon1)					#
utc0 = int(utc1)					#
#########################################################
#################################################################################################
##		output jason									#
												#
def json_out (day, color, val1, val2, var1, maxx, token_new):					#
	output = np.empty((maxx+1,1))								#
	for i in range(iz, maxx):								#
		if val2==0:									#
			output[i] = var1, day[i], color[i], val1[i], token_new			#
		else:										#
			output[i] = var1, day[i], color[i], val1[i], val2[i], token_new		#
												#
	return(output)										#
												#
#################################################################################################
###########################################################################################################################
##	Calendar
def table_out (WRF_nc, var1, iz, ixWRF, iyWRF, date0, utc0, token_new):
	WRFfile = netCDF4.Dataset(WRF_nc, 'r')
	if var1 == 'wind':
		dia, color, val_max, dire, maxx = variables.wind.calendar(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val_max, dire, var1, maxx, token_new)
	elif var1 == 'temperature' :
		dia, color, val_min, val_max, maxx = variables.temperature.calendar(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val_max, val_min, var1, maxx, token_new)
	elif var1 == 'humidity' :
		dia, color, val_min, maxx = variables.humidity.calendar(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
 		output = json_out(dia, color, val_min, 0, var1, maxx, token_new)
	elif var1 == 'rain' :	
		dia, color, val, maxx = variables.rain.calendar(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val, 0, var1, maxx, token_new)
	elif var1 == 'radiation' :
		dia, color, val, maxx = variables.radiation.calendar(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val, 0, var1, maxx, token_new)
	return(output)
###########################################################################################################################
##	table
def table_out (WRF_nc, var1, iz, ixWRF, iyWRF, date0, utc0, token_new):
	WRFfile = netCDF4.Dataset(WRF_nc, 'r')
	if var1 == 'wind':
		dia, color, val, dire, maxx = variables.wind.table(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val_max, dire, var1, maxx, token_new)
	elif var1 == 'temperature' :
		dia, color, val, maxx = variables.temperature.table(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val, 0, var1, maxx, token_new)
	elif var1 == 'humidity' :
		dia, color, val, maxx = variables.humidity.table(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val, 0, var1, maxx, token_new)
	elif var1 == 'rain' :	
		dia, color, val, maxx = variables.rain.table(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val, 0, var1, maxx, token_new)
	elif var1 == 'radiation' :
		dia, color, val, maxx = variables.radiation.table(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		output = json_out(dia, color, val, 0, var1, maxx, token_new)
	return(output)
###########################################################################################################################

#########################################################################################
##	Check the request token and id							#
token_db, id_db = mysql_access.token_get(id1)						#
if token1 != token_db or id1 != id_db :							#
	type1 == error									#
	date_error = datetime.datetime.now()						#
	print >> error.log, "%s tried to access the API WRF, %s" % (ip1, date_error)	#
#########################################################################################
#########################################################################################
##	Generates new token and store							#
	hash0 = os.urandom(16)								#
	hash1 = base64.b64encode(hash0).decode('utf-8')					#
	token_status = mysql_access.token_update(hash1, id1)				#
	if token_status != true:							#
		date_error = datetime.datetime.now()					#
		token_new = token1							#
		print >> error.log, "Token update failed, %s" (date_error)		#
 	else:										#
		token_new = hash1							#
#########################################################################################
#########################################################################################
##	Check if .nc file exists							#
											#
file_name = "/var/www/html/processamento/WRFD20101"+date1+"00.nc"			#
file_name1 = file_name									#
while os.path.isfile(file_name) != True:						#
		date1 = date1 + datetime.timedelta(days = -1)				#
		file_name = "/var/www/html/processamento/WRFD20101"+date1+"00.nc"	#	
		iz += 24								#
		brk +=1									#
		if brk == 3:								#
			file_name = False						#
			break								#
#########################################################################################
#################################################
if file_name != False:				#
	WRF_nc = file_name			#	
	WRFfile = netCDF4.Dataset(WRF_nc, 'r')	#
	latWRF = WRFfile.variables['XLAT']	#	
	lonWRF = WRFfile.variables['XLONG']	#
#################################################
#################################################################################
##	find lat and lon							#	
	izWRF, ixWRF, iyWRF = lat_lon.WRF_get(latWRF, lonWRF, lat0, lon0)	#
#################################################################################
#########################################################################################################
##	separate and call										#
	if type1 == True:										#
		output = calendar_out(WRF_nc, var1, iz, ixWRF, iyWRF, date0, utc0, token_new)		#
		print json.dumps(output)								#
	elif type1 == False:										#
		output = table_out(WRF_nc, var1, iz, ixWRF, iyWRF, date0, utc0, token_new)		#
		print json.dumps(output)								#
##	Erro de login											#
	elif type1 == Error:										#
		print json.dumps(""" Authentication error """)						#
#########################################################################################################
#########################################################################################
else:											#
	date_error = datetime.datetime.now()						#
	print >> error.log, "%s file does not exist %s" % (date_error, file_name1)	#	
	print json.dumps(""" Error model unavailable """)				#
	exit()										#
#########################################################################################
#################################
##	Save the generated token#
token = open('token', 'r+')	#
token.write(hash1)		#
token.close()			#
#################################
