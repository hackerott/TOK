#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import datetime
import os

startdate = datetime.datetime.now() - datetime.timedelta(days=1)
filename = "/var/www/html/figuras/02WRFD20101"+startdate.strftime('%Y%m%d%H')+".jpg"
while os.path.isfile(filename) != True:
	startdate = startdate + datetime.timedelta(hours=1)
        filename = "/var/www/html/figuras/02WRFD20101"+startdate.strftime('%Y%m%d%H')+".jpg"
enddate = datetime.datetime.now() + datetime.timedelta(days=5)
filename = "/var/www/html/figuras/02WRFD20101"+enddate.strftime('%Y%m%d%H')+".jpg"
while os.path.isfile(filename) != True:
        enddate = enddate - datetime.timedelta(hours=1)
        filename = "/var/www/html/figuras/02WRFD20101"+enddate.strftime('%Y%m%d%H')+".jpg"
        
datetest = startdate
temppath=[]
rainpath=[]
windpath=[]
humiditypath=[]
radiationpath=[] 
limit = enddate - startdate
for i in range(0, (limit.days*24)):
#while datetest <= enddate:
	filename = "/var/www/html/figuras/01WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg"
	if os.path.isfile(filename) == True:
                windpath.append("http://50.112.50.113/figuras/01WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg")

        filename = "/var/www/html/figuras/02WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg"
        if os.path.isfile(filename) == True:
                temppath.append("http://50.112.50.113/figuras/02WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg")

        filename = "/var/www/html/figuras/03WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg"
        if os.path.isfile(filename) == True:
                rainpath.append("http://50.112.50.113/figuras/03WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg")

        filename = "/var/www/html/figuras/04WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg"
        if os.path.isfile(filename) == True:
                radiationpath.append("http://50.112.50.113/figuras/04WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg")

        filename = "/var/www/html/figuras/05WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg"
        if os.path.isfile(filename) == True:
                humiditypath.append("http://50.112.50.113/figuras/05WRFD20101"+datetest.strftime('%Y%m%d%H')+".jpg")

	datestet = datetest + datetime.timedelta(hours=1)

if not windpath:
	windpath = "undef"
if not temppath:
        temppath = "undef"
if not rainpath:
        rainpath = "undef"
if not radiationpath:
        radiationpath = "undef"
if not humiditypath:
        humiditypath = "undef"

		

units = {
	"temperature" : {
		"current" : "c",
		"label" : "Temperature",
		"options" : [
		{
			"id" : "c",
			"label" : "~ZC"
		},
		{
			"id" : "f",
			"label" : "~ZF"
		}
		]
	},
	"rain": {
       		"current": "mm",
	        "label": "Rain",
       		"options": {
			"id": "mm",
		        "label": "mm"
	        }
        },
        "radiation": {
        	"current": "wm2",
	        "label": "Radiation",
	        "options": {
		        "id": "wm2",
		        "label": "W/m2"
	        }
	},
        "humidity": {
        	"current": "per",
	        "label": "Humidity",
	        "options": {
		        "id": "per",
		        "label": "%"
	        }
	},
        "wind": {
        	"current": "ms",
	        "label": "Wind",
	        "options": [{
		        "id": "ms",
		        "label": "m/s"
	        },
        	{
        		"id": "kmh",
        		"label": "km/h"
        	}]
        }
}

values = { 
	"temperature": [
		temppath
	],
	"rain": [
		rainpath
	],
	"radiation": [
		radiationpath
	],
	"humidity": [
		humiditypath
	],
	"wind": [
		windpath
	],
}

dic = {"data" :{
	"type"  : "vertical",
	"stepLength" : "1",
	"startDate" : startdate.strftime('%Y%m%d'),
	"endDate" : enddate.strftime('%Y%m%d'),
	"units" : units,
	"values" : values,
	"message" : "Mapa carregado com sucesso",
	"status" : 1
	}}

print "Content-type: application/json\n\n"
#print "\n\n"
#print "{teste: teste}"
print json.dumps(dic)
exit(0)
