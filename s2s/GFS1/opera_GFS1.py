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
##		Determina as unidades						#
def unidade(var1):
	return {
		'chuva'		: 'mm',
		'temperatura'	: 'C',
		'radiacao'	: 'w/m2',
		'umidade'	: '%',
		'vento'		: 'm/s'
		}.get(var1, 'Null')	
#################################################################################
##              json de resposta						#
def json_out (dia, cor, valor1, valor2, var1, maxx, token, tipo):
	unit = unidade(var1)
        resposta = []
	final =  len(dia) - 2
	dias_v = []
	mes_v = []

	if tipo == True:
                for j in range(dia[0].month, dia[final].month + 1):
                        for i in range(0, maxx):
                                if dia[i].month == j:
					dias_d = {'Day'   :dia[i].day,
       		                                  'DOW'   :dia[i].weekday(),
               		                          'Min'   :float(valor2[i]),
                       		                  'Max'   :float(valor1[i]),
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
                        'message'       :"GFS OK",
                        'token'         :token,
                        'data'          :{'unity'       :unit,
                                          'months'      :mes_v}}
#################################################################################

	else:
		hora_v = []
		mes_v  = []
		dias_v = []
		for i in range(0, maxx):
			hora_d = { str(dia[i].hour): {
	                                        'Prob'  : float(valor2[i]),
	                                        'Valor' : float(valor1[i]),
	                                        'Cor'   : int(cor[i])}}
			hora_v.append(hora_d)
		a = 0
		b = 24
		for j in range(dia[0].month, dia[final].month + 1):
			for i in range(0, maxx):
				if dia[i].month == j:
					dias_d = {'Day'   :dia[a].day,
       		                                  'DOW'   :dia[a].weekday(),
						  'Horas' :hora_v[a-b] 	
                                       		  }
                                	dias_v.append(dias_d)
					if a < (maxx-(5*8)):
						a = b
						b += 24
					else:
						a = b
						b += 8
                        mes_d = {'year' :dia[j].year,
				 'month':j,
				 'days' :dias_v
				 }

			dias_v = []
                        mes_v.append(mes_d)
                dic = { 'sucess'        :1,
                        'message'       :"GFS OK",
                        'token'         :token,
                        'data'          :{'unity'       :unit,
                                          'months'      :mes_v}}		



for j in range(dia[0].month, dia[final].month + 1): 
			for i in range(0, maxx):
				if a > maxx:
					break
				dias_d = {'Month' : dia[a].month,
					  'Day'   : dia[a].day,
					  'DOW'   : dia[a].weekday(),
					  'Uni'	  : unidade,
					  'Hora'  : hora_v[a-b]}}}
				dias_v.append(dias_d)

		dic = { 'sucess'        :1,
			'message'       :"GFS Tabela OK",
			'token'         :token,
			'data'          :{'unity'       :unit,
					  'months'     	:dias_v}}

#################################################################################
        resposta = dic
        return(resposta)

#################################################################################
#################################################################################
##	Calendario								#
def calendario_out (GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_novo):
	GFSfile = netCDF4.Dataset(GFS_nc, 'r')					
	if var1 == 'vento':							
		dia, cor, valor_max, dire, maxx = variaveis.vento.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 		#
		resposta = json_out(dia, cor, valor_max, dire, var1, maxx, token_novo, True)
	elif var1 == 'temperatura' :							
		dia, cor, valor_min, valor_max, maxx = variaveis.temperatura.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo, True)
	elif var1 == 'umidade' :								
		dia, cor, valor_min, valor_max, maxx = variaveis.umidade.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo, True)
	elif var1 == 'chuva' :									
		dia, cor, valor_min, valor_max, maxx = variaveis.chuva.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo, True)
	elif var1 == 'radiacao' :								
		dia, cor, valor_min, valor_max, maxx = variaveis.radiacao.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo, True)
	return(resposta)							
#################################################################################
#################################################################################
# Tabela									#
def tabela_out (GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_novo):	
	GFSfile = netCDF4.Dataset(GFS_nc, 'r')					
	if var1 == 'vento':							
		dia, cor, valor, dire, maxx = variaveis.vento.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor, dire, var1, maxx, token_novo, False)
	elif var1 == 'temperatura' :
		dia, cor, valor, maxx = variaveis.temperatura.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo, False)
	elif var1 == 'umidade' :
		dia, cor, valor, maxx = variaveis.umidade.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo, False)
	elif var1 == 'chuva' :
		dia, cor, valor, maxx = variaveis.chuva.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo, False)
	elif var1 == 'radiacao' :							
		dia, cor, valor, maxx = variaveis.radiacao.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0)
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	return(resposta)							
#################################################################################
