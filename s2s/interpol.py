#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import datetime
from scipy.interpolate import interp1d

#######################################
def _get_gfs_days(val, dat):
	try:
		value = []
		for i in range(0, len(val)):
			if val[i] > 9999.99:
				value.append(np.nan)
			elif val[i] < -99.99:
				value.append(np.nan)
			else:
				value.append(val[i])
		value = np.array(value)
		index = np.arange(len(value))
		try:
			not_nan = np.logical_not(np.isnan(value))
			out = interp1d(index[not_nan], value[not_nan], bounds_error=False)
			out = out(index)
		except:
			out = value
		out1 = []
		date = []
		for i in range(0, len(dat)):
			if np.invert(np.isnan(out[i])):
				out1.append(out[i])
				date.append(dat[i])
	except:
		if np.invert(np.isnan(val)):
			out1 = val
		else:
			out1 = 'Null'
		date = dat
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

        index = np.arange(len(value))
        not_nan = np.logical(np.isnan(value))
        out = np.interp(index, index[not_nan], value[not_nan])

        return(out, date)

#######################################
def _get_wrf_days(val, dat):
	try:
		value = []
		for i in range(0, len(val)):
			if val[i] > 9999.99:
				value.append(np.nan)
			elif val[i] < -99.99:
				value.append(np.nan)
			else:
				value.append(val[i])
		value = np.array(value)
		index = np.arange(len(value))
		try:
			not_nan = np.logical_not(np.isnan(value))
			out = interp1d(index[not_nan], value[not_nan], bounds_error=False)
			out = out(index)
		except:
			out = value
		out1 = []
		date = []
		for i in range(0, len(dat)):
			if np.invert(np.isnan(out[i])):
				out1.append(out[i])
				date.append(dat[i])
	except:
		if np.invert(np.isnan(val)):
			out1 = val
		else:
			out1 = 'Null'
		date = dat
	return(out1, date)

#######################################