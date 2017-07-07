#!/usr/bin/env python
#-*- coding:utf-8 -*-


def _get_wrf(iz, ixwrf, iywrf, date0, utc0)
	var = wrf_var._get_NCVAR('nuvem')
	date1 = 
    
    ens1, ens2, ens3, ens4, ens5, ens6, ens7, ens8 = wrf_var._get_FILE()
	
	cloud1 = wrf_var._get_cloud(var, ens1)
	cloud1 = np.sum(cloud1, axis= 3)
	cloud2 = wrf_var._get_cloud(var, ens2)
	cloud2 = np.sum(cloud2, axis= 3)	

	rain1 = wrf_var._get_rain(var, ens1)
	rain2 = wrf_var._get_rain(var, ens2)	

	prob_t_g_c, prob_t_r_c, prob_t_y_c, value_t_c, max_t_c, min_t_c = prob_time._get_TIMEP(ens1, ens2, time, 12, ixWRF, iyWRF, TOP, BOT)
	prob_t_g_r, prob_t_r_r, prob_t_y_r, value_t_r, max_t_r, min_t_r = prob_time._get_TIMEP(ens1, ens2, time, 12, ixWRF, iyWRF, TOP, BOT)

	prob_a_g_c, prob_a_r_c, prob_a_y_c, value_a_c, max_a_c, min_a_c = prob_area._get_AREAP(ens1, time, ixWRF, iyWRF, TOP, BOT)
	prob_a_g_r, prob_a_r_r, prob_a_y_r, value_a_r, max_a_r, min_a_r = prob_area._get_AREAP(ens1, time, ixWRF, iyWRF, TOP, BOT)

	value_c = np.divide(np.add(np.multiply(2, value_t_c), value_a_c), 3)
	value_r = np.divide(np.add(np.multiply(2, value_t_r), value_a_r), 3)

	