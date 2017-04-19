#!/usr/bin/python
# coding: utf-8

import numpy as np
import netCDF4
import math
import sys
import time
import calendar
import datetime
from math import pi
from numpy import cos, sin, arccos, power, sqrt, exp,arctan2

## Entrada
filename = (sys.argv[1])
lat1 =  (sys.argv[2])
lon1 =  (sys.argv[3])
utc1 = (sys.argv[4])
date1 = (sys.argv[5])

lat0 = float(lat1)
lon0 = float(lon1)
utc0 = float(utc1)

ncfile = netCDF4.Dataset(filename, 'r')

def tunnel_fast(latvar,lonvar,lat0,lon0):

    rad_factor = pi/180.0 # radianos

    latvals = latvar[::] * rad_factor # latitude longitude ==> numpy arrays
    lonvals = lonvar[::] * rad_factor
    ny,nx,nz = latvals.shape
    lat0_rad = lat0 * rad_factor
    lon0_rad = lon0 * rad_factor
    clat,clon = cos(latvals),cos(lonvals)
    slat,slon = sin(latvals),sin(lonvals)
    delX = cos(lat0_rad)*cos(lon0_rad) - clat*clon
    delY = cos(lat0_rad)*sin(lon0_rad) - clat*slon
    delZ = sin(lat0_rad) - slat;
    dist_sq = delX**2 + delY**2 + delZ**2
    minindex_1d = dist_sq.argmin()  # 1D index do elemento minimo
    iz_min,ix_min,iy_min = np.unravel_index( minindex_1d, latvals.shape)
    return iz_min,ix_min,iy_min

# variaveis do netcdf
latvar = ncfile.variables['XLAT'] #latitude e longitude
lonvar = ncfile.variables['XLONG']
tempk = ncfile.variables['T2']
umidade = ncfile.variables['Q2']
radiacao = ncfile.variables['SWDOWN']
u_vento = ncfile.variables['U10'] #coordenadas do vetor vento
v_vento = ncfile.variables['V10']
pressao = ncfile.variables['PSFC']
cu_chuva = ncfile.variables['RAINC']
scu_chuva = ncfile.variables['RAINNC']
time = ncfile.variables['Times']
date0 = datetime.datetime.strptime(date1, '%Y%m%d')

#indices das coordenandas
iz,ix,iy = tunnel_fast(latvar, lonvar, lat0, lon0)
max_i = len(time) 

# calcula os resultados das variaveis e imprimi a tabela
print "data, temperatura, umidade, chuva, vento, direcao, radiacao"

r2d = 45.0/np.arctan(1.0)

for i in range(0, max_i):

    d1 = date0 + datetime.timedelta(hours = i + utc0)
    hora = d1.strftime('%d/%m/%Y %H:%M')
    chuva = cu_chuva[i,ix,iy] + scu_chuva[i,ix,iy]- cu_chuva[i-1,ix,iy] - scu_chuva[i-1,ix,iy]
    vento = sqrt(power(u_vento[i,ix,iy],2) + power(v_vento[i,ix,iy],2))
    up =u_vento[i,ix,iy]
    vp =v_vento[i,ix,iy]
    dir = np.arctan2(up, vp) * r2d + 180
#    if dir < 0:
#        dir = dir + 360
    tempc = tempk[i,ix,iy] - 273.15
    rad = radiacao[i,ix,iy]
    urp=umidade[i,ix,iy]
    pressp=379.90516/pressao[i,ix,iy]
    a5=17.2693882 * (tempc) / (tempk[i,ix,iy] - 35.86)
    rh2 = 100*(urp / ( (pressp) * exp(a5) ))
### Saida
    print ''' %s,  %.1f, %.1f, %.1f, %.1f, %.1f, %.1f ''' % (hora, tempc, rh2, chuva, vento, dir, rad)

ncfile.close()
