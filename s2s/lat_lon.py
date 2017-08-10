import netCDF4
import math
import sys
import numpy as np

from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan

###############################################################################
#Functions to locate lat lon from a np.array
## CFS and GFS are exactly the same, keeping separated just for esthetics  
def _get_CFS(latCFS,lonCFS,lat0,lon0):
	rad_factor =  pi/180.0
	latvals = latCFS[:] * rad_factor
	lonvals = lonCFS[:] * rad_factor
	lat0_rad = lat0 * rad_factor
	lon0_rad = lon0 * rad_factor
	delX = (latvals[:]-lat0_rad)**2
	delY = (lonvals[:]-lon0_rad)**2
	minindexX = delX.argmin()  # 1D index of minimum element
	minindexY = delY.argmin()
	return(minindexX, minindexY)

def _get_GFS(latGFS,lonGFS,lat0,lon0):
	rad_factor =  pi/180.0
	latvals = latGFS[:] * rad_factor
	lonvals = lonGFS[:] * rad_factor
	lat0_rad = lat0 * rad_factor
	lon0_rad = lon0 * rad_factor
	delX = (latvals[:]-lat0_rad)**2
	delY = (lonvals[:]-lon0_rad)**2
	minindexX = delX.argmin()  # 1D index of minimum element
	minindexY = delY.argmin()
	return(minindexX, minindexY)

def _get_WRF(latWRF, lonWRF, lat0, lon0):
	rad_factor = pi/180.0
	latvals = latWRF[::] * rad_factor
	lonvals = lonWRF[::] * rad_factor
	ny ,nx, nz = latvals.shape
	lat0_rad = lat0 * rad_factor
	lon0_rad = lon0 * rad_factor
	clat, clon = cos(latvals), cos(lonvals)
	slat, slon = sin(latvals), sin(lonvals)
	delX = cos(lat0_rad) * cos(lon0_rad) - clat * clon
	delY = cos(lat0_rad) * sin(lon0_rad) - clat * slon
	delZ = sin(lat0_rad) - slat;
	dist_sq = delX**2 + delY**2 + delZ**2
	minindex_1d = dist_sq.argmin()
	iz_min, ix_min, iy_min = np.unravel_index( minindex_1d, latvals.shape)
	return(iz_min, ix_min, iy_min)

###############################################################################
#Functions to locate lat lon from a nc file

def GFS_grab(GFSfile,lat0,lon0):
	latGFS	= GFSfile.variables['latitude']
	lonGFS	= GFSfile.variables['longitude']		
	minindexX, minindexY = _get_GFS(latGFS,lonGFS,lat0,lon0)
	return(minindexX, minindexY)


def CFS_grab(CFSfile,lat0,lon0):
	latCFS = CFSfile.variables['latitude']
	lonCFS = CFSfile.variables['longitude']		
	minindexX, minindexY = _get_CFS(latCFS,lonCFS,lat0,lon0)
	return(minindexX, minindexY)


def WRF_grab(WRFfile, lat0, lon0):
	latWRF = WRFfile.variables['XLAT']
	lonWRF = WRFfile.variables['XLONG']	
	minindexZ, minindexX, minindexY = _get_WRF(latWRF,lonWRF,lat0,lon0)
	return(minindexX, minindexY)
