#!/usr/bin/env python
#-*- coding:utf-8 -*-

#import numpy as np
import timezonefinder as tz
import datetime
import pytz
import ephem

def _get_timezone(lat, lon):
	
	tf = tz.TimezoneFinder()
	loc = tf.timezone_at(lng=lat, lat=lon)
	local = pytz.timezone(loc)
	off_set = datetime.datetime.now(local)
	utc = off_set.utcoffset().total_seconds()//3600

	return(int(utc))

def _get_sun(lat, lon, utc):

	observer = ephem.Observer()
	observer.lat 	= str(lat)
	observer.long 	= str(lon)
	observer.date	= datetime.datetime.now().strftime('%Y/%m/%d')

	sun = ephem.Sun(observer)
	sun_rise	= observer.next_rising(sun)
	sun_set		= observer.next_setting(sun)
	sun_rise	= ephem.Date(sun_rise + utc*ephem.hour).datetime().strftime('%H:%M')
	sun_set		= ephem.Date( sun_set + utc*ephem.hour).datetime().strftime('%H:%M')

	return(sun_rise, sun_set)

