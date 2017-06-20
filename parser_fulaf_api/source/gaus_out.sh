#! /bin/bash

#for i in $(seq 1 500) ; do
#	echo "" >> stationlist_gaus.csv
#	 echo ""	>> 24hrprecip_gaus_15.txt

#	done

for i in $(seq 30 150) ; do
	echo "$i;2014;11;23;6;15"	>> 24hrprecip_gaus_15.txt
	lon=$(echo "6.270 - ($i - 1)/50" | bc -l)
	echo "SN$i, $lon, 59.02111" >> stationlist_gaus.csv
	done
