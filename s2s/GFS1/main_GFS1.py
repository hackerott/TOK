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
form = cgi.FieldStorage()		#
					#
lat1 = form.getvalue("lat")		#
lon1 = form.getvalue("lon")		#
utc1 = form.getvalue("utc")		#
var1 = form.getvalue("var")		#
date1 = form.getvalue("data")		#
tipo1 = form.getvalue("tipo")		#
token1 = form.getvalue("token")		#
id1 = form.getvalue("id")		#
ip1  = os.environ["REMOTE_ADDR"]	#
#########################################
#########################################################
##	variaveis iniciais				#
date0 = datetime.datetime.strptime(date1, '%Y%m%d')	#
lat0 = float(lat1)					#
lon0 = float(lon1)					#
utc0 = int(utc1)					#
#########################################################

########################## Funcoes ######################################################

#########################################################################################
##		json de resposta							#
def json_out (dia, cor, valor1, valor2, var1, maxx):					#
	resposta = np.empty((maxx+1,1))							#
	for i in range(iz, maxx):							#
		if valor2==0:								#
			resposta[i] = var1, dia[i], cor[i], valor1[i]			#
		else:									#
			resposta[i] = var1, dia[i], cor[i], valor1[i], valor2[i]	#
	return(resposta)								#
#########################################################################################
###########################################################################################################################
# Calendario
def calendario_out (GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_novo):
	GFSfile = netCDF4.Dataset(GFS_nc, 'r')
	if var1 == 'vento':
		dia, cor, valor_max, dire, maxx = variaveis.vento.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, dire, var1, maxx, token_novo)
	elif var1 == 'temperatura' :
		dia, cor, valor_min, valor_max, maxx = variaveis.temperatura.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, valor_min, var1, maxx, token_novo)
	elif var1 == 'umidade' :
		dia, cor, valor_min, maxx = variaveis.umidade.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_min, 0, var1, maxx, token_novo)
	elif var1 == 'chuva' :	
		dia, cor, valor, maxx = variaveis.chuva.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	elif var1 == 'radiacao' :
		dia, cor, valor, maxx = variaveis.radiacao.calendario(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)

	return(resposta)
###########################################################################################################################
# Tabela
def tabela_out (GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_novo):
	GFSfile = netCDF4.Dataset(GFS_nc, 'r')
	if var1 == 'vento':
		dia, cor, valor, dire, maxx = variaveis.vento.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor_max, dire, var1, maxx, token_novo)
	elif var1 == 'temperatura' :
		dia, cor, valor, maxx = variaveis.temperatura.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	elif var1 == 'umidade' :
		dia, cor, valor, maxx = variaveis.umidade.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	elif var1 == 'chuva' :	
		dia, cor, valor, maxx = variaveis.chuva.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)
	elif var1 == 'radiacao' :
		dia, cor, valor, maxx = variaveis.radiacao.tabela(GFSfile, iz, ixGFS, iyGFS, date0, utc0) 
		resposta = json_out(dia, cor, valor, 0, var1, maxx, token_novo)

	return(resposta)
###########################################################################################################################

###################### Operacao #########################################################

#########################################################################################
##	verifica o token e o id da requisição						#
token_db, id_db = mysql_access.token_get(id1)						#
											#
if token1 != token_db or id1 != id_db :							#
	tipo1 == error									#
	data_erro = datetime.datetime.now()						#
	print >> error.log, "%s tentou acessar a api WRF, %s" % (ip1, data_erro)	#
#########################################################################################
#########################################################################################
##	gera o novo token e guardo no banco						#
else: 											#
	hash0 = os.urandom(16)								#
	hash1 = base64.b64encode(hash0).decode('utf-8')					#
	token_status = mysql_access.token_update(hash1, id1)				#
	if token_status != true:							#
#		token_status = mysql_access.token_update(hash1, id1)			#
		data_erro = datetime.datetime.now()					#
		token_novo = token1							#
		print >> error.log, "Falha na atualização do token, %s" (data_erro)	#
 	else:										#
		token_novo = hash1							#
#########################################################################################
#########################################################################################
##	Checa a existencia do arquivo .nc						#
arquivo = "/var/www/html/processamento/GFSD20101"+date1+"00.nc"				#
arquivo1 = arquivo									#
while os.path.isfile(arquivo) != True:							#
		date1 = date1 + datetime.timedelta(days = -1)				#
		arquivo = "/var/www/html/processamento/GFSD20101"+date1+"00.nc"		#	
		iz += 24								#
		brk +=1									#
		if brk == 3:								#
			arquivo = False							#
			break								#
#########################################################################################
#################################################################
if arquivo != False:						#
	GFS_nc = arquivo					#
	GFSfile = netCDF4.Dataset(GFS_nc, 'r')			#
	latGFS = GFSfile.variables['latitude']			#	
	lonGFS = GFSfile.variables['longitude']			#
#################################################################
#########################################################################
##	localiza lat e lon						#
	ixGFS, iyGFS = lat_lon.GFS_get(latGFS, lonGFS, lat0, lon0)	#
#########################################################################
#########################################################################################################
##	separa e chama 											#
	if tipo1 == True:										#
		resposta = calendario_out(GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_novo)	#
		print json.dumps(resposta)								#
	elif tipo1 == False:										#
		resposta = tabela_out(GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_novo)		#
		print json.dumps(resposta)								#
##	Erro de login											#
	elif tipo1 == Error:										#
		print json.dumps(""" Erro de autenticação """)						#
#########################################################################################################
#################################################
##	guarda os tokens gerados		#
	token = open('token', 'r+')		#
	token.write(hash1)			#
	token.close()				#
################################################# 
#########################################################################################
else:											#
	data_erro = datetime.datetime.now()						#
	print >> error.log, "%s arquivo nao existe %s" % (data_erro, arquivo1)		#	
	print json.dumps(""" Erro modelo indisponivel """)				#
	exit()										#
#########################################################################################
##########################################
###	leitura da json			#
#					#
#form = cgi.FieldStorage()		#
#					#
#input = json.load(form)		# 
#					#
#lat1 = input[GFS][latitude]		#
#lon1 = input[GFS][longitude]		#
#utc1 = input[GFS][utc]			#
#var1 = input[GFS][variavel]		#
#date1 = input[GFS][data]		#
#tipo1 = input[GFS][tipo][calendario]	#
#					#
##########################################
