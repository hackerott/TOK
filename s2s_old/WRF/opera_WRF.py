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

#import lat_lon
import variaveis
#import mysql_access

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

#################################################################################################
##		json de resposta								#
												#
def json_out (dia, cor, valor1, valor2, var1, maxx, token_novo):				#
	resposta = np.empty((maxx+1,1))								#
	for i in range(iz, maxx):								#
		if valor2==0:									#
			resposta[i] = var1, dia[i], cor[i], valor1[i], token_novo		#
		else:										#
			resposta[i] = var1, dia[i], cor[i], valor1[i], valor2[i], token_novo	#
												#
	return(resposta)									#
												#
#################################################################################################
###########################################################################################################################
##	Calendario
def tabela_out (WRF_nc, var1, iz, ixWRF, iyWRF, date0, utc0, token_novo):
	WRFfile = netCDF4.Dataset(WRF_nc, 'r')
	if var1 == 'vento':
		dia, cor, valor_max, dire, maxx = variaveis.vento.calendario(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, dire, var1, maxx, token_novo)
	elif var1 == 'temperatura' :
		dia, cor, valor_min, valor_max, maxx = variaveis.temperatura.calendario(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo)
	elif var1 == 'umidade' :
		dia, cor, valor_min, maxx = variaveis.umidade.calendario(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
 		resposta = json_out(dia, cor, valor_min, 0, var1, maxx, token_novo)
	elif var1 == 'chuva' :	
		dia, cor, valor, maxx = variaveis.chuva.calendario(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	elif var1 == 'radiacao' :
		dia, cor, valor, maxx = variaveis.radiacao.calendario(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	return(resposta)
###########################################################################################################################
##	Tabela
def tabela_out (WRF_nc, var1, iz, ixWRF, iyWRF, date0, utc0, token_novo):
	WRFfile = netCDF4.Dataset(WRF_nc, 'r')
	if var1 == 'vento':
		dia, cor, valor, dire, maxx = variaveis.vento.tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, dire, var1, maxx, token_novo)
	elif var1 == 'temperatura' :
		dia, cor, valor, maxx = variaveis.temperatura.tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	elif var1 == 'umidade' :
		dia, cor, valor, maxx = variaveis.umidade.tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	elif var1 == 'chuva' :	
		dia, cor, valor, maxx = variaveis.chuva.tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	elif var1 == 'radiacao' :
		dia, cor, valor, maxx = variaveis.radiacao.tabela(WRFfile, iz, ixWRF, iyWRF, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	return(resposta)
###########################################################################################################################
