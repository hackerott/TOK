#!/usr/bin/python
# coding: utf-8

import numpy as np
import math
import datetime

#######################################

#######################################
## return the nc var_names for each variable
def _get_NCVAR(var):
	return {
		'chuva'		: 'pratesfc',
		'temperatura'	: 'tmp2m',
		'radiacao'	: 'dswrfsfc',
		'umidade'	: 'spfh2m', 'tmp2m', 'pressfc', 
		'vento'		: 'ugrd10m', 'vgrd10m'
		}.get(var, 'Null')

#######################################
## return the probabilitys for each alert level
def _get_Prob(var_raw, ix, iy, max_i):
	prob_y = [0]*max_i
	prob_g = [0]*max_i
	prob_r = [0]*max_i
	var1   = [0]*max_i
	for i in  range(0, max_i):
		var1[i] =  var_raw[i, ix, iy]
		if var1[i] < top_lim:
			prob_y[i] += 1	

		if var1[i] < bot_lim:
			prob_g[i] += 1
	
		if var1[i] > top_lim:
			prob_r[i] += 1
	return (var1, prob_g, prob_r, prob_y)

#######################################	
# return the final values of prob for each member
def _get_AREA(ncfile, var, ix, iy):
	time = ncfile.variables['time']
	max_i = len(time)
	top_lim =
	bot_lim =
	var_nc = _get_NCVAR(var)
	

	if len(var_nc) == 1:
		var_raw = ncfile.variables[var_nc]

	elif len(var_nc) == 2:
		var_raw1 = ncfile.variables[var_nc[0]] 		
		var_raw2 = ncfile.variables[var_nc[1]] 		
		for i in range(0, max_i):
			var_raw.append(sqrt(power(var_raw1[i, :, :], 2) + power(var_raw2[i, :, :], 2)))

	elif len(var_nc) == 3:
		var_raw1 = ncfile.variables[var_nc[0]] 		
		var_raw2 = ncfile.variables[var_nc[1]] 		
		var_raw3 = ncfile.variables[var_nc[2]]
		for i in range(0, max_i):
			var_raw.append(100*(var_raw1[i, :, :]/(379.90516/var_raw3[i, :, :] * exp(17.29*((var_raw2[i, :, :] - 273.15)/(var_raw2[i, :, :] - 35.86))))))

#Center value gets 1/2 of prob, first 4 points get 1/4, and next 12 1/4
	prob  = [0]*max_i 
	value = [0]*max_i
#######
''' 
Add aqui declaracao de todas as prob (A-0-1 ate A-2-12) via lançamento de tread, para agilizar a execucao, os valores sao independentes.

http://softwareramblings.com/2008/06/running-functions-as-threads-in-python.html

import thread

thread.start_new_thread(_funcao, (argumentos)

'''
	for i in  range(0, max_i):
		prob[i] = ## soma de todas as prob com os pesos
		value[i] = ## soma de todos os valores com os pesos

	max_value = np.mean(value) + np.std(value)
	min_value = np.mean(value) - np.std(value)

	return(prob, value, max_value, min_value)
