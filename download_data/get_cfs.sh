#!/bin/bash
export NCARG_ROOT=/usr/local/ncl-6.3.0
export PATH=$PATH:$NCARG_ROOT/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/ncl_6.3.0/lib
export NETCDF=/usr/bin
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:/usr/local/opengrads/Contents

model_name=CFS
DIR=/var/www/html/processamento/${model_name}
modelo=${model_name}D10001
hh=00
aa=`date +%Y`
mm=`date +%m`
dd=`date +%d`
aa4=`date +%Y`
CTL=/var/www/html/processamento/CFS.ctl

_get_ens(){
	ens=$1
	if test ! -s ${DIR}/${aa}${mm}${dd}${hh}/$ens; then
		echo "Making dir   ${DIR}/${aa}${mm}${dd}${hh}"
		mkdir -p ${DIR}/${aa}${mm}${dd}${hh}/$ens

	else
		  echo "DIR ${DIR}/${aa}${mm}${dd}${hh}/$ens exist"
	fi

	cd ${DIR}/${aa}${mm}${dd}${hh}/$ens
#	cp $CTL  .
	for vez in `seq 32 136` ; do
		_get_down(){

			horas=$(expr $vez \* 6)
			dataf=$(date -u +%Y%m%d%H -d "12am + $horas hours")
			caminho=ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/cfs/prod/cfs/cfs.${aa}${mm}${dd}/${hh}/6hrly_grib_0$ens
			arq=flxf${dataf}.0$ens.${aa}${mm}${dd}${hh}.grb2
			arq2=${dataf}.grb2

			if test ! -s ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} ; then
#				/usr/bin/wget ${caminho}${i}/${arq}
				/usr/bin/axel -a ${caminho}${i}/${arq}
				sleep 0.075
				mv ${arq} ${arq2}
			fi

			if test  -s ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} ; then
			  vartest=`echo $(ls -l ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} | awk '{ print $5 }')`
			  size=`curl -sI ${caminho}/${arq} | grep Content- | cut -d " " -f2 |tr -d '\r\n'`

			  if [ ${vartest} != $size ]  ; then
				echo "file too small"
				rm ${arq}
				/usr/bin/wget ${caminho}/${arq}
#				/usr/bin/axel -a ${caminho}${i}/${arq}
				sleep 0.075
				mv ${arq} ${arq2}
				vartest=$(ls -l ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} | awk '{ print $5 }')

				if [ ${vartest} != $size ]  ; then
				       echo "try 2 times, file still too small"
				       echo "some thing wrong with the file ${arq}"  > ${DIR}/${aa}${mm}${dd}${hh}/$en/log_error1_simul.txt
     				fi

  			  fi
			fi
			}
		echo "1 ## $ens"
		sleep 0.075 && _get_down &&  echo "2 ## $ens"
		sleep 0.15  && _get_down && 	echo "3 ## $ens"
		done
# in the next lines we convert all grib files to single netcdf file only with the needed variables
	cat ${DIR}/${aa}${mm}${dd}${hh}/$ens/*grb2 >> ${aa}${mm}${dd}${hh}.grb2_
	rm *.ctl
	/usr/bin/g2ctl.pl ${aa}${mm}${dd}${hh}.grb2_ >> ${model_name}_.ctl
	rm *.idx
	/usr/local/opengrads/Contents/gribmap -i  ${model_name}_.ctl  > /dev/null 2>${DIR}/${aa}${mm}${dd}${hh}/$ens/erro_gribmap.log
	sleep 0.005
	/usr/local/opengrads/Contents/lats4d.sh -q -format netcdf -vars pressfc dswrfsfc pratesfc ugrd10m vgrd10m tmp2m spfh2m -i ${model_name}_.ctl -o ../../../${modelo}E${ens}${aa}${mm}${dd}${hh} >/dev/null 2>${DIR}/${aa}${mm}${dd}${hh}/$ens/serro_nc.log
	}

#_get_ens 1
_get_ens 1 & _get_ens 2
echo "Ensamble 1 e 2 done"
sleep 10
rm ${DIR}/${aa}${mm}${dd}${hh}/*/*grb2

_get_ens 3 & _get_ens 4
echo "Ensamble 3 e 4 done"
sleep 10
rm ${DIR}/${aa}${mm}${dd}${hh}/*/*grb2

echo "CFS Downloads ended!!!!"
echo "CFS Downloads ended!!!!" >> ${DIR}/${aa}${mm}${dd}${hh}/download_ok.txt

# this scrip depends on wget and axel
# the conversion to netcdf depends on OpenGrads gribmap, lats4d an g2ctl (I think they are all pearl scripts)
