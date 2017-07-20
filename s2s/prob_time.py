#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
# import thread

#######################################
## S2S imports

#######################################
## return the nc var_names for each variable
# def _get_NCVAR(var):
# 	return {
# 		'chuva'		: 'pratesfc',
# 		'temperatura'	: 'tmp2m',
# 		'radiacao'	: 'dswrfsfc',
# 		'umidade'	: ['spfh2m', 'tmp2m', 'pressfc'], 
# 		'vento'		: ['ugrd10m', 'vgrd10m']
# 		}.get(var, 'Null')
#
#######################################
## return the probabilitys for each alert level
def _get_Prob(var_raw1, var_raw2, iz, ix, iy, max_i, top_lim, bot_lim):
	prob_y = [0]*max_i
	prob_g = [0]*max_i
	prob_r = [0]*max_i
	var1   = [0]*max_i
	var2   = [0]*max_i
	for i in  range(0, max_i):
		if i+iz >= max_i:
			break
		var1[i] =  var_raw1[i, ix, iy]
		var2[i] =  var_raw2[i+iz, ix, iy]
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
def _get_TIMEP(var_raw1, var_raw2, time, iz, ix, iy, top_lim, bot_lim):
#	max_i = len(var_raw1[:, ix, iy])
	max_i = len(time)
	value, prob_g, prob_r, prob_y = _get_Prob(var_raw1, var_raw2, iz, ix, iy, max_i, top_lim, bot_lim)
	# max_value = np.mean(value) + np.std(value)
	# min_value = np.mean(value) - np.std(value)
#        std_value = np.std(value)
	t_quartile = np.percentile(value, 75)
	b_quartile = np.percentile(value, 25)
	
        max_value = []
        min_value = []
        for i in range(0, len(value)):
#                max_value.append((value[i]+std_value))
#                min_value.append((value[i]-std_value))
                max_value.append((value[i]+t_quartile)/2)
                min_value.append((value[i]+b_quartile)/2)
		
	return(prob_g, prob_r, prob_y, value, max_value, min_value)

