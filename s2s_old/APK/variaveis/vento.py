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
	var_u = nc.variables['ugrd10m'] 
	var_v = nc.variables['vgrd10m'] 
	var_nc = []
	for i in range(0, 31):
		var_nc.append(sqrt(power(var_u[i, ix, iy], 2) + power(var_v[i, ix, iy], 2)))
	v_max = max(var_nc[1:30])
	v_min = min(var_nc[1:30])
	valor = var_nc[iz]
	if valor <= 1:
		cor = 
	elif valor >= 10: 
		cor =   
	else:
		cor =  

	return(valor, v_max, v_min, cor)
