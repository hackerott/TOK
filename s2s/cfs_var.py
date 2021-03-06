#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import os
import datetime

#######################################
## return the nc var_names for each variable
def _get_NCVAR(var):
	return {
		'chuva'		: 'pratesfc',
		'vento'		: ['ugrd10m', 'vgrd10m'],
		'temp'		: 'tmp2m',
		'radiacao'	: 'dswrfsfc',
		'umidade'	: ['spfh2m', 'tmp2m', 'pressfc'], 
		'figura'	: ['tcdcclm', 'pratesfc'],
		'time'		: 'time',
		'rigning'	: 'pratesfc',
		'vindur'	: ['ugrd10m', 'vgrd10m'],
		'hitastig'	: 'tmp2m',
		'geislun'	: 'dswrfsfc',
		'raki'		: ['spfh2m', 'tmp2m', 'pressfc'],
		'mynd'		: ['tcdcclm', 'pratesfc'],
		'rain'		: 'pratesfc',
		'wind'		: ['ugrd10m', 'vgrd10m'],
		'temperature': 'tmp2m',
		'radiation'	: 'dswrfsfc',
		'humidity'	: ['spfh2m', 'tmp2m', 'pressfc'],
		'figure'	: ['tcdcclm', 'pratesfc'],
		}.get(var, 'Null')
#######################################
## return ID for each var
def _get_ID(var):
	return {
		'chuva'		: 1,
		'vento'		: 2,
		'temp'		: 3,
		'radiacao'	: 4,
		'umidade'	: 5, 
		'figura'	: 6,  
		'all'		: 7,
		'rigning'	: 1,
		"vindur"	: 2,
		'hitastig'	: 3,
		"geislun"	: 4,
		'raki'		: 5,
		'mynd'		: 6,
		'allt'		: 7,
		'rain'		: 1,
		'wind'		: 2,
		'temperature': 3,
		'radiation'	: 4,
		'humidity'	: 5,
		'figure'	: 6
		}.get(var, 'Null')
#######################################
## return limits for each var 
def _get_LIM(var):
	DIC = {
		'chuva'		: [0.4, 10, 0.5],
		'figura'	: [0.4, 10, 0.5],
		'vento'		: [0.4, 7, 2],
		'temp'		: [0.4, 27, 20],
		'radiacao'	: [0.4, 1400, 800],
		'umidade'	: [0.4, 0.3, 0.7],
		'rain'		: [0.4, 10, 0.5],
		'figure'	: [0.4, 10, 0.5],
		'wind'		: [0.4, 7, 2],
		'temperature': [0.4, 27, 20],
		'radiation'	: [0.4, 1400, 800],
		'humidity'	: [0.4, 0.3, 0.7],	
		'rigning'	: [0.4, 10, 0.5],
		'mynd'		: [0.4, 10, 0.5],
		"vindur"	: [0.4, 7, 2],
		"hitastig"	: [0.4, 27, 20],
		"geislun"	: [0.4, 1400, 800],
		"raki"		: [0,4, 0,3, 0,7]
		}
	out =  DIC.get(var, ['Null', 'Null', 'Null'])
	return(out[0], out[1], out[2])
#######################################
## return file path for each grid
def _get_GFILE(var):
	return {1	:	'/var/www/processamento/CFSD10001',
			2	:	'/var/www/processamento/CFSD20001',
			3	:	'/var/www/processamento/EXEMPLE_FILE',
			}.get(var, 'Null')

##############################################################################
## Checkin nc files
def _get_FILE(grid):
	file = _get_GFILE(grid)
	date = datetime.datetime.now()
	# if date.hour >= 12:
	date1 = date.replace(hour=00)
	date2 = date1  - datetime.timedelta(days = 1)
	ens1 = file+"E1"+date1.strftime('%Y%m%d')+"00.nc"
	ens2 = file+"E2"+date1.strftime('%Y%m%d')+"00.nc"
	ens3 = file+"E3"+date1.strftime('%Y%m%d')+"00.nc"
	ens4 = file+"E4"+date1.strftime('%Y%m%d')+"00.nc"
	ens5 = file+"E1"+date2.strftime('%Y%m%d')+"00.nc"
	ens6 = file+"E2"+date2.strftime('%Y%m%d')+"00.nc"
	ens7 = file+"E3"+date2.strftime('%Y%m%d')+"00.nc"
	ens8 = file+"E4"+date2.strftime('%Y%m%d')+"00.nc"		
	brk = 0
	while os.path.isfile(ens1) != True:
		date1 = date1 - datetime.timedelta(days = 1)
		date2 = date2 - datetime.timedelta(days = 1)
		ens1 = file+"E1"+date1.strftime('%Y%m%d')+"00.nc"
		ens2 = file+"E2"+date1.strftime('%Y%m%d')+"00.nc"
		ens3 = file+"E3"+date1.strftime('%Y%m%d')+"00.nc"
		ens4 = file+"E4"+date1.strftime('%Y%m%d')+"00.nc"
		ens5 = file+"E1"+date2.strftime('%Y%m%d')+"00.nc"
		ens6 = file+"E2"+date2.strftime('%Y%m%d')+"00.nc"
		ens7 = file+"E3"+date2.strftime('%Y%m%d')+"00.nc"
		ens8 = file+"E4"+date2.strftime('%Y%m%d')+"00.nc"
		if os.path.isfile(ens5) != True:
			ens1 = False
			break
		brk +=1	
		if brk >= 3:
			ens1 = False
			success = json_out._get_ERROR('file', 'CFS') 			
			exit(1)	
	ens1 = netCDF4.Dataset(ens1, 'r')
	ens2 = netCDF4.Dataset(ens2, 'r')
	ens3 = netCDF4.Dataset(ens3, 'r')
	ens4 = netCDF4.Dataset(ens4, 'r')
	ens5 = netCDF4.Dataset(ens5, 'r')
	ens6 = netCDF4.Dataset(ens6, 'r')
	ens7 = netCDF4.Dataset(ens7, 'r')
	ens8 = netCDF4.Dataset(ens8, 'r')
	return(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, date1)
##############################################################################
# Variables
def _get_rain(var, ncfile):
	try:
		var_nc = _get_NCVAR(var)
		var_rawa = ncfile.variables[var_nc]
		var_raw1 = np.array(var_rawa)
		for i in range(0, len(var_raw1)):
			if i == 0:
				var_raw1[i,:,:] = var_rawa[i,:,:]
			else:
				var_raw1[i,:,:] = np.subtract(var_rawa[i,:,:], var_rawa[i-1,:,:])
		var_raw1 = np.around(var_raw1, decimals=1)
		var_raw1[np.where(var_raw1<0)] = 0
	except:
		var_raw1 = np.nan	
	return(var_raw1)

def _get_wind(var, ncfile):
	try:
		var_nc = _get_NCVAR(var)
		var_rawu = ncfile.variables[var_nc[0]] 		
		var_rawv = ncfile.variables[var_nc[1]] 
		var_raw1 = np.sqrt(np.add(np.power(var_rawu, 2), np.power(var_rawv, 2))) # wind intensity
		var_raw1 = np.around(var_raw1, decimals=2)
		rp2 = 45.0/np.arctan(1.0)
		var_raw2 = np.add(np.multiply(np.arctan2(var_rawu, var_rawv), rp2), 180)
	except:
		var_raw1 = np.nan
		var_raw2 = np.nan

	return(var_raw1, var_raw2)

def _get_temperature(var,  ncfile):
	try:
		var_nc = _get_NCVAR(var)
		var_raw1 = ncfile.variables[var_nc]
		var_raw1  =np.subtract(var_raw1, 273.15)
		var_raw1 = np.around(var_raw1, decimals=2)
	except:
		var_raw1 = np.nan
	return(var_raw1)

def _get_radiation(var, ncfile):
	try:
		var_nc = _get_NCVAR(var)
		var_raw1 = ncfile.variables[var_nc]
		var_raw1 = np.around(var_raw1, decimals=2)
	except:
		var_raw1 = np.nan
	return(var_raw1)

def _get_humidity(var, ncfile):
	try:
		var_nc = _get_NCVAR(var)
		var_rawa = ncfile.variables[var_nc[0]] 		
		var_rawb = ncfile.variables[var_nc[1]] 		
		var_rawc = ncfile.variables[var_nc[2]]
                a1 = np.divide(np.subtract(var_rawb, 273.15), np.subtract(var_rawb, 35.86))
                a2 = np.multiply(17.29, a1)
                a3 = np.exp(a2)
                b1 = np.divide(379.90516, var_rawc)
                c1 = np.multiply(b1, a3)
                d1 = np.divide(var_rawa, c1)
                var_raw1 = np.multiply(100, d1)
		var_raw1 = np.around(var_raw1, decimals=2)
	except:
		var_raw1 = np.nan
		print "\n\n"
		print var_raw1

	return (var_raw1)

def _get_figure(var, ncfile):
	try:
		var_nc = _get_NCVAR(var)
		var_raw1 = ncfile.variables[var_nc[0]]
		var_raw2 = ncfile.variables[var_nc[1]]	
		var_raw1 = np.divide(var_raw1, 100)
	except:
		var_raw1 = np.nan
		var_raw2 = np.nan
	return(var_raw1, var_raw2)

def _get_time(var, ncfile):
	try:
		var_nc = _get_NCVAR(var)
		var_raw1 = ncfile.variables[var_nc]
	except:
		var_raw1 = np.nan	
	return(var_raw1)

#######################################
# Return all vars
def _get_all(var, ncfile):
	rain				= _get_rain('chuva', ncfile)
	speed, direction	= _get_wind('vento', ncfile)			
	radiation			= _get_radiation('radiacao', ncfile)
	temperature			= _get_temperature('temperatura', ncfile)
	humidity			= _get_humidity('umidade', ncfile)
	return(rain, speed, direction, radiation, temperature, humidity)
