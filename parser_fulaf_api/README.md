# Operation:
	To run the API, execute on terminal the main.pyc file contained inside run folder, with WRFout, 
	list of stations(control file), stations data, output path, forecast start date and analises date as arguments.
	There is no need to create the output folder, but is necessary that the user whom's folder belongs run the code.

```bash
$: python main.pyc /path/to/24hrprecip-201411.txt /path/to/WRFout.nc4 /path/to/stationlist.csv /path/to/output/folder YYYYMMDDHH YYYYMMDDHH

python source/main.py data/station/24hrprecip-201411.txt data/nc/rav2-12km-wrfout_d01_2014-11-22_00_surface_reduced.nc4 data/station/stationlist.csv out/12km 2014112206 2014112306
```

# Dependencies:
	-python 2.7
		-NumPy
		-OS
		-Sys
		-netCDF4
		-Datetime
		-Math
		-Timeit
		-Multiprocessing
		-Joblib
		-Mpl_toolkits
		-Scipy
# Details:
 
	- main.py:
>	Receive the terminal inputs, reads a control file containing a list with all stations and locations, execute all other services 
	
	- output.py:
>	Create and control the output files and output messages to terminal

	- lat_lon.py:
>	Calculates the closest point in the forecast from station lat lon tuple

	- parser_station.py:
>	Parses the station data file, returns 2 arrays containing dates and data

	- parser_wrf.py:
>	Parses the WRF out file, returns 2 arrays with same data format as parser_satation does

	- calc_stat.py:
>	Calculate all the statistics, sync all dates and locations
	
	-plot_map.py:
>	Generates all plots, maps and scatters

	- calc_area_error.py:
>	Calculate error considering a range around the station

	
## TOK
### TEMPOOK repository


###### Gustavo Beneduzi
