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

#################################################################################
##	leitura do form								#
										#
form = cgi.FieldStorage()							#
										#
lat1 = form.getvalue("lat")							#
lon1 = form.getvalue("lon")							#
utc1 = form.getvalue("utc")							#
var1 = form.getvalue("var")							#
date1 = form.getvalue("data")							#
token1 = form.getvalue("token")							#
id1 = form.getvalue("id")							#
iz1 = form.getvalue("iz")							#
ip1  = os.environ["REMOTE_ADDR"]						#
#################################################################################
#################################################################################
##	variaveis iniciais							#
date0	= datetime.datetime.strptime(date1, '%Y%m%d')				#
lat0	= float(lat1)								#
lon0	= float(lon1)								#
utc0	= int(utc1)								#
if iz1 == None:									#
	iz0 = 0									#
else:										#
	iz0 = int(iz1)								#
gfs_iz	= iz0									#
#################################################################################
#################################################################################
##	Header 									#
print "Content-type: application/json\n\n"					#	
#################################################################################
#################################################################################
##	verifica o token e o id da requisição					#
token_db = mysql_access.token_get(id1)						#
if token1 != token_db:								#
	tipo1 = 'error'								#	
	data_erro = datetime.datetime.now()					#
	status = "%s tentou acessar a api WRF, %s" % (ip1, data_erro)		#
	resposta = { 'success'        : 2,					#
                      'error'         : 'problema de autenticação',		#
                      'message'       : status }				#
        print json.dumps(resposta)						#
	exit()									#
else: 										#
	tipo1 = 'sucesso'
#################################################################################
#################################################################################################
##	Checa a existencia do arquivo .nc de todos os modelos					#
date0 = datetime.datetime.strptime(date1, '%Y%m%d')						#
date2 = date0 + datetime.timedelta(days = -1)							#	
resposta = []											#
gfs_file = "/var/www/html/processamento/GFSD10001"+date0.strftime('%Y%m%d')+"00.nc"		#
brk   = 0											#
dateG = date0											#
while os.path.isfile(gfs_file) != True:								#
	dateG = dateG - datetime.timedelta(days = 1)						#
	gfs_file = "/var/www/html/processamento/GFSD10001"+dateG.strftime('%Y%m%d')+"00.nc"	#	
	brk +=1											#
	gfs_iz += 24										#
	if brk >= 3:										#
		gfs_file = False								#
		break										#
#################################################################################################
#################################################################################
# so GFS'
if gfs_file != False:
	gfs_ix, gfs_iy = GFS.lat_lon.GFS_grab(gfs_file, lat0, lon0)
	if tipo1 == 'sucesso':
		resposta = GFS.opera_GFS1.calendario_out(gfs_file, var1, gfs_iz, gfs_ix, gfs_iy, dateG, utc0, token_novo)
		print json.dumps(resposta)
		exit()
	elif tipo1 == 'error':	
		resposta1 = { 'success'        :2,
                              'error'         :'problema de autenticação',
			      'message'	      :'token ou usuario incorreto'}	
		resposta.append(resposta1)
		print json.dumps(resposta)
		exit()
	else:	
		resposta1 = { 'success'        :0,
                              'error'         :'recurso indisponivel',
                              'message'       :'GFS não possui esse recurso%s' % (tipo1)}
		resposta.append(resposta1)
		print json.dumps(resposta)
		exit()
else:	
	data_erro = datetime.datetime.now()						
	status = "%s arquivo nao existe WRF=%s GFS=%s CFS=%s" % (data_erro, wrf_file, gfs_file, ens1)	
	resposta1  = { 'success'        :0,
               	      'error'         :'recurso indisponivel',
		      'message'       : status} 	
	resposta.append(resposta1)
	print json.dumps(resposta)				
	exit()		
#################################################################################
#################################################################################
# API desenvolvida por Gustavo Beneduzi para TempoOK! 2016-2017			#
#	- Token de segurança							#
#	- Localização de LAT e LON						#
#	- Calculo de variaveis meteorologicas					#
#	- JSON de respostas							#
#################################################################################

