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
			if len(value[0]) > 1:
				tp = 1
			else:
				tp = 0
		except:
			tp = 0

		if tp == 1:
			out = []
			for i in range(0, len(value)):
				value_1 = np.multiply(value[i,0], 2.23694)
				if value[i,0] < 1 and value[i,0] > 0:
					val = int((value_1*10))/10.0
					val = [val, int(value[i,1])] 
				else:
					try:
						val = [int(value_1), int(value[i,1])] #probably add to much error
					except:
						val = [value_1, int(value[i,1])]
				out.append(val)
			out = np.array(out)
			return(out, cur)
		elif tp == 0:
			try:
				out = []
				for i in range(0, len(value)):
					val = np.multiply(value[i], 2.23694)
					if val < 1 and val > 0:
						val = int((val*10))/10.0
					else:
						try:
							val = int(val) #probably add to much error
						except:
							val = val
					out.append(val)
				return(out, cur)
			except:
				try:
					out = np.multiply(value, 2.23694)
				except:
					out = value
					cur = "metric"
				return(out, cur)	

	elif var_id == 3:	
		if len(value[0]) > 0: ## ugly fix 
			v = []
			for i, val in enumerate(value):
				try:
					val1 = (val[0] * 1.8) + 32
				except:
					val1 = np.nan
				try:
					val2 = (val[1] * 1.8) + 32
				except:
					val2 = np.nan
				if val1 < 1 and val1 > 0:
					val1 = int(val1*10)/10.0	
				else:
					try:
						val1 = int(val1)
					except:
						val1 = val1
				if val2 < 1 and val2 > 0:
					val2 = int(val2*10)/10.0	
				else:
					try:
						val2 = int(val2)
					except:
						val2 = val2
				v.append([val1, val2])
			value = v
			del v, val1, val2
		else:   
			value = np.add(np.multiply(value, 1.8), 32)

	elif var_id <= 5:	
		cur = "metric"
		value = value

	else:
		cur = "metric"
		return(value, cur)
	out = []

	try:
		for i in range(0, len(value)):
			if len(value[i]) > 0:
				val = value[i]
				if val[0] < 1 and  val[0] > 0:
					v1 = int(val[0]*10)/10.0
				else:
					try:
						v1 = int(val[0])
					except:
						v1 = val[0]	
				if val[1] < 1 and  val[1] > 0:
					v2 = int(val[1]*10)/10.0
				else:
					try:
						v2 = int(val[1])
					except:
						v2 = val[1]	
				val = [v1, v2]
			else:	
				if value[i] < 1 and value[i] > 0:
					val = int((value[i] *10))/10.0
				else:
					val = int(value[i]) #probably add to much error
			out.append(val)
	except:
		if len(value) == 0:
			if value < 1 and value > 0:
				val = int((value *10))/10.0
			else:
				try:
					val = int(value) #probably add to much error
				except:
					val = val
			out = val
		else:
			out = value
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
	
	try:
		for i in range(0, len(value)):
			if value[i] < 1 and value[i] > 0:
				val = int((value[i] *10))/10.0
			else:
				val = int(value[i]) #probably add to much error
			out.append(val)
	except:
		try:
			for val in value:
				try:
					if val.any() < 1 and val.any() > 0:
						try:
							val = int((val *10))/10.0
						except:
							val = val
					else:
						try:
							val = int(val) #probably add to much error
						except:
							val = val
					out.append(val)
				except:
					out.append(val)
		except:
			out = value			
		out = np.array(out)
	return(out, cur)
