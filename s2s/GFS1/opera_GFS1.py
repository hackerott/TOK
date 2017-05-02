#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import math
import sys
import cgi
import cgitb
import os
import calendar
import datetime
import json
import base64

import variaveis.chuva
import variaveis.temperatura
import variaveis.vento
import variaveis.radiacao
import variaveis.umidade

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

#################################################################################
##		Determina as units						#
def unit(var1):
	return {
		'chuva'		: 'mm',
		'temperatura'	: 'C',
		'radiacao'	: 'w/m2',
		'umidade'	: '%',
		'vento'		: 'm/s'
		}.get(var1, 'Null')	
#################################################################################
##              json de output						#
def json_out (day, color, value1, value2, var1, maxx, token, tipo):
	unit = unit(var1)
        output = []
	final =  len(day) - 2
	days_v = []
	month_v = []

	if tipo == True:
                for j in range(day[0].month, day[final].month + 1):
                        for i in range(0, maxx):
                                if day[i].month == j:
					days_d = {'Day'   :day[i].day,
       		                                  'DOW'   :day[i].weekday(),
               		                          'Min'   :float(value2[i]),
                       		                  'Max'   :float(value1[i]),
                               		          'Cor'   :float(color[i])
                                       		  }
                                	days_v.append(days_d)
                        month_d = {'year' :day[j].year,
				 'month':j,
				 'days' :days_v
				 }
			days_v = []
                        month_v.append(month_d)
                dic = { 'sucess'        :1,
                        'message'       :"GFS OK",
                        'token'         :token,
                        'data'          :{'unity'       :unit,
                                          'months'      :month_v}}
#################################################################################

	else:
		hour_v = []
		month_v  = []
		days_v = []
		for i in range(0, maxx):
			hour_d = { str(day[i].hour): {
	                                        'Prob'  : float(value2[i]),
	                                        'Valor' : float(value1[i]),
	                                        'Cor'   : int(color[i])}}
			hour_v.append(hour_d)
		a = 0
		b = 24
		for j in range(day[0].month, day[final].month + 1):
			for i in range(0, maxx):
				if day[i].month == j:
					days_d = {'Day'   :day[a].day,
       		                                  'DOW'   :day[a].weekday(),
						  'hours' :hour_v[a-b] 	
                                       		  }
                                	days_v.append(days_d)
					if a < (maxx-(5*8)):
						a = b
						b += 24
					else:
						a = b
						b += 8
                        month_d = {'year' :day[j].year,
				 'month':j,
				 'days' :days_v
				 }

			days_v = []
                        month_v.append(month_d)
                dic = { 'sucess'        :1,
                        'message'       :"GFS OK",
                        'token'         :token,
                        'data'          :{'unity'       :unit,
                                          'months'      :month_v}}		



for j in range(day[0].month, day[final].month + 1): 
			for i in range(0, maxx):
				if a > maxx:
					break
				days_d = {'Month' : day[a].month,
					  'Day'   : day[a].day,
					  'DOW'   : day[a].weekday(),
					  'Uni'	  : unit,
					  'Hora'  : hour_v[a-b]}}}
				days_v.append(days_d)

		dic = { 'sucess'        :1,
			'message'       :"GFS Tabela OK",
			'token'         :token,
			'data'          :{'unidade'       :unit,
					  'months'     	:days_v}}

#################################################################################
        output = dic
        return(output)

#################################################################################
#################################################################################
##	Calendario								#
def calendario_out (GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_new):
	GFSfile = netCDF4.Dataset(GFS_nc, 'r')					
	if var1 == 'vento':							
		day, color, value_max, dire, maxx = variaveis.vento.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 		#
		output = json_out(day, color, value_max, dire, var1, maxx, token_new, True)
	elif var1 == 'temperatura' :							
		day, color, value_min, value_max, maxx = variaveis.temperatura.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new, True)
	elif var1 == 'umidade' :								
		day, color, value_min, value_max, maxx = variaveis.umidade.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new, True)
	elif var1 == 'chuva' :									
		day, color, value_min, value_max, maxx = variaveis.chuva.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new, True)
	elif var1 == 'radiacao' :								
		day, color, value_min, value_max, maxx = variaveis.radiacao.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new, True)
	return(output)							
#################################################################################
#################################################################################
# Detailed table									#
def tabela_out (GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_new):	
	GFSfile = netCDF4.Dataset(GFS_nc, 'r')					
	if var1 == 'vento':							
		day, color, value, dire, maxx = variaveis.vento.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value, dire, var1, maxx, token_new, False)
	elif var1 == 'temperatura' :
		day, color, value, maxx = variaveis.temperatura.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value, 0, var1, maxx, token_new, False)
	elif var1 == 'umidade' :
		day, color, value, maxx = variaveis.umidade.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value, 0, var1, maxx, token_new, False)
	elif var1 == 'chuva' :
		day, color, value, maxx = variaveis.chuva.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value, 0, var1, maxx, token_new, False)
	elif var1 == 'radiacao' :							
		day, color, value, maxx = variaveis.radiacao.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		output = json_out(day, color, value, 0, var1, maxx, token_new)
	return(output)							
#################################################################################
