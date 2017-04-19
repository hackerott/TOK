#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import cgi
#import os
import datetime
import io
import json
import matplotlib.pyplot as plt

import variaveis.chuva
import variaveis.temperatura
import variaveis.vento
import variaveis.radiacao
import variaveis.umidade

#################################################################################
form = cgi.FieldStorage()
#iz	= form.getvalue("iz")
ix	= form.getvalue("ix")
iy	= form.getvalue("iy")
modelo 	= form.getvalue("model")
nc_file	= form.getvalue("file")
var1	= form.getvalue("var")
#################################################################################
def titulo(var1):
	return {
		'chuva'		: 'resposta acumulada (mm)',
		'temperatura'	: 'Temperatura (C)',
		'radiacao'	: 'Radiacao  (w/m2)',
		'umidade'	: 'Umidade relativa (%)',
		'vento'		: 'Velocidade do Vento (m/s)'
		}.get(var1, 'Null')

def label_x(var1):
	return {
		'chuva'		: 'Acumulado por dia',
		'temperatura'	: 'Maxima e minima',
		'radiacao'	: 'Acumulado',
		'umidade'	: 'Maxima e minima',
		'vento'		: 'Maximo e direçao da maxima'
		}.get(var1, 'Null')

def label_y(var1):
	return {
		'chuva'		: 'mm',
		'temperatura'	: 'C',
		'radiacao'	: 'w/m2',
		'umidade'	: '%',
		'vento'		: 'm/s'
		}.get(var1, 'Null')

#################################################################################
plt.figure(var1, figsize=(9, 6))
plt.title(titulo(var1))
plt.ylabel(label_y(var1))
plt.xlabel(label_x(var1))

if modelo == 'WRF':
	wrffile = netCDF4.Dataset(nc_file, 'r')
	if var1 == 'chuva':
		resposta, index, cor, lim_y = variaveis.chuva.wrf(ix, iy, wrffile, date0)
		plt.bar(index, resposta, 0.75, bottom=0, color=cor)
		plt.plot(index, reposta[0], color='b')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	elif var1 == 'temperatura':
		resposta1, resposta2, index, cor, lim_y = variaveis.temperatura.wrf(ix, iy, wrffile, date0)
		plt.plot(index, resposta1, color='blue')
		plt.plot(index, resposta2, color='red')
		plt.plot(index, resposta1[0], color='black')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	elif var1 == 'radiacao':
		resposta, index, cor, lim_y = variaveis.radiacao.wrf(ix, iy, wrffile, date0)
		plt.bar(index, resposta, 0.75, bottom=0, color=cor)
		plt.plot(index, reposta[0], color='b')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	elif var1 == 'umidade':
		resposta1, resposta2, index, cor, lim_y = variaveis.umidade.wrf(ix, iy, wrffile, date0)
		plt.plot(index, resposta1, color='blue')
		plt.plot(index, resposta2, color='red')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	elif var1 == 'vento':
		resposta, U, V, index, cor, lim_y = variaveis.vento.wrf(ix, iy, wrffile, date0)
		plt.quiver(index, resposta, U, V, color='blue')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	else:
		resposta = { 'success'       :0,
                             'error'         :'recurso indisponivel',
                             'message'       :'GRA não possui esta função %s' %var1}		
		print  "Content-type : application/json\n\n"
		print json.dumps(resposta)
		exit()
#################################################################################
elif modelo == 'GFS': 
	gfsfile = netCDF4.Dataset(nc_file, 'r')
	if var1 == 'chuva':
		resposta, index, cor, lim_y = variaveis.chuva.gfs(ix, iy, gfsfile, date0)
		plt.bar(index, resposta, 0.75, bottom=0, color=cor)
		plt.plot(index, reposta[0], color='b')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	elif var1 == 'temperatura':
		resposta1, resposta2, index, cor, lim_y = variaveis.temperatura.gfs(ix, iy, gfsfile, date0)
		plt.plot(index, resposta1, color='b')
		plt.plot(index, resposta2, color='r')
		plt.plot(index, resposta1[0], color='black')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	elif var1 == 'radiacao':
		resposta, index, cor, lim_y = variaveis.radiacao.gfs(ix, iy, gfsfile, date0)
		plt.bar(index, resposta, 0.75, bottom=0, color=cor)
		plt.plot(index, reposta[0], color='b')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	elif var1 == 'umidade':
		resposta1, resposta2, index, cor, lim_y = variaveis.umidade.gfs(ix, iy, gfsfile, date0)
		plt.plot(index, resposta1, color='b')
		plt.plot(index, resposta2, color='r')
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	elif var1 == 'vento':
		resposta, U, V, index, cor, lim_y = variaveis.vento.gfs(ix, iy, gfsfile, date0)
		plt.quiver(index, resposta, U, V, color=cor)
		plt.xlim(0, 10.75)
		plt.ylim(0, lim_y)

	else:
		resposta = { 'success'       :0,
        	             'error'         :'recurso indisponivel',
        	             'message'       :'GRA não possui esta função %s' % var1}		
		print "Content-type : application/json\n\n"
		print json.dumps(resposta)
		exit()

buf = io.BytesIO()
plt.savefig(buf, format='png')
#################################################################################
print "Content-type: image/png\n\n"
print buf.read()
#buf.close()
exit()
