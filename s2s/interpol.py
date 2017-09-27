#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import datetime
from scipy.interpolate import interp1d

#######################################
def _get_gfs_days(val, dat):
	for i in range(0, len(val)):
		if val[i] < -999.9:
			value.append(np.nan)
		else:
			value.append(val[i])
	date = dat
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

        index = np.arange(len(value))
        not_nan = np.logical(np.isnan(value))
        out = np.interp(index, index[not_nan], value[not_nan])

        return(out, date)
