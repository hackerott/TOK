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
##		define unidade 							#
def unidade(var1):
	return {
		'chuva'		: 'mm',
		'temperatura'	: 'C',
		'radiacao'	: 'w/m2',
		'umidade'	: '%',
		'vento'		: 'm/s'
		}.get(var1, 'Null')
#################################################################################
#################################################################################
<<<<<<< HEAD
##		json de output						#
def json_out (day, color, value1, value2, var1, maxx, token):
	output = []
	month_v	 = []
=======
##		json de resposta						#
def json_out (day, color, value1, value2, var1, maxx, token):
	output = []
	mes_v	 = []
>>>>>>> f8ed1d5d4bfcc0dfe079134f4be0d03f0a6c3dfe
	days_v	 = []
	final	 = len(day) - 2
	unit	 = unidade(var1)
	for j in range(day[0].month, day[final].month + 1):
		for i in range(0, maxx):
			if day[i].month == j:
				days_d = {'Day'   :day[i].day,
					  'DOW'   :day[i].weekday(),
					  'Prob'  :float(value2[i]),
					  'value' :float(value1[i]),
					  'color'   :float(color[i])
					 }
				days_v.append(days_d)
<<<<<<< HEAD
		month_d = {'year' :day[j].year,
=======
		mes_d = {'year' :day[j].year,
>>>>>>> f8ed1d5d4bfcc0dfe079134f4be0d03f0a6c3dfe
 			 'month':j,
			 'days' :days_v
			 }
		days_v = []
<<<<<<< HEAD
		month_v.append(month_d)
=======
		mes_v.append(mes_d)
>>>>>>> f8ed1d5d4bfcc0dfe079134f4be0d03f0a6c3dfe
	dic = { 'sucess'        :1,
		'message'       :"CFS OK",
		'token'         :token,
		'data'          :{'unity'       :unit,
		'months'      :month_v
				 }
		}
	output = dic 
	return(output)
#################################################################################
#################################################################################
##	calls all variables						#
def calendario_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, iz, ixCFS, iyCFS, date0, utc0, token_new):
	if var1 == 'vento':
		day, value_min, color, value_max, maxx = variaveis.vento.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
<<<<<<< HEAD
		output = json_out(day, color, value_max, value_min, var1, maxx, token_novo)
	elif var1 == 'temperatura' :
		day, value_min, color, value_max, maxx = variaveis.temperatura.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = json_out(day, color, value_max, value_min, var1, maxx, token_novo)
	elif var1 == 'umidade' :
		day, value_min, color, value_max, maxx = variaveis.umidade.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = json_out(day, color, value_max, value_min, var1, maxx, token_novo)
	elif var1 == 'chuva' :	
		day, value_min, color, value_max, maxx = variaveis.chuva.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = json_out(day, color, value_max, value_min, var1, maxx, token_novo)
	elif var1 == 'radiacao' :
		day, value_min, color, value_max, maxx = variaveis.radiacao.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = json_out(day, color, value_max, value_min, var1, maxx, token_novo)
=======
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'temperatura' :
		day, value_min, color, value_max, maxx = variaveis.temperatura.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'umidade' :
		day, value_min, color, value_max, maxx = variaveis.umidade.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'chuva' :	
		day, value_min, color, value_max, maxx = variaveis.chuva.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'radiacao' :
		day, value_min, color, value_max, maxx = variaveis.radiacao.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = json_out(day, color, value_max, value_min, var1, maxx, token_new)
>>>>>>> f8ed1d5d4bfcc0dfe079134f4be0d03f0a6c3dfe
#	print "🌡 ☁️ 🌁 🌫 ☂ 💧 ⛅ ☀️ 🌀 🍃 💨"
	return(output)
#################################################################################
