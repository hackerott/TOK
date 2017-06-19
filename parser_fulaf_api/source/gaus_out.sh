#! /bin/bash

for i in $(seq 1 30) ; do
	echo "$i;2014;11;24;6;15"	>> 24hrprecip_gaus_15.txt
	lon=$(echo "6.270 - ($i - 1)/100" | bc -l)
	echo "SN$i, $lon, 59.02111" >> stationlist_gaus.csv
	done