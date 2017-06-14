#!/bin/bash
export NCARG_ROOT=/usr/local/ncl-6.3.0
export PATH=$PATH:$NCARG_ROOT/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/ncl_6.3.0/lib
export NETCDF=/usr/bin
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:/usr/local/opengrads/Contents

model_name=GFS
DIR=/home/ubuntu/${model_name}
modelo=${model_name}D10001
hh=00
aa=`date +%Y`
mm=`date +%m`
dd=`date +%d`
aa4=`date +%Y`

aaant=`date -d "-1day" "+%Y"`
mmant=`date -d "-1day" "+%m"`
ddant=`date -d "-1day" "+%d"`
rm -rf  ${DIR}/${aaant}${mmant}${ddant}${hh}



if test ! -s ${DIR}/${aa}${mm}${dd}${hh}; then
  echo "CRIANDO DIRETORIO  ${DIR}/${aa}${mm}${dd}${hh}"
  mkdir ${DIR}/${aa}${mm}${dd}${hh}
else
  echo "DIRETORIO ${DIR}/${aa}${mm}${dd}${hh} CRIADO"
fi

down(){
cd ${DIR}/${aa}${mm}${dd}${hh}

for horas in `seq -f %03g 6 1 240` ; do
   dataf=`date "+%Y%m%d%H" --date="${aa}-${mm}-${dd} ${hh}"+${horas}hour`
   caminho=ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.${aa}${mm}${dd}${hh}
   arq=gfs.t${hh}z.pgrb2.0p25.f$horas
   arq2=${dataf}.grb2
   arqf=${modelo}${dataf}.nc
if test  -s ${DIR}/${aa}${mm}${dd}${hh}/${arqf} ; then
  vartest=$(ls -l ${DIR}/${aa}${mm}${dd}${hh}/${arqf} | awk '{ print $5 }')
  if [ ${vartest} -lt 500 ]  ; then
     echo "arquivo existe mas eh pequeno"
     /usr/bin/wget ${caminho}/${arq}
     mv ${arq} ${arq2}
     /usr/bin/g2ctl.pl ${arq2}  > ${model_name}.ctl
     sleep 1
     /usr/local/opengrads/Contents/gribmap -i  ${model_name}.ctl
     /usr/local/opengrads/Contents/lats4d.sh -q -format netcdf -lat -56 7 -lon 279 330 -vars pressfc dswrfsfc acpcpsfc ugrd10m vgrd10m tmp2m spfh2m  -i ${model_name}.ctl -o ${modelo}${dataf}
     sleep 1
     rm -f ${arq2}

     vartest=$(ls -l ${DIR}/${aa}${mm}${dd}${hh}/${arqf} | awk '{ print $5 }')
     if [ ${vartest} -lt 500 ]  ; then
       echo "tentei abaixar o arquivo pela 2 vez e continua pequeno"
       echo "deu merda no download do arquivo ${arq2}"  > ${DIR}/log_error1_simul.txt
     fi
  fi
  echo "ARQUIVO ja existe, nada a fazer. "
elif test -s ${arq2} ; then
  echo "Arquivo ${arq2} existe. Nada a fazer"
else
  echo "Arquivos nao existem, baixando $arq ..."
  /usr/bin/wget ${caminho}/${arq}
  mv ${arq} ${arq2}
  /usr/bin/g2ctl.pl ${arq2}  > ${model_name}.ctl
  sleep 1
  /usr/local/opengrads/Contents/gribmap -i  ${model_name}.ctl
  /usr/local/opengrads/Contents/lats4d.sh -q -format netcdf -lat -56 7 -lon 279 330 -vars pressfc dswrfsfc acpcpsfc ugrd10m vgrd10m tmp2m spfh2m  -i ${model_name}.ctl -o ${modelo}${dataf}
  sleep 1
  rm -f ${arq2}

fi
done
}
down
down

rm -f *.idx
if test  -s ${DIR}/${aa}${mm}${dd}${hh}/${modelo}${dataf}.nc ; then
   echo "fazendo figuras"
   cd /home/ubuntu/faz_figs
   ./figuras_${model_name}.sh > log_figuras${model_name}
   sleep 1
   sudo rm -fv /var/www/html/figuras/01${modelo}${aaant}${mmant}${ddant}*
   sudo rm -fv /var/www/html/figuras/02${modelo}${aaant}${mmant}${ddant}*
   sudo rm -fv /var/www/html/figuras/03${modelo}${aaant}${mmant}${ddant}*
   sudo rm -fv /var/www/html/figuras/04${modelo}${aaant}${mmant}${ddant}*
   sleep 1

   cd ${DIR}/${aa}${mm}${dd}${hh}
   files=`ls ${modelo}*`
   sudo ncrcat -O ${files} /var/www/html/processamento/${modelo}${aa}${mm}${dd}${hh}.nc
   sleep 1
   sudo rm -fv /var/www/html/processamento/${modelo}${aaant}${mmant}${ddant}${hh}.nc
   rm -fv ${files}
fi
