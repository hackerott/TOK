#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import datetime

#######################################
def _get_gfs_days(val, dat):
	tgt_date = dat[0] + datetime.timedelta(days = 4)
	value = []
	date = []
	for i in range(0, len(value)):
		if dat[i] > tgt_date:
			value.append(val[i])
			for j in range(0, 3):
				value.append(np.nan)
				date.append(dat[i] + datetime.timedelta(hours = i))

		else:
			value.append(val[i])
			date.append(dat[i])
	index = np.arange(len(value))
	not_nan = np.logical(np.isnan(value))
	out = np.interp(index, index[not_nan], value[not_nan])

	return(out, date)

#######################################
'''
This is a really bad idea, there will be more interpoleted data then actualy data usin this function
'''
def _get_cfs_days(val, dat):
	value = []
	date = []
	for i in range(0, len(value)):
		value.append(val[i])
		date.append(dat[i])
		for j in range(1, 8):
			value.append(np.nan)
			date.append(dat[i] + datetime.timedelta(hours = i))

	index = np.arange(len(value))
	not_nan = np.logical(np.isnan(value))
	out = np.interp(index, index[not_nan], value[not_nan])

	return(out, date)