import numpy as np
import netCDF4



#######################################
## return the nc var_names for each variable
def _get_NCVAR(var):
	return {
		'chuva'		: 'pratesfc',
		'temperatura'	: 'tmp2m',
		'radiacao'	: 'dswrfsfc',
		'umidade'	: ['spfh2m', 'tmp2m', 'pressfc'], 
		'vento'		: ['ugrd10m', 'vgrd10m']
		}.get(var, 'Null')

def _get_rain(var, ncfile):
	var_nc = _get_NCVAR(var)
	var_raw1 = ncfile.variables[var_nc]

	return(var_raw1)

def _get_wind(var, ncfile):
	var_nc = _get_NCVAR(var)

	var_rawu = ncfile1.variables[var_nc[0]] 		
	var_rawv = ncfile1.variables[var_nc[1]] 
	var_raw1 = np.sqrt(np.add(np.power(var_rawu, 2), np.power(var_rawv, 2))) # wind intensity
	var_raw2 = np.arctan2(var_rawu, var_rawv) + np.power(var_rawv, 2)

	return(var_raw1, var_raw2)
def _get_radiation(var, ncfile):
	var_nc = _get_NCVAR(var)
	var_raw1 = ncfile.variables[var_nc]

def _get_temperature(var,  ncfile):
	var_nc = _get_NCVAR(var)
	var_raw1 = ncfile.variables[var_nc]
	var_raw1  =np.subtract(var_raw1, 273.15)

	return(var_raw1)

def _get_humidity(var, ncfile):
	var_nc = _get_NCVAR(var)
	var_rawa = ncfile1.variables[var_nc[0]] 		
	var_rawb = ncfile1.variables[var_nc[1]] 		
	var_rawc = ncfile1.variables[var_nc[2]]
	
	var_raw1 = np.multiply(np.multiply(100, np.divide(var_rawa, np.divide(379.90516, var_rawc))), np.exp(np.multiply(17.29, np.divide(np.add(var_rawb, -273.15), np.add(var_rawb, -35.86))))) 
	return (var_raw1)

def _get_all(var, ncfile):
	rain				= _get_rain('chuva', ncfile)
	speed, direction	= _get_wind('vento', ncfile)			
	radiation			= _get_radiation('radiacao', ncfile)
	temperature			= _get_temperature('temperatura', ncfile)
	humidity			= _get_humidity('umidade', ncfile)

	return(rain, speed, direction, radiation, temperature, humidity)