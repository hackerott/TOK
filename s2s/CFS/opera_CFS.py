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
##		json de resposta						#
def json_out (dia, cor, valor1, valor2, var1, maxx, token):
	resposta = []
	mes_v	 = []
	dias_v	 = []
	final	 = len(dia) - 2
	unit	 = unidade(var1)
	for j in range(dia[0].month, dia[final].month + 1):
		for i in range(0, maxx):
			if dia[i].month == j:
				dias_d = {'Day'   :dia[i].day,
					  'DOW'   :dia[i].weekday(),
					  'Prob'  :float(valor2[i]),
					  'Valor' :float(valor1[i]),
					  'Cor'   :float(cor[i])
					 }
				dias_v.append(dias_d)
		mes_d = {'year' :dia[j].year,
 			 'month':j,
			 'days' :dias_v
			 }
		dias_v = []
		mes_v.append(mes_d)
	dic = { 'sucess'        :1,
		'message'       :"CFS OK",
		'token'         :token,
		'data'          :{'unity'       :unit,
		'months'      :mes_v
				 }
		}
	resposta = dic 
	return(resposta)
#################################################################################
#################################################################################
##	separa e chama as variaveis						#
def calendario_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, iz, ixCFS, iyCFS, date0, utc0, token_novo):
	if var1 == 'vento':
		dia, valor_min, cor, valor_max, maxx = variaveis.vento.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo)
	elif var1 == 'temperatura' :
		dia, valor_min, cor, valor_max, maxx = variaveis.temperatura.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo)
	elif var1 == 'umidade' :
		dia, valor_min, cor, valor_max, maxx = variaveis.umidade.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo)
	elif var1 == 'chuva' :	
		dia, valor_min, cor, valor_max, maxx = variaveis.chuva.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo)
	elif var1 == 'radiacao' :
		dia, valor_min, cor, valor_max, maxx = variaveis.radiacao.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo)
#	print "🌡 ☁️ 🌁 🌫 ☂ 💧 ⛅ ☀️ 🌀 🍃 💨"
	return(resposta)
#################################################################################
