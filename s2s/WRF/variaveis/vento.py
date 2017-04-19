#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import math
import sys
import calendar
import datetime

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

###Vento

def week_get(data):
    fdate = data
    year  =  fdate.year
    month = fdate.month
    day = fdate.day
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)


def calendario(WRFfile, iz, ixWRF, iyWRF,  date0, utc0):
	time = WRFfile.variables['time']
	WRF_u = WRFfile.variables['U10']
	WRF_v = WRFfile.variables['V10']
	max_i = len(time) 	
	ventoW = np.empty((max_i+1,1))
	dirW = np.empty((max_i+1,1))
	corW = np.empty((max_i+1,1))
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz
	for i in range(0, max_i):
		vp = WRF_v[i, ixWRF, iyWRF]
		up = WRF_u[i, ixWRF, iyWRF]
		dirW[i] = np.arctan2(up, vp) * r2d + 180
		ventoW[i] = np.sqrt(np.power(up,2) + np.power(vp,2))
	dia = iz % 24
	maxx = max_i % 24
#	d1 = np.empty((9+1,1)
	data = np.empty((maxx+1,1)
	for i in range(dia, maxx):
		i_max = np.argmax(ventoW[b:a]) 	
		diaW_max[i] = ventoW[i_max+b]
		dirW_max[i] = dirW[i_max+b]	
		if diaW_max[i] > 8:
			corW[i] = 3 #vermelho
		elif diaW_max[i] > 5:
			corW[i] = 2 #amarelo
		else:
			corW[i] = 1 #verde

		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data[i] = d1.strftime('%A, %d/%m/%Y')
#	weekday = np.empty((35,1))
#	mday = np.empty((35,1))
#	week_number = np.empty((35,1))
#	data_tabela = np.empty((35,1))
#	d1 = np.empty((35,1))
#	for i in range(0, 30):
#		d1[i] = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
#		weekday[i] = d1.isoweekday()  #1~7 p/ os dias da semana
#		mday[i] = d1.day #1~31
#		week_number[i] = week_get(d1) #numero da semana no mes
	
	return(data, corW, diaW_max, dirW_max, maxx

####################################################################################################################
##	Tabela

def tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0)
	
	time = WRFfile.variables['Times']
	max_i = len(time)
	time_step = 1

	WRF_u = WRFfile.variables['U10']
	WRF_v = WRFfile.variables['V10']
	ventoW = np.empty((max_i,1))
	dirW = np.empty((max_i,1))
	corW = [None]*max_i
	r2d = 45.0/np.arctan(1.0)
	z = iz
	max = z + 24
	if z == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = np.empty((max_i,1))
	for i in range (z, max):
		vp = WRF_v[i, ixWRF, iyWRF]
		up = WRF_u[i, ixWRF, iyWRF]
		dirW[i] = np.arctan2(up, vp) * r2d + 180
		ventoW[i] = np.sqrt(np.power(up,2) + np.power(vp,2))
	        if ventoW[i] > 8:
       			corW[i] = "RED" #amarelo
       		elif ventoW[i] > 5:
       			corW[i] = "YELLOW" #vermelho
       		else:
			corW[i] = "GREEN" #verde
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6) 
		hora[i] = d1.strftime('%d/%m %Hh')
			
	return(hora, corW, ventoW, dirW, max)

