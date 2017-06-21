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
#import ../prob_area as prob_area
#import ../prob_time as prob_time
import ../meteo_var as meteo_var

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
##		json de output							#
def _json_out (day, color, value1, value2, var1, maxx, token):
	output = []
	month_v	 = []
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

		month_d = {'year' :day[j].year,
 			 'month':j,
			 'days' :days_v
			 }
		days_v = []
		month_v.append(month_d)
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
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'temperatura' :
		day, value_min, color, value_max, maxx = variaveis.temperatura.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'umidade' :
		day, value_min, color, value_max, maxx = variaveis.umidade.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'chuva' :	
		day, value_min, color, value_max, maxx = variaveis.chuva.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'radiacao' :
		day, value_min, color, value_max, maxx = variaveis.radiacao.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
#	print "🌡 ☁️ 🌁 🌫 ☂ 💧 ⛅ ☀️ 🌀 🍃 💨"
	return(output)
#################################################################################
def calendario_stat_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, iz, ixCFS, iyCFS, date0, utc0, token_new, ):
	if var1 == 'vento':
		top_lim, bot_lim, prob_lim = variaveis.vento.prob_limits()
		day, value_min, color, value_max, maxx = meteo_var.calendar(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0, var1, top_lim, bot_lim, prob_lim) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'temperatura' :
		top_lim, bot_lim, prob_lim = variaveis.temeperatura.prob_limits()
		day, value_min, color, value_max, maxx = meteo_var.calendar(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0, var1, top_lim, bot_lim, prob_lim) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'umidade' :
		top_lim, bot_lim, prob_lim = variaveis.umidade.prob_limits()
		day, value_min, color, value_max, maxx = meteo_var.calendar(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0, var1, top_lim, bot_lim, prob_lim) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'chuva' :	
		top_lim, bot_lim, prob_lim = variaveis.chuva.prob_limits()
		day, value_min, color, value_max, maxx = meteo_var.calendar(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0, var1, top_lim, bot_lim, prob_lim) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
	elif var1 == 'radiacao' :
		top_lim, bot_lim, prob_lim = variaveis.radiacao.prob_limits()
		day, value_min, color, value_max, maxx = meteo_var.calendar(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0, var1, top_lim, bot_lim, prob_lim) 
		output = _json_out(day, color, value_max, value_min, var1, maxx, token_new)
#	print "🌡 ☁️ 🌁 🌫 ☂ 💧 ⛅ ☀️ 🌀 🍃 💨"
	return(output)
#################################################################################








