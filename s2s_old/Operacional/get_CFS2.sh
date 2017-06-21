#!/bin/bash
export NCARG_ROOT=/usr/local/ncl-6.3.0
export PATH=$PATH:$NCARG_ROOT/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/ncl_6.3.0/lib
export NETCDF=/usr/bin
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:/usr/local/opengrads/Contents

model_name=CFS
DIR=/p1-zar/gustavo/tempook_proc/${model_name}
modelo=${model_name}D10001
hh=00
aa=`date +%Y`
mm=`date +%m`
dd=`date +%d`
aa4=`date +%Y`
CTL=/p1-zar/gustavo/tempook_proc/CFS/CFS.ctl

ensa(){
	ens=$1	
	if test ! -s ${DIR}/${aa}${mm}${dd}${hh}/$ens; then
		echo "CRIANDO DIRETORIO  ${DIR}/${aa}${mm}${dd}${hh}"
		mkdir -p ${DIR}/${aa}${mm}${dd}${hh}/$ens
	
	else
		  echo "DIRETORIO ${DIR}/${aa}${mm}${dd}${hh}/$ens CRIADO"
	fi

	cd ${DIR}/${aa}${mm}${dd}${hh}/$ens
	cp $CTL  . 
	for vez in `seq 32 136` ; do
		down(){
   
			horas=$(expr $vez \* 6)
			dataf=$(date -u +%Y%m%d%H -d "12am + $horas hours")
			caminho=ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/cfs/prod/cfs/cfs.${aa}${mm}${dd}/${hh}/6hrly_grib_0$ens
			arq=flxf${dataf}.0$ens.${aa}${mm}${dd}${hh}.grb2
			arq2=${dataf}.grb2

			if test ! -s ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} ; then
				/usr/bin/wget ${caminho}${i}/${arq}
#				/usr/bin/axel -a ${caminho}${i}/${arq}
				sleep 0.05
				mv ${arq} ${arq2}	
			fi

			if test  -s ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} ; then
			  vartest=`echo $(ls -l ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} | awk '{ print $5 }')`
			  tamanho=`curl -sI ${caminho}/${arq} | grep Content- | cut -d " " -f2 |tr -d '\r\n'`

			  if [ ${vartest} != $tamanho ]  ; then
				echo "arquivo existe mas eh pequeno"
				rm ${arq}
				/usr/bin/wget ${caminho}/${arq}
#				/usr/bin/axel -a ${caminho}${i}/${arq}
				sleep 0.05
				mv ${arq} ${arq2}
				vartest=$(ls -l ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} | awk '{ print $5 }')

				if [ ${vartest} != $tamanho ]  ; then
				       echo "tentei abaixar o arquivo pela 2 vez e continua pequeno"
				       echo "deu merda no download do arquivo ${arq}"  > ${DIR}/${aa}${mm}${dd}${hh}/$en/log_error1_simul.txt
     				fi

  			  fi
		  	   
			fi
			}
		sleep 0.1
		down
		sleep 0.1
		down

		/opt/opengrads/gribmap -i  ${model_name}.ctl  > /dev/null 2>${DIR}/${aa}${mm}${dd}${hh}/$ens/erro_gribmap.log

		/opt/opengrads/lats4d.sh -q -format netcdf -vars pressfc dswrfsfc pratesfc ugrd10m vgrd10m tmp2m spfh2m -i ${model_name}.ctl -o ../${modelo}E${ens}${aa}${mm}${dd}${hh} >/dev/null 2>${DIR}/${aa}${mm}${dd}${hh}/$ens/serro_nc.log

	done

	}

ensa 1 & ensa 2 & ensa 3 & ensa 4 && echo "Terminou os Download do CFS!!!!"


