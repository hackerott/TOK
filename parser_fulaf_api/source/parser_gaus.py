import numpy as np
import netCDF4
import datetime
from numpy import cos, sin, arccos, power, sqrt, exp, arctan2, argmin, argmax, arctan


def _get_gaus_wrf(nc_file, theta, sig_x, sig_y, ampl, center):
	WRFfile = netCDF4.Dataset(nc_file, 'r')
	WRF_lat		= WRFfile.variables['XLAT_M'] 
	WRF_lon		= WRFfile.variables['XLONG_M'] 
	# rain_c		= WRFfile.variables["RAINC"]
	rain_c = np.zeros((31, 511, 481))
	size		= rain_c.shape
	# print size
	a = cos(theta)**2/(2*sig_x**2) + sin(theta)**2/(2*sig_y**2)
	b = -sin(2*theta)/(4*sig_x**2) + sin(2*theta)/(4*sig_y**2)
	c = sin(theta)**2/(2*sig_x**2) + cos(theta)**2/(2*sig_y**2);
	for i in range(0, size[1]):
		for j in range(0, size[2]):
			# rain_c[24, i, j] = ampl * exp( ( (-1*(a*(i-center[0])**2)) - (2*b*(i-center[0])*(j-center[1])) + (c*(j-center[1])**2) ) )
			rain_c[23, i, j] = ampl * exp( -1*( ((a*(i-center[0])**2)) - (2*b*(i-center[0])*(j-center[1])) + (c*(j-center[1])**2) ) )
	return(rain_c, WRF_lat, WRF_lon)

def DATA_get_wrf(rain_c, ix, iy, date0, date1, WRF_lat, WRF_lon):
	date1 = datetime.datetime.strptime(str(date1), '%Y%m%d%H')	
	max_j	= (len(rain_c) // 24) + 1
	out	= []
	date_f	= []
	lat	= []
	lon	= []
	a = 24
	b = 0
	date0 = datetime.datetime.strptime(str(date0), '%Y%m%d%H') + datetime.timedelta(hours= 24)
	for j in range(0, max_j):
#		if a > max_i:
#			break
		if date0 == date1:
			out_self = sum(rain_c[b:a, ix, iy])
			if out_self < 0:
				out_self = 0
			out.append(out_self)
			date_f.append(date0)
			lat.append(WRF_lat[ix, iy])
			lon.append(WRF_lon[ix, iy])
		b = a
		a += 24
	return(out, rain_c, date_f, lat, lon)