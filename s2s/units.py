#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np

#######################################'
## return the variables end value in imperial system 
def _get_imperial(value, var_id):
	cur = "imperial"
	if var_id == 1:
		value = np.multiply(value, 0.036)
	elif var_id == 2:
		try:
			value_1 = np.multiply(value[:,0], 2.23694)
			out = []
			for val, i in value_1:
				if val < 1 and val > 0:
					val = int((val *10))/10.0
					val = [val, int(value[i,1])] 
				else:
					val = [int(val), int(value[i,1])] #probably add to much error
				out.append(val)
			out = np.array(out)
			return(out, cur)
		except:
			value = np.multiply(value, 2.23694)
	elif var_id == 3:	
		value = np.add(np.multiply(value, 1.8), 32)
	elif var_id <= 5:	
		cur = "metric"
		value = value
	else:
		cur = "metric"
		return(value, cur)
	out = []
	for val in value:
		if val < 1 and val > 0:
			val = int((val *10))/10.0
		else:
			val = int(val) #probably add to much error
		out.append(val)
	return(out, cur)
#######################################'
## return the variables end value metric
def _get_metric(value, var_id):
	cur = "metric"
	out = []
	if var_id == 2:	
		try:
			for i in range(0, len(value)):
				if value[i,0] < 1 and value[i,0] > 0:
					val = int((value[i, 0]*10))/10.0
					val = [val, int(value[i, 1])] 
				else:
					val = [int(value[i, 0]), int(value[i, 1])] #probably add to much error
				out.append(val)
			out = np.array(out)
			return(out, cur)
		except:
			value = value
	elif var_id <= 5:
		value = value

	else:
		return(value, cur)
	for val in value:
		if val < 1 and val > 0:
			val = int((val *10))/10.0
		else:
			val = int(val) #probably add to much error
		out.append(val)
	return(out, cur)
