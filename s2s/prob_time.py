#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
# import thread

#######################################
## return the probabilitys for each alert level
def _get_Prob(var_raw1, var_raw2, iz, ix, iy, max_i, top_lim, bot_lim):
	prob_y	= [0]*max_i
	prob_g	= [0]*max_i
	prob_r	= [0]*max_i
	var1	= [0]*max_i
	var2	= [0]*max_i
	for i in  range(0, max_i):
		if i+iz >= max_i:
			break
		var1[i] =  var_raw1[i, ix, iy]
		var2[i] =  var_raw2[i+iz, ix, iy]
		if var1[i] < -99.99 and var2[i] < -99.99:
			var1[i] = np.nan
			var2[i] = np.nan

		elif var1[i] > -99.99 and var2[i] < -99.99:  
			if var1[i] < top_lim:
				prob_y[i] += 2	
			if var1[i] < bot_lim:
				prob_g[i] += 2
			if var1[i] >= top_lim:
				prob_r[i] += 2
			var2[i] = np.nan

		elif var1[i] < -99.99 and var2[i] > -99.99:  
			if var1[i] < top_lim:
				prob_y[i] += 1	
			if var1[i] < bot_lim:
				prob_g[i] += 1
			if var1[i] >= top_lim:
				prob_r[i] += 1
			var1[i] = np.nan

		elif var1[i] > 99999.99  and var2[i] > 99999.99:
			var1[i] = np.nan
			var2[i] = np.nan

		elif var1[i] < 99999.99 and var2[i] > 99999.99:  
			if var1[i] < top_lim:
				prob_y[i] += 2	
			if var1[i] < bot_lim:
				prob_g[i] += 2
			if var1[i] >= top_lim:
				prob_r[i] += 2
			var2[i] = np.nan

		elif var1[i] > 99999.99 and var2[i] < 99999.99:  
			if var2[i] < top_lim:
				prob_y[i] += 1	
			if var2[i] < bot_lim:
				prob_g[i] += 1
			if var2[i] >= top_lim:
				prob_r[i] += 1
			var1[i] = np.nan

		else:
			if var1[i] < top_lim:
				prob_y[i] += 2	
			if var1[i] < bot_lim:
				prob_g[i] += 2
			if var1[i] >= top_lim:
				prob_r[i] += 2
			if var2[i] < top_lim:
				prob_y[i] += 1	
			if var2[i] < bot_lim:
				prob_g[i] += 1
			if var2[i] >= top_lim:
				prob_r[i] += 1

	for i in range((max_i-24), max_i):
		var1[i] =  var_raw1[i, ix, iy]
		if var1[i] < -99.99 or var1[i] > 9999.99:
			var1[i] = np.nan
		else:
			if var1[i] < top_lim:
				prob_y[i] += 2	
			if var1[i] < bot_lim:
				prob_g[i] += 2
			if var1[i] >= top_lim:
				prob_r[i] += 2
		var2[i] = var1[i]

	prob_y = np.divide(prob_y, 3)
	prob_g = np.divide(prob_g, 3)
	prob_r = np.divide(prob_r, 3)
	var1 = np.divide(np.add(np.multiply(var1, 2), var2), 3)

	return (var1, prob_g, prob_r, prob_y)

#######################################
# return the final values of prob for each member
def _get_TIMEP(var_raw1, var_raw2, time, iz, ix, iy, top_lim, bot_lim):
	max_i = len(time)
	value, prob_g, prob_r, prob_y = _get_Prob(var_raw1, var_raw2, iz, ix, iy, max_i, top_lim, bot_lim)
	t_quartile = np.nanpercentile(value, 75)
	b_quartile = np.nanpercentile(value, 25)
	max_value = []
	min_value = []
	for i in range(0, len(value)):
		# max_value.append(np.mean([value[i],t_quartile]))
		# min_value.append(np.mean([value[i],b_quartile]))
		max_value.append(np.divide(np.add(value[i],t_quartile), 2))
		min_value.append(np.divide(np.add(value[i],b_quartile), 2))
		# if np.isnan(max_value[-1]):
		# 	max_value[-1] = t_quartile
		# if np.isnan(min_value[-1]):
		# 	min_value[-1] = b_quartile
		# if max_value[-1] > 9999.99:
		# 	max_value[-1] = t_quartile
		# if min_value[-1] < -99.99:
		# 	min_value[-1] = b_quartile

	return(prob_g, prob_r, prob_y, value, max_value, min_value)

