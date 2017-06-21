#!/bin/bash

#########################################################################
#*Dependencias:								#
#	wget, axel, gribmap, grads, lats4d(opengrads), g2ctl(opengrads)	#
#									#
#*Obter dias anteriores:						#
#	alterar a variavel dd e mm para dia e mes desejado, lembrando	#
#	ques estão disponiveis até 7 dias annteriores			#
#									#
#*Mudar diretorios:							#
#	Alterar a variavel DIR, todos os outros caminhos dependem	#
#	desta variavel, sendo criados durante o script			#
#########################################################################

model_name=CFS
DIR=~/${model_name}/processamento/
modelo=${model_name}D10001
hh=00
aa=`date +%Y`
mm=`date +%m`
#mm=12
#dd=`date +%d`
dd=26
aa4=`date +%Y`

ensa(){
	ens=$1	
	if test ! -s ${DIR}/${aa}${mm}${dd}${hh}/$ens; then
		echo "CRIANDO DIRETORIO  ${DIR}/${aa}${mm}${dd}${hh}"
		mkdir -p ${DIR}/${aa}${mm}${dd}${hh}/$ens

	else
		  echo "DIRETORIO ${DIR}/${aa}${mm}${dd}${hh}/$ens CRIADO"
	fi

	cd ${DIR}/${aa}${mm}${dd}${hh}/$ens
	for vez in `seq 32 136` ; do
		down(){

			horas=$(expr $vez \* 6)
			dataf=$(date -u +%Y%m%d%H -d "12am + $horas hours")
			caminho=ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/cfs/prod/cfs/cfs.${aa}${mm}${dd}/${hh}/6hrly_grib_0$ens
			arq=flxf${dataf}.0$ens.${aa}${mm}${dd}${hh}.grb2
			arq2=${dataf}.grb2

			if test ! -s ${DIR}/${aa}${mm}${dd}${hh}/$ens/${arq2} ; then
#				/usr/bin/wget ${caminho}${i}/${arq}
				/usr/bin/axel -a ${caminho}${i}/${arq} > /dev/null 2>${DIR}/${aa}${mm}${dd}${hh}/$en/erro_download.log
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
					hora=$(date)
				       echo "$hora deu merda no download do arquivo ${arq}"  > ${DIR}/${aa}${mm}${dd}${hh}/$en/log_error1_simul.txt
     				fi

  			  fi
			fi
			}
		sleep 0.05 && down
		sleep 0.05 && down
		done
	cat ${DIR}/${aa}${mm}${dd}${hh}/$ens/*grb2 > ${aa}${mm}${dd}${hh}.grb2_$ens
	/opt/opengrads/g2ctl.pl ${DIR}/${aa}${mm}${dd}${hh}/$ens/${aa}${mm}${dd}${hh}.grb2_$ens > ${DIR}/${aa}${mm}${dd}${hh}/$ens/${model_name}_$ens.ctl
	/opt/opengrads/gribmap -i  ${DIR}/${aa}${mm}${dd}${hh}/$ens/${model_name}_$ens.ctl  > /dev/null 2>${DIR}/${aa}${mm}${dd}${hh}/$ens/erro_gribmap.log
	sleep 0.005
	/opt/opengrads/lats4d.sh -q -format netcdf -vars pressfc dswrfsfc pratesfc ugrd10m vgrd10m tmp2m spfh2m -i ${DIR}/${aa}${mm}${dd}${hh}/$ens/${model_name}_$ens.ctl -o $DIR/${modelo}E${ens}${aa}${mm}${dd}${hh} >/dev/null 2>${DIR}/${aa}${mm}${dd}${hh}/$ens/serro_nc.log
	}

#ensa 1
ensa 1 & ensa 2
echo "Terminou 1 e 2"
sleep 1
rm ${DIR}/${aa}${mm}${dd}${hh}/*/*grb2

ensa 3 & ensa 4
echo "Terminou 3 e 4"
sleep 1
rm ${DIR}/${aa}${mm}${dd}${hh}/*/*grb2

echo "Terminou os Download do CFS!!!!"
hora=$(date)


#echo "$hora Terminou os Download do CFS!!!!" >> ${DIR}/${aa}${mm}${dd}${hh}/download_ok.txt

if test -s ${DIR}/${modelo}E1${aa}${mm}${dd}${hh}.nc && ${DIR}/${modelo}E2${aa}${mm}${dd}${hh}.nc && ${DIR}/${modelo}E3${aa}${mm}${dd}${hh}.nc && ${DIR}/${modelo}E4${aa}${mm}${dd}${hh}.nc ; then
	echo "$hora Terminou os Download do CFS!!!!" >> ${DIR}/download_ok.txt
	rm -r ${DIR}/${aa}${mm}${dd}${hh}
else;
	echo "Falha no download do CFS !!!" | mail -s "CFS Download" gasbeneduzi@gmail.com; joao.hackerott@gmail.com
	echo "$hora falharam os Download do CFS!!!!" >> ${DIR}/download_falha.txt
