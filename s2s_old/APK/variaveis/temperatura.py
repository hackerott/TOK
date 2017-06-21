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
	var_nc = nc.variables['tmp2m'] 
	v_max = max(var_nc[1:30, ix, iy])  - 273.15
	v_min = min(var_nc[1:30, ix, iy])  - 273.15
	valor = var_nc[iz, ix, iy] - 273.15
	if valor >= 23 :
		cor = 
	elif valor >= 30: 
		cor =   
	else:
		cor =  

	return(valor, v_max, v_min, cor)
