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

import lat_lon
import variaveis
import mysql_access

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

#########################################
##	leitura do form			#
					#
form = cgi.FieldStorage()		#
					#
					#
lat1 = form.getvalue[latitude]		#
lon1 = form.getvalue[longitude]		#
utc1 = form.getvalue[utc]		#
var1 = form.getvalue[variavel]		#
date1 = form.getvalue[data]		#
tipo1 = form.getvalue[tipo]		#
token1 = form.getvalue[token]		#
id1 = form.getvalue[id]			#
ip1  = os.environ["REMOTE_ADDR"]	#
#########################################
#########################################################
##	variaveis iniciais				#
#date0 = datetime.datetime.strptime(date1, '%Y%m%d')	#
lat0 = float(lat1)					#
lon0 = float(lon1)					#
utc0 = int(utc1)					#
#########################################################
#funcoes
#########################################################################################
##		json de resposta							#
											#
def json_out (dia, cor, valor1, valor2, var1, maxx):					#
	out = np.empty((maxx+1,1))							#
	for i in range(iz, maxx):							#
		if valor2==0:								#
			out[i] = var1, dia[i], cor[i], valor1[i]			#
		else:									#
			out[i] = var1, dia[i], cor[i], valor1[i], valor2[i]	#
											#
	return(out)								#
											#
#########################################################################################
###########################################################################################################################
##	separa e chama as variaveis
def calendario_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, iz, ixCFS, iyCFS, date0, utc0, token_novo):
	if var1 == 'vento':
		dia, cor, valor_max, dire, maxx = variaveis.vento.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		out = json_out(dia, cor, valor_max, dire, var1, maxx, token_novo)
		print json.dumps(out)

	elif var1 == 'temperatura' :
		dia, cor, valor_min, valor_max, maxx = variaveis.temperatura.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		out = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo)
		print json.dumps(out)

	elif var1 == 'umidade' :
		dia, cor, valor_min, maxx = variaveis.umidade.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		out = json_out(dia, cor, valor_min, 0, var1, maxx, token_novo)
		print json.dumps(out)
	elif var1 == 'chuva' :	
		dia, cor, valor, maxx = variaveis.chuva.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		out = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
		print json.dumps(out)

	elif var1 == 'radiacao' :
		dia, cor, valor, maxx = variaveis.radiacao.calendario(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, iz, ixCFS, iyCFS, date0, utc0) 
		out = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
		print json.dumps(out)
###########################################################################################################################
#execucao
#########################################################################################
##	verifica o token e o id da requisição						#
token_db, id_db = mysql_access.token_get(id1)						#
											#
if token1 != token_db or id1 != id_db :							#
	tipo1 == error									#
	data_erro = datetime.datetime.now()						#
	print >> error.log, "%s tentou acessar a api WRF, %s" % (ip1, data_erro)	#
	print json.dumps(""" Erro de autenticação """)					#
#	exit()										#	
#########################################################################################
#########################################################################################
##	gera o novo token e guardo no banco						#
else 											#
	hash0 = os.urandom(16)								#
	hash1 = base64.b64encode(hash0).decode('utf-8')					#
	token_status = mysql_access.token_update(hash1, id1)				#
	if token_status != true:							#
		data_erro = datetime.datetime.now()					#
		token_novo = token1							#
		print >> error.log, "Falha na atualização do token, %s" (data_erro)	#
 	else:										#
		token_novo = hash1							#
#########################################################################################
#########################################################################
##	Checa a existencia do arquivo .nc				#
date0 = datetime.datetime.strptime(date1, '%Y%m%d')			#
date2 = date0 + datetime.timedelta(days = -1)				#
									#
ens1 = "/var/www/html/processamento/CFSD20101"+date0+"00.nc"		#
ens2 = "/var/www/html/processamento/CFSD20102"+date0+"00.nc"		#
ens3 = "/var/www/html/processamento/CFSD20103"+date0+"00.nc"		#
ens4 = "/var/www/html/processamento/CFSD20104"+date0+"00.nc"		#
									#
ens5 = "/var/www/html/processamento/CFSD20101"+date2+"00.nc"		#
ens6 = "/var/www/html/processamento/CFSD20102"+date2+"00.nc"		#
ens7 = "/var/www/html/processamento/CFSD20103"+date2+"00.nc"		#
ens8 = "/var/www/html/processamento/CFSD20104"+date2+"00.nc"		#
									#
while os.path.isfile(ens1) != True:					#
	date0 = date0 + datetime.timedelta(days = -1)			#
	date2 = date2 + datetime.timedelta(days = -1)			#
	iz += 4								#
	ens1 = "/var/www/html/processamento/CFSD20101"+date0+"00.nc"	#
	ens2 = "/var/www/html/processamento/CFSD20102"+date0+"00.nc"	#
	ens3 = "/var/www/html/processamento/CFSD20103"+date0+"00.nc"	#
	ens4 = "/var/www/html/processamento/CFSD20104"+date0+"00.nc"	#
	ens5 = "/var/www/html/processamento/CFSD20101"+date2+"00.nc"	#
	ens6 = "/var/www/html/processamento/CFSD20102"+date2+"00.nc"	#
	ens7 = "/var/www/html/processamento/CFSD20103"+date2+"00.nc"	#
	ens8 = "/var/www/html/processamento/CFSD20104"+date2+"00.nc"	#
	brk +=1								#
	if brk == 3:							#
		arquivo = False						#
		break							#
#########################################################################
##	Se o arquivo existe execuyta as chamadas
if arquivo != False:
	CFS_nc = ens1	
	CFSfile = netCDF4.Dataset(CFS_nc, 'r')
	latCFS = CFSfile.variables['latitude']	
	lonCFS = CFSfile.variables['longitude']
#localiza lat e lon
	ixCFS, iyCFS = lat_lon.CFS_get(latCFS, lonCFS, lat0, lon0)
#chama o calendario
	if tipo1 == True:
		out = calendario_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, iz, ixCFS, iyCFS, date0, utc0, token_novo)
		print json.dumps(out)
#erro no login
	elif tipo1 == error:					
		print json.dumps(""" Erro de autenticação """)	
#solicitar a tabela
	else:
		print json.dumps(""" Funcao indispo nivel""")						
###########################################################################################################################
#########################################################################################
else:											#
	data_erro = datetime.datetime.now()						#
	print >> error.log, "%s arquivo nao existe %s" % (data_erro, arquivo1)		#	
	print json.dumps(""" Erro modelo indisponivel """)				#
	exit()										#
#########################################################################################
#########################################
##	guarda os tokens gerados	#
					#
token = open('token', 'r+')		#
token.write(hash1)			#
token.close()				#
#########################################
