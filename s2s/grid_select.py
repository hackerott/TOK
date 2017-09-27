#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Simple arrays to save the corner of forecasts grids.
Every new grid should added here. 
lc = left corner
rc = rigth corner
'''
#######################################
def _get_WRF_corners():
	rc_lat = [-22] 
	rc_lon = [330]
	lc_lat = [-27]
	lc_lon = [320]
	return(rc_lat, rc_lon, lc_lat, lc_lon)
#######################################
def _get_GFS_corners():
	rc_lat = [7] 
	rc_lon = [330]
	lc_lat = [-56]
	lc_lon = [279]
	return(rc_lat, rc_lon, lc_lat, lc_lon)
#######################################
def _get_CFS_corners():
	rc_lat = [90] 
	rc_lon = [360]
	lc_lat = [-90]
	lc_lon = [0]
	return(rc_lat, rc_lon, lc_lat, lc_lon)
#######################################
def _get_GRID(lat, lon, model):
	if model == 'WRF': 					# lon = -180 to 180
		rc_lat, rc_lon, lc_lat, lc_lon = _get_WRF_corners()
	elif model == 'GFS':				# lon = 0 to 360
		if lon < 0:
			lon = (360+lon)
		rc_lat, rc_lon, lc_lat, lc_lon = _get_GFS_corners()
	elif model == 'CFS':				# lon = 0 to 360
		if lon < 0:
			lon = (360+lon)
		rc_lat, rc_lon, lc_lat, lc_lon = _get_CFS_corners()
	
	for i in range(0, len(rc_lat)):
		if lat >= rc_lat[i] and lat <= lc_lat[i]:
			if  lon >= rc_lon[i] and lon <= lc_lon[i]:	
				grid = i
				break
		else:
			grid = 0		
	return(grid+1)
#######################################

