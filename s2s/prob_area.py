#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
#import thread

#######################################
## return the probabilitys for each alert level
def _get_Prob(var_raw, ix, iy, max_i, top_lim, bot_lim):
	prob_y	= [0]*(max_i)
	prob_g	= [0]*(max_i)
	prob_r	= [0]*(max_i)
	var1	= [0]*(max_i)
	for i in  range(0, max_i):
		var1[i] =  var_raw[i, ix, iy]
		if var1[i] > -99.99:
			if var1[i] < top_lim:
				prob_y[i] += 1	

			if var1[i] < bot_lim:
				prob_g[i] += 1
	
			if var1[i] >= top_lim:
				prob_r[i] += 1
		elif var1[i] > 9999.99 :
			prob_y[i] += 0
			prob_g[i] += 0
			prob_r[i] += 0
			var1[i] = np.nan
		else:
			prob_y[i] += 0
			prob_g[i] += 0
			prob_r[i] += 0
			var1[i] = np.nan

	return (var1, prob_g, prob_r, prob_y)

#######################################	
# return the final values of prob for each member
def _get_AREAP(var_raw, time, ix, iy, top_lim, bot_lim, ):

	max_i	= len(time)
	prob_r	= [0]*max_i 
	prob_g	= [0]*max_i 
	prob_y	= [0]*max_i 
	value	= [0]*max_i

#Paralel execution, still not working
	# v_1, p_g1, p_r1, p_y1 = thread.start_new_thread(_get_Prob, (var_raw, ix, iy, max_i, top_lim, bot_lim))

#Serial execution, amaziling fast 
	v_1, p_g1, p_r1, p_y1 = _get_Prob(var_raw, ix, iy, max_i, top_lim, bot_lim)
	v_2, p_g2, p_r2, p_y2 = _get_Prob(var_raw, ix, iy+1, max_i, top_lim, bot_lim)
	v_3, p_g3, p_r3, p_y3 = _get_Prob(var_raw, ix, iy-1, max_i, top_lim, bot_lim)
	v_4, p_g4, p_r4, p_y4 = _get_Prob(var_raw, ix+1, iy, max_i, top_lim, bot_lim)

	v_5, p_g5, p_r5, p_y5 = _get_Prob(var_raw, ix-1, iy, max_i, top_lim, bot_lim)
	v_6, p_g6, p_r6, p_y6 = _get_Prob(var_raw, ix+1, iy+1, max_i, top_lim, bot_lim)
	v_7, p_g7, p_r7, p_y7 = _get_Prob(var_raw, ix+1, iy-1, max_i, top_lim, bot_lim)
	v_8, p_g8, p_r8, p_y8 = _get_Prob(var_raw, ix-1, iy+1, max_i, top_lim, bot_lim)
	v_9, p_g9, p_r9, p_y9 = _get_Prob(var_raw, ix-1, iy-1, max_i, top_lim, bot_lim)

	v_10, p_g10, p_r10, p_y10 = _get_Prob(var_raw, ix+2, iy+2, max_i, top_lim, bot_lim)
	v_11, p_g11, p_r11, p_y11 = _get_Prob(var_raw, ix+2, iy+1, max_i, top_lim, bot_lim)
	v_12, p_g12, p_r12, p_y12 = _get_Prob(var_raw, ix+2, iy, max_i, top_lim, bot_lim)
	v_13, p_g13, p_r13, p_y13 = _get_Prob(var_raw, ix+2, iy-1, max_i, top_lim, bot_lim)
	v_14, p_g14, p_r14, p_y14 = _get_Prob(var_raw, ix+2, iy-2, max_i, top_lim, bot_lim)
	v_15, p_g15, p_r15, p_y15 = _get_Prob(var_raw, ix+1, iy+2, max_i, top_lim, bot_lim)
	v_16, p_g16, p_r16, p_y16 = _get_Prob(var_raw, ix+1, iy-2, max_i, top_lim, bot_lim)
	v_17, p_g17, p_r17, p_y17 = _get_Prob(var_raw, ix, iy+2, max_i, top_lim, bot_lim)
	v_18, p_g18, p_r18, p_y18 = _get_Prob(var_raw, ix, iy-2, max_i, top_lim, bot_lim)
	v_19, p_g19, p_r19, p_y19 = _get_Prob(var_raw, ix-1, iy+2, max_i, top_lim, bot_lim)
	v_20, p_g20, p_r20, p_y20 = _get_Prob(var_raw, ix-1, iy-2, max_i, top_lim, bot_lim)
	v_21, p_g21, p_r21, p_y21 = _get_Prob(var_raw, ix-2, iy+2, max_i, top_lim, bot_lim)
	v_22, p_g22, p_r22, p_y22 = _get_Prob(var_raw, ix-2, iy+1, max_i, top_lim, bot_lim)
	v_23, p_g23, p_r23, p_y23 = _get_Prob(var_raw, ix-2, iy, max_i, top_lim, bot_lim)
	v_24, p_g24, p_r24, p_y24 = _get_Prob(var_raw, ix-2, iy-1, max_i, top_lim, bot_lim)
	v_25, p_g25, p_r25, p_y25 = _get_Prob(var_raw, ix-2, iy-2, max_i, top_lim, bot_lim)

#Center value gets 1/2 of prob, first 4 points get 1/4, and next 12 1/4	

	prob_g	= (np.add(np.divide(p_g1, 2), np.add(np.divide(np.add(np.add(np.add(p_g2, p_g3), np.add(p_g4, p_g5)), np.add(np.add(p_g6, p_g7), np.add(p_g8, p_g9))), 32), np.divide(np.add(np.add(np.add(np.add(p_g10, p_g11), np.add(p_g12, p_g13)), np.add(np.add(p_g14, p_g15), np.add(p_g16, p_g17))), np.add(np.add(np.add(p_g18, p_g19), np.add(p_g20, p_g21)), np.add(np.add(p_g22, p_g23), np.add(p_g24, p_g25)))), 64))))

	prob_r	= (np.add(np.divide(p_r1, 2), np.add(np.divide(np.add(np.add(np.add(p_r2, p_r3), np.add(p_r4, p_r5)), np.add(np.add(p_r6, p_r7), np.add(p_r8, p_r9))), 32), np.divide(np.add(np.add(np.add(np.add(p_r10, p_r11), np.add(p_r12, p_r13)), np.add(np.add(p_r14, p_r15), np.add(p_r16, p_r17))), np.add(np.add(np.add(p_r18, p_r19), np.add(p_r20, p_r21)), np.add(np.add(p_r22, p_r23), np.add(p_r24, p_r25)))), 64))))

	prob_y	= (np.add(np.divide(p_y1, 2), np.add(np.divide(np.add(np.add(np.add(p_y2, p_y3), np.add(p_y4, p_y5)), np.add(np.add(p_y6, p_y7), np.add(p_y8, p_y9))), 32), np.divide(np.add(np.add(np.add(np.add(p_y10, p_y11), np.add(p_y12, p_y13)), np.add(np.add(p_y14, p_y15), np.add(p_y16, p_y17))), np.add(np.add(np.add(p_y18, p_y19), np.add(p_y20, p_y21)), np.add(np.add(p_y22, p_y23), np.add(p_y24, p_y25)))), 64))))

	value	= np.add(np.divide(v_1, 2), np.add(np.divide(np.add(np.add(np.add(v_2, v_3), np.add(v_4, v_5)), np.add(np.add(v_6, v_7), np.add(v_8, v_9))), 32), np.divide(np.add(np.add(np.add(np.add(v_10, v_11), np.add(v_12, v_13)), np.add(np.add(v_14, v_15), np.add(v_16, v_17))), np.add(np.add(np.add(v_18, v_19), np.add(v_20, v_21)), np.add(np.add(v_22, v_23), np.add(v_24, v_25)))), 64)))

	t_quartile = np.percentile(value, 75)
	b_quartile = np.percentile(value, 25)
	max_value = []
	min_value = []
	for i in range(0, len(value)):
#		max_value.append(np.mean([value[i],t_quartile]))
#		min_value.append(np.mean([value[i],b_quartile]))
		max_value.append(np.divide(np.add(value[i],t_quartile), 2))
		min_value.append(np.divide(np.add(value[i],b_quartile), 2))
	
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
