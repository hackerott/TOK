#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sci
from mpl_toolkits.basemap import Basemap

#######################################
import parser_station
import parser_wrf
import calc_stat

################################################################################
## create the necessary variables for ploting
def DATA_get(rain_station, rain_wrf, lat, lon):
#	lat_max = max(lat) + 1 # for dinamic setting cornners
#	lat_min = min(lat) - 1
#	lon_max = max(lon) + 1
#	lon_min = min(lon) - 1
#	lc = [lat_min, lon_min] # lower left cornner
#	rc = [lat_max, lon_max] # upper right cornner
	lc = [56, 4]	
	rc = [65, 15]
	
	return(rain_wrf, rain_station, lat, lon, lc, rc )	

################################################################################
## create RMSE scatter size and color scheme
def get_RMSE_plot(rain_wrf, rain_station):
#	size_r	= []
#	size_b	= []
	color_r	= []
	color_b	= []
	mrs = max(rain_station)
	for i in range(len(rain_wrf)):
		rmse = np.sqrt((rain_wrf[i] - rain_station[i])**2)
 		bias = (rain_wrf[i]- rain_station[i])/mrs 
		color_r.append(rmse)
		color_b.append(bias)
	
	return(color_b, color_r)

#		size_r.append(10 + np.absolute(rmse/mrs)*10)
#		size_b.append(10 + np.absolute(bias/mrs)*10)
#	return(size_r, size_b, color_b, color_r)

################################################################################
## create and plot RMSE scatter  
def DATA_plot_scatter(rain_wrf, rain_station, lat, lon, lc, rc, path4):
	print "Setting RMSE and BIAS scale..."
#	size_r, size_b, color_b, color_r  = get_RMSE_plot(rain_wrf, rain_station)
	color_b, color_r  = get_RMSE_plot(rain_wrf, rain_station)
	rmse = np.mean(color_r)
	bias = np.mena(color_b)
	print "Setting basemaps..."
	file_name_map = '%s/map_rmse_bias.png' % (path4)
	file_name_scatter = '%s/scatter_obs_sim.png' % (path4)
	file_name = '%s/model_simulation.png' % (path4)

##SCATTER
	print "Drawing Obs X Sim..."
	index = np.arange(len(rain_station))
	diference = np.subtract(rain_station, rain_wrf)
	fig3 = plt.figure("SCATTER",figsize=(16, 9))
	plt.ylabel('Observation [mm]')
	plt.xlabel('Simulation [mm]')
#	plt.title('Obs X Sim')
	plt.xlim(0, max(max(rain_wrf), max(rain_station)))
	plt.ylim(0, max(max(rain_wrf), max(rain_station)))
	plt.scatter(rain_wrf, rain_station, c='black', marker='o', linewidth=0)
	plt.plot(index, index, c='grey')
	x_box = (len(index)/16) * 14
	y_box = (len(index)/8) * 6
	plt.figtext(x_box, y_box, "\bStatistical indicators:\n\n Relative error: %s \n Absolute error: %s \n  " % (rmse, bias) ,bbox={'facecolor':'lightgray', 'alpha':0.5, 'pad':10}, multialignment = 'left')
	plt.savefig(file_name_scatter, dpi=300, pad_inches=0)

##RMSE
	fig = plt.figure("RMSE/BIAS SCATTER",figsize=(16, 9))
	ax = fig.add_subplot(121)
	ax.set_title("Absolute error (|sim - obs|) [mm]")
	map1 = Basemap(projection='merc',llcrnrlat=lc[0], urcrnrlat=rc[0], llcrnrlon=lc[1], urcrnrlon=rc[1],resolution='h')
	map1.drawcoastlines()
	map1.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
#	map1.drawstates(color='k')
	map1.fillcontinents(color='lightgray', zorder=0)
	print "Drawing RMSE..."	
	map1.scatter(lon, lat, c=color_r, s=30, marker='o', latlon=True, linewidth=0, )
	map1.colorbar(location='right', size='5%', pad='2%')
	map1.drawmapscale(lc[1]+1.3, lc[0]+0.6, lc[1]+10, lc[0]+8, 250, barstyle='fancy', fontsize = 11) 
	map1.drawparallels(np.arange(lc[0],rc[0]+2.5,2.5), labels=[1,0,0,1])
	map1.drawmeridians(np.arange(lc[1],rc[1]+5,5.), labels=[1,0,0,1])

##BIAS
	color_b.append(1.0)
	color_b.append(-1.0)
	lat.append(0) 
	lon.append(0)
	lat.append(0)
	lon.append(0)
	ax = fig.add_subplot(122)
	ax.set_title("Relative error (sim-obs)/max(obs)")
	map2 = Basemap(projection='merc',llcrnrlat=lc[0], urcrnrlat=rc[0], llcrnrlon=lc[1], urcrnrlon=rc[1],resolution='h')
	map2.drawcoastlines()
	map2.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
#	map2.drawstates(color='k')
	map2.fillcontinents(color='lightgray', zorder=0)
	print "Drawing BIAS..."
	map2.scatter(lon, lat, c=color_b, s=30, marker='o', latlon=True, linewidth=0, )
	map2.colorbar(location='right', size='5%', pad='2%')
	map2.drawmapscale(lc[1]+1.3, lc[0]+0.6, lc[1]+10, lc[0]+8, 250, barstyle='fancy', fontsize = 11) 
	map2.drawparallels(np.arange(lc[0],rc[0]+2.5,2.5), labels=[1,0,0,1])
	map2.drawmeridians(np.arange(lc[1],rc[1]+5,5.), labels=[1,0,0,1])
	plt.savefig(file_name_map, dpi=300, pad_inches=0)

	a =  max(max(rain_wrf), max(rain_station)) # max lim of scale
	b =  min(min(rain_wrf), min(rain_station)) # min lim of scale
	rain_wrf.append(a) 
	rain_station.append(a)
	rain_wrf.append(b)
	rain_station.append(b)

##Model
	fig2 = plt.figure("MODEL SIMULATION SCATTER",figsize=(16, 9))
	ax = fig2.add_subplot(121)
	ax.set_title("Model [mm]")
	map3 = Basemap(projection='merc',llcrnrlat=lc[0], urcrnrlat=rc[0], llcrnrlon=lc[1], urcrnrlon=rc[1],resolution='h')
	map3.drawcoastlines()
	map3.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
#	map3.drawstates(color='k')
	map3.fillcontinents(color='lightgray', zorder=0)
	print "Drawing Model..."
	map3.scatter(lon, lat, c=rain_wrf, s=30, marker='o', latlon=True, linewidth=0, )
	map3.colorbar(location='right', size='5%', pad='2%')
	map3.drawmapscale(lc[1]+1.3, lc[0]+0.6, lc[1]+10, lc[0]+8, 250, barstyle='fancy', fontsize = 11) 
	map3.drawparallels(np.arange(lc[0],rc[0]+2.5,2.5), labels=[1,0,0,1])
	map3.drawmeridians(np.arange(lc[1],rc[1]+5,5.), labels=[1,0,0,1])

##Station
	ax = fig2.add_subplot(122)
	ax.set_title("Station [mm]")
	map4 = Basemap(projection='merc',llcrnrlat=lc[0], urcrnrlat=rc[0], llcrnrlon=lc[1], urcrnrlon=rc[1],resolution='h')
	map4.drawcoastlines()
	map4.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
#	map4.drawstates(color='k')
	map4.fillcontinents(color='lightgray', zorder=0)
	print "Drawing Observations..."
	map4.scatter(lon, lat, c=rain_station, s=30, marker='o', latlon=True, linewidth=0, )
	map4.colorbar(location='right', size='5%', pad='2%')
	map4.drawmapscale(lc[1]+1.3, lc[0]+0.6, lc[1]+10, lc[0]+8, 250, barstyle='fancy', fontsize = 11) 
	map4.drawparallels(np.arange(lc[0],rc[0]+2.5,2.5), labels=[1,0,0,1])
	map4.drawmeridians(np.arange(lc[1],rc[1]+5,5.), labels=[1,0,0,1])
	plt.savefig(file_name, dpi=300, pad_inches=0)

	return()

