import numpy as np
import netCDF4
import math
import sys
import datetime


def _get_station(lat, lon, date0):
	"""
	Create a dict with lat lon values for all station availabe 
	Search the closest pair
	Check if da date exist in the station file
	"""
	stations_d	=	{	"A540" : [-23.45, -44.62],
						"Axxx" : [-22.22, -44.44],
					}

	dif_lat_lon = []
	for key,lat_d in stations_d.items():
		dif_lat_lon.append(abs(lat_d[0] - lat) + abs(lat_d[1] - lon))
		key1.append(key)
	station = key1[np.argmin(dif_lat_lon)]
	station_file = "/path/%s.csv" %(station)	
	raw_data = np.genfromtxt(station_file, delimiter=";",skip_header=1, skip_footer=1)
	date_v = raw_data[:0] # check correct column as parsing as soon as i got the actualy data
	if date0 in date_v:
		return(station_file, True)
	else:
		return(station, False)

def _data_station(station_file, date0): 
	"""
	return all meteo vars for given station file and date
	"""
	raw_data	=	np.genfromtxt(station_file, delimiter=";",skip_header=1, skip_footer=1)

   	date_v	=	raw_data[:, 0] 
   	rain_v	=	raw_data[:, 1] 
   	temp_v	=	raw_data[:, 2] 
   	tmax_v	=	raw_data[:, 3] 
   	tmin_v	=	raw_data[:, 4] 
   	radi_v	=	raw_data[:, 5] 
   	wind_v	=	raw_data[:, 6] 
   	dire_v	=	raw_data[:, 7] 
   	
   	for i in range(0, len(date_v)):
   		if date_v[i] == date0:
   			a = i
   			break

	out = [date_v[a], rain_v[a], temp_v[a], tmax_v[a], tmin_v[a], radi_v[a], wind_v[a], dire_v[a]]
	return(out)







