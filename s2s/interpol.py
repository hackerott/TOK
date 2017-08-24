#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import datetime
from scipy.interpolate import interp1d

#######################################
def _get_gfs_days(val, dat):
	ds = int(len(val) - 24)
	tgt_date = dat[0] + datetime.timedelta(hours = ds)
	value = []
	date = []
	for i in range(0, len(val)):
		if dat[i] == dat[-1]:
			date.append(dat[i])
			value.append(int(val[i]*10)/10.0)
			break
		elif dat[i] >= tgt_date:
			for j in range(1, 3):
				value.append(np.nan)
				date.append(dat[i] + datetime.timedelta(hours = j))
			value.append(int(val[i]*10)/10.0)
		else:
			value.append(int(val[i]*10)/10.0)
			date.append(dat[i])
	value = np.array(value)
	index = np.arange(len(value))
	not_nan = np.logical_not(np.isnan(value))
	out = interp1d(index[not_nan], value[not_nan], bounds_error=False)
	out = out(index)
	out1 = []
	for i in range(0, len(out)):
		out1.append(out[i])
	return(out1, date)

#######################################
'''
This is a really bad idea, there will be more interpoleted data then actualy data usin this function
'''
def _get_cfs_days(val, dat):
	value = []
	date = []
	for i in range(0, len(val)):
		value.append(int(val[i]*10)/10.0)
		date.append(dat[i])
		for j in range(1, 8):
			value.append(np.nan)
			date.append(dat[i] + datetime.timedelta(hours = i))

	value = np.array(value)
	index = np.arange(len(value))
	not_nan = np.logical_not(np.isnan(value))
	out = interp1d(index[not_nan], value[not_nan], bounds_error=False)
	out = out(index)
	out1 = []
	for i in range(0, len(out)):
		out1.append(out[i])
	return(out1, date)
