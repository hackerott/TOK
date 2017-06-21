#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import netCDF4
import math
import sys
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan


def apk(GFSfile, iz, ix, iy): 
	nc = netCDF4.Dataset(GFSfile, 'r')
	var_q = nc.variables['spfh2m'] 
	var_t = nc.variables['tmp2m'] 
	var_p = nc.variables['pressfc'] 
	var_nc = []
	for i in range(0, 31):
		var_nc.append(100*(var_q[i, ix, iy]/(379.90516/var_p[i, ix, iy] * exp(17.2693882*((var_t[i, ix, iy] - 273.15)/(var_t[i, i, i] - 35.86))))))

	v_max = max(var_nc[1:30])
	v_min = min(var_nc[1:30])
	valor = var_nc[iz]
        if valor <= 1:
                cor = 'Yellow'
        elif valor >= 10:
                cor = 'Red'
        else:
                cor = 'Green'

	return(valor, v_max, v_min, cor)
