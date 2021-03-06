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
def _get_Prob(var_raw, ix, iy, max_i, top_lim, bot_lim):
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
def _get_AREAP(ncfile, var, ix, iy, top_lim, bot_lim, ):
	time = ncfile.variables['time']
	max_i = len(time)
	top_lim =
	bot_lim =
	var_nc = _get_NCVAR(var)
###
#ERROR MANAGEMENT
	if var_nc == 'Null':  
		exit(1)
'''
Add here (or in other script) proper error management, need to create a error table
'''
###
	if len(var_nc) == 1:
		var_raw = ncfile.variables[var_nc] #single variable from nc

	elif len(var_nc) == 2:
		var_raw1 = ncfile.variables[var_nc[0]] 		
		var_raw2 = ncfile.variables[var_nc[1]] 		
		var_raw = np.sqrt(np.add(np.power(var_raw1, 2), np.power(var_raw2, 2))) # wind intensity

	elif len(var_nc) == 3:
		var_raw1 = ncfile.variables[var_nc[0]] 		
		var_raw2 = ncfile.variables[var_nc[1]] 		
		var_raw3 = ncfile.variables[var_nc[2]]
		var_raw = np.multiply(np.multiply(100, np.divide(var_raw1, np.divide(379.90516, var_raw3))), np.exp(np.multiply(17.29, np.divide(np.add(var_raw2, -273.15), np.add(var_raw2, -35.86))))) # relative humidity

#	prob	= [0]*max_i 
	prob_r	= [0]*max_i 
	prob_g	= [0]*max_i 
	prob_y	= [0]*max_i 
	value	= [0]*max_i

#prob goes from 1 to 25 

	v_1, p_g1, p_r1, p_y1 = thread.start_new_thread(_get_Prob, (var_raw, ix, iy, max_i, top_lim, bot_lim))
	v_2, p_g2, p_r2, p_y2 = thread.start_new_thread(_get_Prob, (var_raw, ix, iy+1, max_i, top_lim, bot_lim))
	v_3, p_g3, p_r3, p_y3 = thread.start_new_thread(_get_Prob, (var_raw, ix, iy-1, max_i, top_lim, bot_lim))
	v_4, p_g4, p_r4, p_y4 = thread.start_new_thread(_get_Prob, (var_raw, ix+1, iy, max_i, top_lim, bot_lim))
	v_5, p_g5, p_r5, p_y5 = thread.start_new_thread(_get_Prob, (var_raw, ix-1, iy, max_i, top_lim, bot_lim))
	v_6, p_g6, p_r6, p_y6 = thread.start_new_thread(_get_Prob, (var_raw, ix+1, iy+1, max_i, top_lim, bot_lim))
	v_7, p_g7, p_r7, p_y7 = thread.start_new_thread(_get_Prob, (var_raw, ix+1, iy-1, max_i, top_lim, bot_lim))
	v_8, p_g8, p_r8, p_y8 = thread.start_new_thread(_get_Prob, (var_raw, ix-1, iy+1, max_i, top_lim, bot_lim))
	v_9, p_g9, p_r9, p_y9 = thread.start_new_thread(_get_Prob, (var_raw, ix-1, iy-1, max_i, top_lim, bot_lim))

	v_10, p_g10, p_r10, p_y10 = thread.start_new_thread(_get_Prob, (var_raw, ix+2, iy+2, max_i, top_lim, bot_lim))
	v_11, p_g11, p_r11, p_y11 = thread.start_new_thread(_get_Prob, (var_raw, ix+2, iy+1, max_i, top_lim, bot_lim))
	v_12, p_g12, p_r12, p_y12 = thread.start_new_thread(_get_Prob, (var_raw, ix+2, iy, max_i, top_lim, bot_lim))
	v_13, p_g13, p_r13, p_y13 = thread.start_new_thread(_get_Prob, (var_raw, ix+2, iy-1, max_i, top_lim, bot_lim))
	v_14, p_g14, p_r14, p_y14 = thread.start_new_thread(_get_Prob, (var_raw, ix+2, iy-2, max_i, top_lim, bot_lim))
	v_15, p_g15, p_r15, p_y15 = thread.start_new_thread(_get_Prob, (var_raw, ix+1, iy+2, max_i, top_lim, bot_lim))
	v_16, p_g16, p_r16, p_y16 = thread.start_new_thread(_get_Prob, (var_raw, ix+1, iy-2, max_i, top_lim, bot_lim))
	v_17, p_g17, p_r17, p_y17 = thread.start_new_thread(_get_Prob, (var_raw, ix, iy+2, max_i, top_lim, bot_lim))
	v_18, p_g18, p_r18, p_y18 = thread.start_new_thread(_get_Prob, (var_raw, ix, iy-2, max_i, top_lim, bot_lim))
	v_19, p_g19, p_r19, p_y19 = thread.start_new_thread(_get_Prob, (var_raw, ix-1, iy+2, max_i, top_lim, bot_lim))
	v_20, p_g20, p_r20, p_y20 = thread.start_new_thread(_get_Prob, (var_raw, ix-1, iy-2, max_i, top_lim, bot_lim))
	v_21, p_g21, p_r21, p_y21 = thread.start_new_thread(_get_Prob, (var_raw, ix-2, iy+2, max_i, top_lim, bot_lim))
	v_22, p_g22, p_r22, p_y22 = thread.start_new_thread(_get_Prob, (var_raw, ix-2, iy+1, max_i, top_lim, bot_lim))
	v_23, p_g23, p_r23, p_y23 = thread.start_new_thread(_get_Prob, (var_raw, ix-2, iy, max_i, top_lim, bot_lim))
	v_24, p_g24, p_r24, p_y24 = thread.start_new_thread(_get_Prob, (var_raw, ix-2, iy-1, max_i, top_lim, bot_lim))
	v_25, p_g25, p_r25, p_y25 = thread.start_new_thread(_get_Prob, (var_raw, ix-2, iy-2, max_i, top_lim, bot_lim))

#Center value gets 1/2 of prob, first 4 points get 1/4, and next 12 1/4	

	prob_g	= np.add(np.divide(p_g1, 2), np.add(np.divide(np.add(np.add(np.add(p_g2, p_g3), np.add(p_g4, p_g5)), np.add(np.add(p_g6, p_g7), np.add(p_g8, p_g9))), 3), np.divide(np.add(np.add(np.add(np.add(p_g10, p_g11), np.add(p_g12, p_g13)), np.add(np.add(p_g14, p_g15), np.add(p_g16, p_g17))), np.add(np.add(np.add(p_g18, p_g19), np.add(p_g20, p_g21)), np.add(np.add(p_g22, p_g23), np.add(p_g24, p_g25)))), 6)))

	prob_r	= np.add(np.divide(p_r1, 2), np.add(np.divide(np.add(np.add(np.add(p_r2, p_r3), np.add(p_r4, p_r5)), np.add(np.add(p_r6, p_r7), np.add(p_r8, p_r9))), 3), np.divide(np.add(np.add(np.add(np.add(p_r10, p_r11), np.add(p_r12, p_r13)), np.add(np.add(p_r14, p_r15), np.add(p_r16, p_r17))), np.add(np.add(np.add(p_r18, p_r19), np.add(p_r20, p_r21)), np.add(np.add(p_r22, p_r23), np.add(p_r24, p_r25)))), 6)))

	prob_y	= np.add(np.divide(p_y1, 2), np.add(np.divide(np.add(np.add(np.add(p_y2, p_y3), np.add(p_y4, p_y5)), np.add(np.add(p_y6, p_y7), np.add(p_y8, p_y9))), 3), np.divide(np.add(np.add(np.add(np.add(p_y10, p_y11), np.add(p_y12, p_y13)), np.add(np.add(p_y14, p_y15), np.add(p_y16, p_y17))), np.add(np.add(np.add(p_y18, p_y19), np.add(p_y20, p_y21)), np.add(np.add(p_y22, p_y23), np.add(p_y24, p_y25)))), 6)))

	value	= np.add(np.divide(v_1, 2), np.add(np.divide(np.add(np.add(np.add(v_2, v_3), np.add(v_4, v_5)), np.add(np.add(v_6, v_7), np.add(v_8, v_9))), 3), np.divide(np.add(np.add(np.add(np.add(v_10, v_11), np.add(v_12, v_13)), np.add(np.add(v_14, v_15), np.add(v_16, v_17))), np.add(np.add(np.add(v_18, v_19), np.add(v_20, v_21)), np.add(np.add(v_22, v_23), np.add(v_24, v_25)))), 6)))

	max_value = np.mean(value) + np.std(value)
	min_value = np.mean(value) - np.std(value)

	# array	= [v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11, v_12, v_13, v_14, v_15, v_16, v_17, v_18, v_19, v_20, v_21, v_22, v_23, v_24, v_25] 
	# max_index = np.divide((np.mean(array) + np.std(array)), max(array).any)
	# min_index = np.divide((np.mean(array) - np.std(array)), min(array).any)
	# val_index = np.divide(value, np.mean(array))

	# if max_index <= 1 and min_index <=1:
	# 	print "baixa dispersao/low dispersion"
	# if val_index > 1 and max_index > 1:
	# 	print "vies positivo/positive bias"
	# if val_index < 1 and min_index > 1:
	# 	print "vies negativo/negative bias"

	return(prob_g, prob_r, prob_y, value, max_value, min_value)
