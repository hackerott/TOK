#!/usr/bin/env python
#-*- coding:utf-8 -*-
#import datetime
import astro_tz

def _get_figure_url(var):
	return{
			"1"	:	"http://breki.belgingur.is/figuras/images_sky/clo.png",
			"2"	:	"http://breki.belgingur.is/figuras/images_sky/clo_r.png",
			"3"	:	"http://breki.belgingur.is/figuras/images_sky/clo_s.png",
			"4"	:	"http://breki.belgingur.is/figuras/images_sky/clo_t.png",
			"5"	:	"http://breki.belgingur.is/figuras/images_sky/moo.png",
			"6"	:	"http://breki.belgingur.is/figuras/images_sky/moo_f_c.png",
			"7"	:	"http://breki.belgingur.is/figuras/images_sky/moo_h.png",
			"8"	:	"http://breki.belgingur.is/figuras/images_sky/moo_m_c.png",
			"9"	:	"http://breki.belgingur.is/figuras/images_sky/moo_r.png",
			"10":	"http://breki.belgingur.is/figuras/images_sky/moo_s.png",
			"11":	"http://breki.belgingur.is/figuras/images_sky/moo_t.png",
			"12":	"http://breki.belgingur.is/figuras/images_sky/sun.png",
			"13":	"http://breki.belgingur.is/figuras/images_sky/sun_f_c.png",
			"14":	"http://breki.belgingur.is/figuras/images_sky/sun_h_c.png",
			"15":	"http://breki.belgingur.is/figuras/images_sky/sun_m_c.png",
			"16":	"http://breki.belgingur.is/figuras/images_sky/sun_r.png",
			"17":	"http://breki.belgingur.is/figuras/images_sky/sun_s.png",
			"18":	"http://breki.belgingur.is/figuras/images_sky/sun_t.png",
			
	}.get(str(var), 'Null')

def _get_figure_value(cloud, rain, date, sunrise, sunset):
	if cloud < 0.75:
		if date.hour > sunrise and date.hour < sunset:
			if rain < 0.1:
				if cloud < 0.10:
					value = (_get_figure_url(12))
				elif cloud < 0.4:
					value = (_get_figure_url(13))
				else:
					value = (_get_figure_url(15))
			elif rain < 3:
				value = (_get_figure_url(16))
			else:
				value = (_get_figure_url(18))		
		else:	
			if rain < 0.1:
				if cloud < 0.1:
					value = (_get_figure_url(5))
				elif cloud < 0.4:
					value = (_get_figure_url(6))
				else:
					value = (_get_figure_url(8))
			elif rain < 3:
				value = (_get_figure_url(9))
			else:
				value = (_get_figure_url(11))
	else:
		if rain < 0.1:
			value = (_get_figure_url(1))
		elif rain < 3:
			value = (_get_figure_url(2))
		else:
			value = (_get_figure_url(4))
	return(value)

def DATA_cond_figure(cloud, rain, date, sunrise, sunset):
	value = []
	sunset = int(sunset[:2])
	sunrise = int(sunrise[:2])
	try:
		for i in range(0, len(date)):
			v = _get_figure_value(cloud[i], rain[i], date[i], sunrise, sunset)
			value.append(v)
	except:
		value = _get_figure_value(cloud, rain, date, sunrise, sunset)
		
	return(value)

