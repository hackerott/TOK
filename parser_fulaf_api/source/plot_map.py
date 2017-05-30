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
def DATA_get(rain_station, rain_wrf, lat, lon, area_error):
#	lat_max = max(lat) + 1 # for dinamic setting cornners
#	lat_min = min(lat) - 1
#	lon_max = max(lon) + 1
#	lon_min = min(lon) - 1
#	lc = [lat_min, lon_min] # lower left cornner
#	rc = [lat_max, lon_max] # upper right cornner
	lc = [56, 4]	
	rc = [65, 15]
	
	return(rain_wrf, rain_station, lat, lon, lc, rc, area_error)	
################################################################################
## calculate the RMSE
def _get_rmse(rain_station, rain_wrf):
	r =  []
	for i in range(0, len(rain_station)):
		r.append((rain_station[i] - rain_wrf[i])**2)
	return np.sqrt(np.mean(r))

################################################################################
## calculate the BIAS
def _get_bias(rain_station, rain_wrf):
	b = []
	n = 0
	for i in range(0, len(rain_station)):
		b.append(rain_station[i] - rain_wrf[i])
		n += 1
	return sum(b)/n
################################################################################
## create scatter size and color scheme
def get_SCATTER_plot(rain_wrf, rain_station):
#	size_r	= []
#	size_b	= []
	color_a	= []
	color_r	= []
	mrs = max(rain_station)
	n = len(rain_station)
	for i in range(len(rain_wrf)):
		absolute_e = np.absolute((rain_wrf[i] - rain_station[i]))
 		relative_e = (rain_wrf[i]- rain_station[i])/mrs 
		color_a.append(absolute_e)
		color_r.append(relative_e)

	return(color_r, color_a)

#		size_r.append(10 + np.absolute(rmse/mrs)*10)
#		size_b.append(10 + np.absolute(bias/mrs)*10)
#	return(size_r, size_b, color_b, color_r)

################################################################################
## create and plot RMSE scatter  
def DATA_plot_scatter(rain_wrf, rain_station, lat, lon, lc, rc, path4):
	print "Setting RMSE and BIAS scale..."
#	size_r, size_b, color_b, color_r  = get_RMSE_plot(rain_wrf, rain_station)
	color_r, color_a  = get_SCATTER_plot(rain_wrf, rain_station)

	mae = np.mean(color_a)
	mre = np.mean(color_r)
	rmse = _get_rmse(rain_station, rain_wrf)
	bias = _get_bias(rain_station, rain_wrf)

	print "Setting basemaps..."
	file_name_map = '%s/map_mae_mre.png' % (path4)
	file_name_scatter = '%s/scatter_obs_sim.png' % (path4)
	file_name = '%s/model_simulation.png' % (path4)

##SCATTER plot
	print "Drawing Obs X Sim..."
	diference = np.subtract(rain_station, rain_wrf)
	fig3 = plt.figure("SCATTER",figsize=(16, 9))
	plt.ylabel('Observation [mm]')
	plt.xlabel('Simulation [mm]')
#	plt.title('Obs X Sim')
	plt.xlim(0, max(max(rain_wrf), max(rain_station)))
	plt.ylim(0, max(max(rain_wrf), max(rain_station)))
	plt.scatter(rain_wrf, rain_station, c='black', marker='o', linewidth=0)
	plt.plot(rain_station, rain_station, c='gray')
	plt.figtext(0.73, 0.70, "Statistical indicators:\n\n MRE: %.3f\n MAE: %.3f\n Bias: %.3f\n RMSE: %.3f" % (mre, mae, bias, rmse) ,bbox={'facecolor':'lightgray', 'alpha':0.5, 'pad':10}, fontsize=15, multialignment = 'left')
	plt.savefig(file_name_scatter, dpi=300, pad_inches=0)

##Absolute Error Map
	fig = plt.figure("RMSE/BIAS SCATTER",figsize=(16, 9))
	ax = fig.add_subplot(121)
	ax.set_title("Absolute error (|sim - obs|) [mm]")
	map1 = Basemap(projection='merc',llcrnrlat=lc[0], urcrnrlat=rc[0], llcrnrlon=lc[1], urcrnrlon=rc[1],resolution='h')
	map1.drawcoastlines()
	map1.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
	map1.fillcontinents(color='lightgray', zorder=0)
	print "Drawing Absolute error..."	
	map1.scatter(lon, lat, c=color_a, s=30, marker='o', latlon=True, linewidth=0, )
	map1.colorbar(location='right', size='5%', pad='2%')
	map1.drawmapscale(lc[1]+1.3, lc[0]+0.6, lc[1]+10, lc[0]+8, 250, barstyle='fancy', fontsize = 11) 
	map1.drawparallels(np.arange(lc[0],rc[0]+2.5,2.5), labels=[1,0,0,1])
	map1.drawmeridians(np.arange(lc[1],rc[1]+5,5.), labels=[1,0,0,1])

##Realtive Error Map
	color_r.append(1.0)
	color_r.append(-1.0)
	lat.append(0) 
	lon.append(0)
	lat.append(0)
	lon.append(0)
	ax = fig.add_subplot(122)
	ax.set_title("Relative error (sim-obs)/max(obs)")
	map2 = Basemap(projection='merc',llcrnrlat=lc[0], urcrnrlat=rc[0], llcrnrlon=lc[1], urcrnrlon=rc[1],resolution='h')
	map2.drawcoastlines()
	map2.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
	map2.fillcontinents(color='lightgray', zorder=0)
	print "Drawing Relative error..."
	map2.scatter(lon, lat, c=color_r, s=30, marker='o', latlon=True, linewidth=0, )
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

##Model Map
	fig2 = plt.figure("MODEL SIMULATION SCATTER",figsize=(16, 9))
	ax = fig2.add_subplot(121)
	ax.set_title("Model [mm]")
	map3 = Basemap(projection='merc',llcrnrlat=lc[0], urcrnrlat=rc[0], llcrnrlon=lc[1], urcrnrlon=rc[1],resolution='h')
	map3.drawcoastlines()
	map3.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
	map3.fillcontinents(color='lightgray', zorder=0)
	print "Drawing Model..."
	map3.scatter(lon, lat, c=rain_wrf, s=30, marker='o', latlon=True, linewidth=0, )
	map3.colorbar(location='right', size='5%', pad='2%')
	map3.drawmapscale(lc[1]+1.3, lc[0]+0.6, lc[1]+10, lc[0]+8, 250, barstyle='fancy', fontsize = 11) 
	map3.drawparallels(np.arange(lc[0],rc[0]+2.5,2.5), labels=[1,0,0,1])
	map3.drawmeridians(np.arange(lc[1],rc[1]+5,5.), labels=[1,0,0,1])

##Station Map
	ax = fig2.add_subplot(122)
	ax.set_title("Station [mm]")
	map4 = Basemap(projection='merc',llcrnrlat=lc[0], urcrnrlat=rc[0], llcrnrlon=lc[1], urcrnrlon=rc[1],resolution='h')
	map4.drawcoastlines()
	map4.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
	map4.fillcontinents(color='lightgray', zorder=0)
	print "Drawing Observations..."
	map4.scatter(lon, lat, c=rain_station, s=30, marker='o', latlon=True, linewidth=0, )
	map4.colorbar(location='right', size='5%', pad='2%')
	map4.drawmapscale(lc[1]+1.3, lc[0]+0.6, lc[1]+10, lc[0]+8, 250, barstyle='fancy', fontsize = 11) 
	map4.drawparallels(np.arange(lc[0],rc[0]+2.5,2.5), labels=[1,0,0,1])
	map4.drawmeridians(np.arange(lc[1],rc[1]+5,5.), labels=[1,0,0,1])
	plt.savefig(file_name, dpi=300, pad_inches=0)

	return()

