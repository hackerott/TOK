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
		'chuva'		: '03',
		'temperatura'	: '02',
		'radiacao'	: '04',
		'umidade'	: '02',
		'vento'		: '01'
		}.get(var1, '02')	

#################################################################################
##		Determina as imagens_variaveis						#
def imagen(var1):
	return {
		'chuva'		: 'chuva.png',
		'temperatura'	: 'temperatura.png',
		'radiacao'	: 'radiacao.png',
		'umidade'	: 'umidade.png',
		'vento'		: 'vento.png'
		}.get(var1, 'temperatura.png')	

#################################################################################
##              json de resposta						#
def json_out (cor, v_max, v_min, valor, url_map, url_img):
	dic =   { 'Min'   :float(v_min),
		  'Max'   :float(v_max),
		  'Cor'   :float(cor),
		  'Valor' :float(valor), 
		  'img'	  :str(url_map),
		  'img_1' :str(url_img),
		 }
        resposta = dic
        return(resposta)
#################################################################################
#		apk
def apk_out (GFS_nc, var1, iz, ixGFS, iyGFS, date0, utc0, token_novo):
	GFSfile = netCDF4.Dataset(GFS_nc, 'r')				
	unit = unidade(var1)
	img = imagen(var1)
	url_img = 'http://50.112.50.113/figuras/imagens_variaveis/%s' % (img) 
	url_map = 'http://50.112.50.113/figuras/%s' + 'GFSD10001' + '%s%i' % (unit, date0, iz0)

	if var1 == 'vento':								
		valor, valor_max, valor_min, cor = variaveis.vento.apk(GFSfile, iz, ixGFS, iyGFS)
		resposta = json_out(cor, valor_max, valor_min, valor, url_map, url_img)
	elif var1 == 'temperatura' :							
		valor, valor_max, valor_min, cor = variaveis.temperatura.apk(GFSfile, iz, ixGFS, iyGFS)
		resposta = json_out(cor, valor_max, valor_min, valor, url_map, url_img)
	elif var1 == 'umidade' :								
		valor, valor_max, valor_min, cor = variaveis.umidade.apk(GFSfile, iz, ixGFS, iyGFS)
		resposta = json_out(cor, valor_max, valor_min, valor, url_map, url_img)
	elif var1 == 'chuva' :									
		valor, valor_max, valor_min, cor = variaveis.chuva.apk(GFSfile, iz, ixGFS, iyGFS)
		resposta = json_out(cor, valor_max, valor_min, valor, url_map, url_img)
	elif var1 == 'radiacao' :								
		valor, valor_max, valor_min, cor = variaveis.radicao.apk(GFSfile, iz, ixGFS, iyGFS)
		resposta = json_out(cor, valor_max, valor_min, valor, url_map, url_img)
	return(resposta)								

