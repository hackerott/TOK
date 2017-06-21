#!/bin/bash
#-*- coding:utf-8 -*-

lat=-17.2580
lon=-44.8356
utc=0
ano=2016
mes=09
dia=15

url=ftp://ftp.betravedur.is/pub/wrf/brazil/cfs.
prefix=ENS0
sufix=dailyVarzeaPalma_d02
data=${ano}${mes}${dia}

for numero in `seq -w 1 4` ; do
	arquivo=$prefix$numero-$sufix
	axel -a ${url}${data}00/${arquivo}
	ncks -d south_north,100,150 -d west_east,100,150 ${arquivo} -O ${arquivo}_crop 	
	python WRF_CSV.py ${arquivo}_crop ${lat} ${lon} ${utc} ${data} > ${arquivo}_${data}.csv
	rm  ${arquivo}*
done

mkdir ${data}
mv ${arquivo}_${data}.csv ${data}/. 



cdo -f nc -sellonlatbox,longi,longf,lati,latf entrada saida
