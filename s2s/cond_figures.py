#!/usr/bin/env python
#-*- coding:utf-8 -*-

def _get_figure_url(var):
	return{
			"1"	:	"http://50.112.50.113/figuras/images_sky/clo.png",
			"2"	:	"http://50.112.50.113/figuras/images_sky/clo_r.png",
			"3"	:	"http://50.112.50.113/figuras/images_sky/clo_s.png",
			"4"	:	"http://50.112.50.113/figuras/images_sky/clo_t.png",
			"5"	:	"http://50.112.50.113/figuras/images_sky/moo.png",
			"6"	:	"http://50.112.50.113/figuras/images_sky/moo_f_c.png",
			"7"	:	"http://50.112.50.113/figuras/images_sky/moo_h.png",
			"8"	:	"http://50.112.50.113/figuras/images_sky/moo_m_c.png",
			"9"	:	"http://50.112.50.113/figuras/images_sky/moo_r.png",
			"10":	"http://50.112.50.113/figuras/images_sky/moo_s.png",
			"11":	"http://50.112.50.113/figuras/images_sky/moo_t.png",
			"12":	"http://50.112.50.113/figuras/images_sky/sun.png",
			"13":	"http://50.112.50.113/figuras/images_sky/sun_f_c.png",
			"14":	"http://50.112.50.113/figuras/images_sky/sun_h_c.png",
			"15":	"http://50.112.50.113/figuras/images_sky/sun_m_c.png",
			"16":	"http://50.112.50.113/figuras/images_sky/sun_r.png",
			"17":	"http://50.112.50.113/figuras/images_sky/sun_s.png",
			"18":	"http://50.112.50.113/figuras/images_sky/sun_t.png",
			
	}.get(var, 'Null')

def DATA_cond_figure(cloud, rain, date0):
	for i, date in date0:
		if cloud[i] < 0.75:
			if date.hour < 18 and date.hour > 6:
				if rain[i] < 0.1:
					if cloud[i] < 0.25:
						value.append(_get_figure_url(13))
					elif cloud[i] < 0.5:
						value.append(_get_figure_url(14))
					else:
						value.append(_get_figure_url(15))
				elif rain[i] < 3:
					value.append(_get_figure_url(16))
				else:
					value.append(_get_figure_url(18))		
			else:	
				if rain[i] < 0.1:
					if cloud[i] < 0.25:
						value.append(_get_figure_url(6))
					elif cloud[i] < 0.5:
						value.append(_get_figure_url(7))
					else:
						value.append(_get_figure_url(8))
				elif rain[i] < 3:
					value.append(_get_figure_url(9))
				else:
					value.append(_get_figure_url(11))
		else:
			if rain[i] < 0.1:
				value.append(_get_figure_url(1))
			elif rain[i] < 3:
				value.append(_get_figure_url(2))
			else:
				value.append(_get_figure_url(4))

	return(value)
