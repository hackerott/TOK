#!/usr/bin/python
# coding: utf-8

import numpy as np
import thread
import netCDF4

#######################################

#######################################
## return the nc var_names for each variable
def _get_NCVAR(var):
	return {
		'chuva'		: 'pratesfc',
		'temperatura'	: 'tmp2m',
		'radiacao'	: 'dswrfsfc',
		'umidade'	: ['spfh2m', 'tmp2m', 'pressfc'], 
		'vento'		: ['ugrd10m', 'vgrd10m']
		}.get(var, 'Null')

#######################################
## return the probabilitys for each alert level
def _get_Prob(var_raw1, var_raw2, ix, iy, max_i, top_lim, bot_lim):
	prob_y = [0]*max_i
	prob_g = [0]*max_i
	prob_r = [0]*max_i
	var1   = [0]*max_i
	for i in  range(0, max_i):
		var1[i] =  var_raw1[i, ix, iy]
		var2[i] =  var_raw2[i, ix, iy]
		if var1[i] < top_lim:
			prob_y[i] += 2	
		if var1[i] < bot_lim:
			prob_g[i] += 2
		if var1[i] > top_lim:
			prob_r[i] += 2

		if var2[i] < top_lim:
			prob_y[i] += 1	
		if var2[i] < bot_lim:
			prob_g[i] += 1
		if var2[i] > top_lim:
			prob_r[i] += 1

	prob_y = np.divide(prob_y, 3)
	prob_g = np.divide(prob_g, 3)
	prob_r = np.divide(prob_r, 3)
	var1 = np.divide(np.add(np.multiply(var1, 2), var2), 3)	

	return (var1, prob_g, prob_r, prob_y)
#######################################	
# return the final values of prob for each member
def _get_TIMEP(ncfile1, ncfile2, var, ix, iy, top_lim, bot_lim):
	time = ncfile.variables['time']
	max_i = len(time)
	top_lim =
	bot_lim =
	var_nc = _get_NCVAR(var)
###
#ERROR MANAGEMENT
	if var_nc == 'Null':  
		exit(1)

	if len(var_nc) == 1:
		var_raw1 = ncfile1.variables[var_nc] #single variable from nc
		var_raw2 = ncfile2.variables[var_nc] #single variable from nc
	elif len(var_nc) == 2:
		var_rawa = ncfile.variables[var_nc[0]] 		
		var_rawb = ncfile.variables[var_nc[1]] 		
		var_rawc = ncfile.variables[var_nc[0]] 		
		var_rawd = ncfile.variables[var_nc[1]] 		
		var_raw1 = np.sqrt(np.add(np.power(var_rawa, 2), np.power(var_rawb, 2))) # wind intensity
		var_raw2 = np.sqrt(np.add(np.power(var_rawc, 2), np.power(var_rawd, 2))) # wind intensity

	elif len(var_nc) == 3:
		var_rawa = ncfile1.variables[var_nc[0]] 		
		var_rawb = ncfile1.variables[var_nc[1]] 		
		var_rawc = ncfile1.variables[var_nc[2]]
		var_rawd = ncfile2.variables[var_nc[0]] 		
		var_rawe = ncfile2.variables[var_nc[1]] 		
		var_rawf = ncfile2.variables[var_nc[2]]
		var_raw1 = np.multiply(np.multiply(100, np.divide(var_rawa, np.divide(379.90516, var_rawc))), np.exp(np.multiply(17.29, np.divide(np.add(var_rawb, -273.15), np.add(var_rawb, -35.86))))) # relative humidity
		var_raw2 = np.multiply(np.multiply(100, np.divide(var_rawd, np.divide(379.90516, var_rawf))), np.exp(np.multiply(17.29, np.divide(np.add(var_rawe, -273.15), np.add(var_rawe, -35.86))))) # relative humidity


	value, prob_g, prob_r, prob_y = _get_Prob(var_raw1, var_raw2, ix, iy, max_i, top_lim, bot_lim)
	# max_value = np.mean(value) + np.std(value)
	# min_value = np.mean(value) - np.std(value)
	std_value = np.std(value)
	max_value = []
	min_value = []
	for i in range(0, len(value)):
		max_value.append((value[i]+std_value))
		min_value.append((value[i]-std_value))
	return(prob_g, prob_r, prob_y, value, max_value, min_value)

