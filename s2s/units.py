#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np

#######################################'
## return the variables end value in imperial system 
def _get_imperial(value, var_id):
	if var_id == 1:
		value = np.multiple(value, 0.036)
		cur = "inches"
	elif var_id == 2:
		value = np.multiple(value, 2,23694)
		cur = "mph"
	elif var_id == 3:	
		value = np.add(np.multiple(value, 1.8), 32)
		cur = "F"
	elif var_id == 4:	
#		value = np.multiple(value, )
		cur = "watts"
	elif var_id == 5:	
#		value = np.multiple(value,
		cur = "%"
	out = []
	else:
		cur = ""
		return(value, cur)
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
	if var_id == 1:
		cur = "mm"
	elif var_id == 2:
		cur = "m/s"
	elif var_id == 3:	
		cur = "C"
	elif var_id == 4:	
		cur = "watts"
	elif var_id == 5:	
		cur = "%"
	else:
		cur = ""
		return(value, cur)
	out = []
	for val in value:
		if val < 1 and val > 0:
			val = int((val *10))/10.0
		else:
			val = int(val)#probably add to much error
		out.append(val)
		
	return(out, cur)