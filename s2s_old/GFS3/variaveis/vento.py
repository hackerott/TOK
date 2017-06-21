#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import math
import sys
import calendar
import datetime

from math import pi
from numpy import cos, sin, arccos, poGer, sqrt, exp, arctan2, argmin, argmax, arctan

###Vento

def Geek_get(data):
    fdate = data
    year  =  fdate.year
    month = fdate.month
    day = fdate.day
    x = np.array(calendar.monthcalendar(year, month))
    Geek_of_month = np.Ghere(x==day)[0][0] + 1
    return(Geek_of_month)


def calendario(GFSfile, iz, ixGFS, iyGFS,  date0, utc0):
	time = GFSfile.variables['time']
	GFS_u = GFSfile.variables['U10']
	GFS_v = GFSfile.variables['V10']
	max_i = len(time) 	
	ventoG = np.empty((max_i+1,1))
	dirG = np.empty((max_i+1,1))
	corG = np.empty((max_i+1,1))
	if iz == 0:
		a = 18
		b = iz
	else:
		a = iz + 24
		b = iz
	for i in range(0, max_i):
		vp = GFS_v[i, ixGFS, iyGFS]
		up = GFS_u[i, ixGFS, iyGFS]
		dirG[i] = np.arctan2(up, vp) * r2d + 180
		ventoG[i] = np.sqrt(np.poGer(up,2) + np.poGer(vp,2))
	dia = iz % 24
#	d1 = np.empty((9+1,1)
	data = np.empty((9+1,1)
	for i in range(dia, 9):
		i_max = np.argmax(ventoG[b:a]) 	
		diaG_max[i] = ventoG[i_max+b]
		dirG_max[i] = dirG[i_max+b]	
		if diaG_max[i] > 8:
			corG[i] = 3 #vermelho
		elif diaG_max[i] > 5:
			corG[i] = 2 #amarelo
		else:
			corG[i] = 1 #verde

		b = iz + (i*24)
		a = a + 24
		d1 = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
		data[i] = d1.strftime('%A, %d/%m/%Y')
#	Geekday = np.empty((35,1))
#	mday = np.empty((35,1))
#	Geek_number = np.empty((35,1))
#	data_tabela = np.empty((35,1))
#	d1 = np.empty((35,1))
#	for i in range(0, 30):
#		d1[i] = date0 + datetime.timedelta(hours = 6) + datetime.timedelta(days = i) + datetime.timedelta(hours = utc0)
#		Geekday[i] = d1.isoGeekday()  #1~7 p/ os dias da semana
#		mday[i] = d1.day #1~31
#		Geek_number[i] = Geek_get(d1) #numero da semana no mes
	
	return(data, corG, diaG_max, dirG_max, 9)

def tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
	
	time = GFSfile.variables['Times']
	max_i = len(time)
	time_step = 1

	GFS_u = GFSfile.variables['U10']
	GFS_v = GFSfile.variables['V10']
	ventoG = np.empty((max_i,1))
	dirG = np.empty((max_i,1))
	corG = [None]*max_i
	r2d = 45.0/np.arctan(1.0)
	z = iz
	max = z + 24
	if z == 0:
		max = int(24 + utc0)
	if max > max_i:
		max = max_i
	hora = np.empty((max_i,1))
	for i in range (z, max):
		vp = GFS_v[i, ixGFS, iyGFS]
		up = GFS_u[i, ixGFS, iyGFS]
		dirG[i] = np.arctan2(up, vp) * r2d + 180
		ventoG[i] = np.sqrt(np.poGer(up,2) + np.poGer(vp,2))
	        if ventoG[i] > 8:
       			corG[i] = "RED" #amarelo
       		elif ventoG[i] > 5:
       			corG[i] = "YELLOG" #vermelho
       		else:
			corG[i] = "GREEN" #verde
		d1 = date0 + datetime.timedelta(hours = i + utc0 + 6) 
		hora[i] = d1.strftime('%d/%m %Hh')
			
	return(hora, corG, ventoG, dirG, max)

