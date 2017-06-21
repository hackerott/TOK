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

import mysql_access

import WRF.opera_WRF
import WRF.lat_lon
import GFS1.opera_GFS1
import GFS1.lat_lon
import CFS.opera_CFS
import CFS.lat_lon


from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

#########################################
##	leitura do form			#
					#
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
					#
#########################################
#########################################################
##	variaveis iniciais				#
date0	= datetime.datetime.strptime(date1, '%Y%m%d')	#
lat0	= float(lat1)					#
lon0	= float(lon1)					#
utc0	= int(utc1)					#
wrf_iz	= 0						#
gfs_iz	= 0						#
cfs_iz	= 0						#
#########################################################
print "Content-type: application/json\n\n"
#########################################################################################
##	verifica o token e o id da requisição						#
token_db, id_db = mysql_access.token_get(id1)						#
if token1 != token_db:									#
	tipo1 = 'error'									#	
	data_erro = datetime.datetime.now()						#
	print """###### ERRO ######"""							#
	print "%s tentou acessar a api WRF, %s" % (ip1, data_erro)			#
	exit()										#
##	gera o novo token e guardo no banco						#
else: 											#
	hash0 = os.urandom(14)								#
	hash1 = base64.b64encode(hash0).decode('utf-8')					#
	token_status = mysql_access.token_update(hash1, id1)				#
	if token_status != True:							#
		data_erro = datetime.datetime.now()					#
		token_novo = token1							#
		print "Falha de atualizacao de token %s" % (data_erro)	>> error.log
 	else:										#
		token_novo = hash1							#
#########################################################################################

#################################################################################################
##	Checa a existencia do arquivo .nc de todos os modelos					#
## WRF, GFS, CFS, GRAF										#
date0 = datetime.datetime.strptime(date1, '%Y%m%d')						#
date2 = date0 + datetime.timedelta(days = -1)							#	
												#
wrf_file = "/var/www/html/processamento/WRFD20101"+date0.strftime('%Y%m%d')+"00.nc"		#	
gfs_file = "/var/www/html/processamento/GFSD10001"+date0.strftime('%Y%m%d')+"00.nc"		#
ens1	 = "/var/www/html/processamento/CFSD10001E1"+date0.strftime('%Y%m%d')+"00.nc"		#
ens2	 = "/var/www/html/processamento/CFSD10001E2"+date0.strftime('%Y%m%d')+"00.nc"		#
ens3	 = "/var/www/html/processamento/CFSD10001E3"+date0.strftime('%Y%m%d')+"00.nc"		#
ens4	 = "/var/www/html/processamento/CFSD10001E4"+date0.strftime('%Y%m%d')+"00.nc"		#
ens5	 = "/var/www/html/processamento/CFSD10001E1"+date2.strftime('%Y%m%d')+"00.nc"		#
ens6	 = "/var/www/html/processamento/CFSD10001E2"+date2.strftime('%Y%m%d')+"00.nc"		#
ens7	 = "/var/www/html/processamento/CFSD10001E3"+date2.strftime('%Y%m%d')+"00.nc"		#
ens8	 = "/var/www/html/processamento/CFSD10001E4"+date2.strftime('%Y%m%d')+"00.nc"		#
brk = 0												#
dateW = date0											#
dateG = date0											#
dateC = date0											#
while os.path.isfile(wrf_file) != True:								#
	dateW = dateW - datetime.timedelta(days = 1)						#
	wrf_file = "/var/www/html/processamento/WRFD20101"+dateW.strftime('%Y%m%d')+"00.nc"	#
	brk +=1											#
	if brk >= 3:										#
		wrf_file = False								#
		break										#
brk = 0												#
while os.path.isfile(gfs_file) != True:								#
	dateG = dateG - datetime.timedelta(days = 1)						#
	gfs_file = "/var/www/html/processamento/GFSD10001"+dateG.strftime('%Y%m%d')+"00.nc"	#	
	brk +=1											#
	if brk >= 3:										#
		gfs_file = False								#
		break										#
brk = 0												#
while os.path.isfile(ens1) != True:								#
	dateC = dateC - datetime.timedelta(days = 1)						#
	date2 = date2 - datetime.timedelta(days = 1)						#
	cfs_iz += 24										#
	ens1 = "/var/www/html/processamento/CFSD10001E1"+dateC.strftime('%Y%m%d')+"00.nc"	#
	ens2 = "/var/www/html/processamento/CFSD10001E2"+dateC.strftime('%Y%m%d')+"00.nc"	#
	ens3 = "/var/www/html/processamento/CFSD10001E3"+dateC.strftime('%Y%m%d')+"00.nc"	#
	ens4 = "/var/www/html/processamento/CFSD10001E4"+dateC.strftime('%Y%m%d')+"00.nc"	#
	ens5 = "/var/www/html/processamento/CFSD10001E1"+date2.strftime('%Y%m%d')+"00.nc"	#
	ens6 = "/var/www/html/processamento/CFSD10001E2"+date2.strftime('%Y%m%d')+"00.nc"	#
	ens7 = "/var/www/html/processamento/CFSD10001E3"+date2.strftime('%Y%m%d')+"00.nc"	#
	ens8 = "/var/www/html/processamento/CFSD10001E4"+date2.strftime('%Y%m%d')+"00.nc"	#
	if os.path.isfile(ens5) != True:							#
		ens1 = False									#
		break										#
	brk +=1											#
	if brk >= 3:										#	
		ens1 = False									#
		break										#	
#################################################################################################

#################################################################################################
##	Determina quais dados serão respondidos devido a existencia ou não dos arquiv		#
if id_db == 1:											#
	wrf_file = wrf_file									#
	gfs_file = gfs_file									#
	cfs_file = cfs_file									#
elif id_db == 2:										#
	wrf_file = False									#
	gfs_file = gfs_file									#
	cfs_file = cfs_file									#
elif id_db  == 3:										#
	wrf_file  = False									#
	gfs_file = gfs_file									#
	cfs_file = False									#
else:												#
	print json.dumps(""" Erro modelo indisponivel/falha de autentiucacao  """)		#	
	exit(1)											#
#################################################################################################

resposta = []

#sem wrf		
if wrf_file == False and gfs_file != False and ens1 != False:
	gfs_ix, gfs_iy = GFS1.lat_lon.GFS_grab(gfs_file, lat0, lon0)
	cfs_ix, cfs_iy = CFS.lat_lon.CFS_grab(ens1, lat0, lon0)	
	if tipo1 == 'Calendar':
		resposta1 = GFS1.opera_GFS1.calendario_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		resposta2 = CFS.opera_CFS.calendario_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, cfs_iz, cfs_ix, cfs_iy, dateC, utc0, token_novo)
		resposta.append(resposta1)
		resposta.append(resposta2)
		print json.dumps(resposta)		
		exit(0)

	elif tipo1 == 'Table':
		resposta = GFS1.opera_GFS1.tabela_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		print json.dumps(resposta)				
		exit(0)
	else:	
		resposta  = """ Erro de autenticação """
		print json.dumps(resposta)
		exit(1)

#sem GFS
elif gfs_file == False and wrf_file != False and ens1 != False:		           
	wrf_ix, wrf_iy = WRF.lat_lon.WRF_grab(wrf_file, lat0, lon0)
	cfs_ix, cfs_iy = CFS.lat_lon.CFS_grab(ens1, lat0, lon0)	
	if tipo1 == 'Calendar':
		resposta1 = WRF.opera_WRF.calendario_out(wrf_file, var1, wrf_iz, wrf_ix, wrf_iy, dateW, utc0, token_novo)
		resposta2 = CFS.opera_CFS.calendario_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, cfs_iz, cfs_ix, cfs_iy, dateC, utc0, token_novo)
		resposta.append(resposta1)
		resposta.append(resposta2)
		print json.dumps(resposta)		
		exit(0)
	elif tipo1 == 'Table':
		resposta = WRF.opera_WRF.tabela_out(wrf_file, var1, wrf_iz, wrf_ix, wrf_iy, dateW, utc0, token_novo)
		print json.dumps(resposta)				
		exit(0)
	else:	
		resposta  = """ Erro de autenticação """
		print json.dumps(resposta)
		exit(1)

#sem CFS
elif ens1 == False and gfs_file != False and wrf_file != False:
	wrf_ix, wrf_iy = WRF.lat_lon.WRF_grab(wrf_file, lat0, lon0)
	gfs_ix, gfs_iy = GFS.lat_lon.GFS_grab(gfs_file, lat0, lon0)
	if tipo1 == 'Calendar':
		resposta1 = WRF.opera_WRF.calendario_out(wrf_file, var1, wrf_iz, wrf_ix, wrf_iy, dateW, utc0, token_novo)
		resposta2 = GFS1.opera_GFS1.calendario_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		resposta.append(resposta1)
		resposta.append(resposta2)
		print json.dumps(resposta)
		exit(0)
	elif tipo1 == 'Table':
		resposta1 = WRF.opera_WRF.tabela_out(wrf_file, var1, wrf_iz, wrf_ix, wrf_iy, dateW, utc0, token_novo)
		resposta2 = GFS1.opera_GFS1.tabela_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		resposta.append(resposta1)
		resposta.append(resposta2)
		print json.dumps(resposta)
		exit(0)
	else:	
		resposta  = """ Erro de autenticação """
		print json.dumps(resposta)
		exit(1)

# completo 
elif ens1 != False and gfs_file != False and wrf_file != False:
	wrf_ix, wrf_iy = WRF.lat_lon.WRF_grab(wrf_file, lat0, lon0)
	gfs_ix, gfs_iy = GFS.lat_lon.GFS_grab(gfs_file, lat0, lon0)
	cfs_ix, cfs_iy = CFS.lat_lon.CFS_grab(ens1, lat0, lon0)	
	if tipo1 == 'Calendar':
		resposta1 = WRF.opera_WRF.calendario_out(wrf_file, var1, wrf_iz, wrf_ix, wrf_iy, dateW, utc0, token_novo)
		resposta2 = GFS1.opera_GFS1.calendario_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		resposta3 = CFS.opera_CFS.calendario_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, cfs_iz, cfs_ix, cfs_iy, dateC, utc0, token_novo)
		resposta.append(resposta1)
		resposta.append(resposta2)
		resposta.append(resposta3)
		print json.dumps(resposta)
		exit(0)
	elif tipo1 == 'Table':
		resposta1 = WRF.opera_WRF.tabela_out(wrf_file, var1, wrf_iz, wrf_ix, wrf_iy, dateW, utc0, token_novo)
		resposta2 = GFS1.opera_GFS1.tabela_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		resposta.append(resposta1)
		resposta.append(resposta2)
		print json.dumps(resposta)
		exit(0)
	else:	
		resposta  = """ Erro de autenticação """
		print json.dumps(resposta)
		exit(1)

# so GFS'
elif ens1 == False and gfs_file != False and wrf_file == False:
	gfs_ix, gfs_iy = GFS.lat_lon.GFS_grab(gfs_file, lat0, lon0)
	if tipo1 == 'Calendar':
		resposta = GFS1.opera_GFS1.calendario_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		print json.dumps(resposta)
		exit(0)
	elif tipo1 == 'Table':
		resposta = GFS1.opera_GFS1.tabela_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		print json.dumps(resposta)
		exit(0)
	else:	
		resposta  = """ Erro de autenticação """
		print json.dumps(resposta)
		exit(1)

# so WRF
elif ens1 == False and gfs_file == False and wrf_file != False:
	wrf_ix, wrf_iy = WRF.lat_lon.WRF_grab(wrf_file, lat0, lon0)
	if tipo1 == 'Calendar':
		resposta = WRF.opera_WRF.calendario_out(wrf_file, var1, wrf_iz, wrf_ix, wrf_iy, dateW, utc0, token_novo)
		print json.dumps(resposta)
		exit(0)
	elif tipo1 == 'Table':
		resposta = WRF.opera_WRF.tabela_out(wrf_file, var1, wrf_iz, wrf_ix, wrf_iy, dateW, utc0, token_novo)
		print json.dumps(resposta)
		exit(0)
	else:	
		resposta  = """ Erro de autenticação """
		print json.dumps(resposta)
		exit(1)

# so CFS
    elif ens1 != False and gfs_file == False and wrf_file == False:
	cfs_ix, cfs_iy = CFS.lat_lon.CFS_grab(ens1, lat0, lon0)	
	if tipo1 == 'Calendar':
		resposta = CFS.opera_CFS.calendario_out(ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8, var1, cfs_iz, cfs_ix, cfs_iy, dateC, utc0, token_novo)
		print json.dumps(resposta)
		exit(0)
	else:	
		resposta  = """ Erro de autenticação """
		print json.dumps(resposta)
		exit(1)

# sem nenhum		
else:	
	data_erro = datetime.datetime.now()						
	print "%s arquivo nao existe WRF=%s GFS=%s CFS=%s" % (data_erro, wrf_file, gfs_file, ens1)	
	print json.dumps(""" Erro modelo indisponivel !""")				
	exit(1)		


								
###############################################################################################################
	## Chamada de execução dos graficos apos todas as respostas do calendario	

