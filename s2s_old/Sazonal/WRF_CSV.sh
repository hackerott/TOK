#!/bin/bash

export NCARG_ROOT=/usr/local/ncl-6.3.0
export PATH=$PATH:$NCARG_ROOT/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/ncl_6.3.0/lib
export NETCDF=/usr/bin
export PATH=$PATH:/usr/local/bin


FILE=/home/${ens_name}
data_inic=

if test ! -s $FILE; then
	mkdir $FILE

cd $FILE

axel  http:// ftp.bel /$data_inic

a= $(ls $FILE | wc -l)

for 
ncks 

python  WRF_CSV.py > .csv 

mv *.csv  /destino do processamento
rm -r $FILE/ENS?_ 

#compacta os arquivos cortados para armazenamento
tar -cfz $FILE.tar.gz $FILE

rm -r $FILE

