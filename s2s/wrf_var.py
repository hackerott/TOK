#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4

#######################################
## return the nc var_names for each variable
def _get_NCVAR(var):
	return {
		'chuva'		: ['RAINC', 'RAINNC'],
		'temp'		: '',
		'radiacao'	: '',
		'umidade'	: '', 
		'vento'		: '',
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
		'all'		: 6
		}.get(var, 'Null')

#######################################
## return limits for each var 
def _get_LIM(var):
	DIC = {
		'chuva'		: [0.4, 10, 0.5]
		'vento'		: [0.4, 7, 2]
		'temp'		: [0.4, 27, 20]
		'radiacao'	: [0.4, 1400, 800]
		'umidade'	: [0.4, 0.3, 0.7]
		}
	out =  DIC.get(var, ['Null', 'Null', 'Null'])
	return(out[0], out[1], out[2])

##############################################################################
## Checkin nc files
def _get_FILE(dateC, date2):
	ens1 = "/var/www/html/processamento/WRFD10001"+dateC.strftime('%Y%m%d%H')+".nc"
	ens2 = "/var/www/html/processamento/WRFD10001"+date2.strftime('%Y%m%d%H')+".nc"
	while os.path.isfile(ens1) != True:
		dateC = dateC - datetime.timedelta(hours = 12)
		date2 = date2 - datetime.timedelta(hours = 12)
		ens1 = "/var/www/html/processamento/WRFD10001"+dateC.strftime('%Y%m%d%H')+".nc"
		ens2 = "/var/www/html/processamento/WRFD10001"+date2.strftime('%Y%m%d%H')+".nc"
		if os.path.isfile(ens2) != True:
			ens1 = False
			break
		brk += 1	
		if brk >= 3:
			ens1 = False
			success = json_out._get_ERROR('file', 'GFS') 			
			exit(1)	

	return(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8)

##############################################################################
## Variables
def _get_rain(var, ncfile):
	var_nc = _get_NCVAR(var[0])
	var_rawa = ncfile.variables[var_nc[0]]	
	var_rawb = ncfile.variables[var_nc[1]]
	var_raw1 = np.add(var_rawa, var_rawb)
	return(var_raw1)

def _get_wind(var, ncfile):
	var_nc = _get_NCVAR(var)
	var_rawu = ncfile1.variables[var_nc[0]] 		
	var_rawv = ncfile1.variables[var_nc[1]] 
	var_raw1 = np.sqrt(np.add(np.power(var_rawu, 2), np.power(var_rawv, 2))) # wind intensity
	var_raw2 = np.arctan2(var_rawu, var_rawv) + np.power(var_rawv, 2)
	return(var_raw1, var_raw2)

def _get_radiation(var, ncfile):
	var_nc = _get_NCVAR(var)
	var_raw1 = ncfile.variables[var_nc]
	return(var_raw1)

def _get_temperature(var,  ncfile):
	var_nc = _get_NCVAR(var)
	var_raw1 = ncfile.variables[var_nc]
	var_raw1  =np.subtract(var_raw1, 273.15)
	return(var_raw1)

def _get_humidity(var, ncfile):
	var_nc = _get_NCVAR(var)
	var_rawa = ncfile1.variables[var_nc[0]] 		
	var_rawb = ncfile1.variables[var_nc[1]] 		
	var_rawc = ncfile1.variables[var_nc[2]]
	var_raw1 = np.multiply(np.multiply(100, np.divide(var_rawa, np.divide(379.90516, var_rawc))), np.exp(np.multiply(17.29, np.divide(np.add(var_rawb, -273.15), np.add(var_rawb, -35.86))))) 
	return (var_raw1)

def _get_cloud(var, ncfile):
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
