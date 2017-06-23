#Structure:

	It's madded of 3 independent API, each one responsible for a model (main_wrf.py, main_gfs.py, main_cfs.py), which are related to it's own variable description and selection file (wrf_var.py, cfs_var.py, gfs_var.py). 
	All the calculation and assignments will be done by integrated scripts.

		- prob_area.ý: ensemble using the area near selected point
		- prob_time.py: ensemble using previous forecasts
		- figure.py: assign condition figure
		- calendar.py: create data for s2s calendar view
		- table.py: create data for hourly tables
		- card.py: generate daily card, with figures and max/min values
		- lat_lon.py: locate the closest grid point, to be used in further calculations
		- json_output.py: single script to generate json objects to be printed/saved as final output   
		- XXX_var.py: all the variables names/keys, as also limits for alert levels.
		
#TOK

### Gustavo Beneduzi
