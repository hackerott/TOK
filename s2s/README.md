#Structure:

	It's maded of 3 independent API, each one responsible for a model (main_wrf.py, main_gfs.py, main_cfs.py), which are related to it's own variable discription and selection file (wrf_var.py, cfs_var.py, gfs_var.py). 
	All the calculation and asignments will be done by integraded scripts.

		- prob_area.ý: ensamble using the area near selected point
		- prob_time.py: ensamble using previus forecasts
		- figure.py: asign condition figure
		- calendar.py: create data for s2s calendar view
		- table.py: create data for hourly tables
		- card.py: generate daily card, with figures and max/min values
		- lat_lon.py: locate the closest grid point, to be used in further calculations
		- json_output.py: single script to genarate json objects to be printed/saved as final output   
		
#TOK

### Gustavo Beneduzi
