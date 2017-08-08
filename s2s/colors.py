#!/usr/bin/env python
#-*- coding:utf-8 -*-

# import numpy as np
# import datetime

def _get_color(val):
	return {1	:	"red",
			2	:	"yellow",
			3	:	"green"
			}.get(val, "yellow")

def _get_WRF(value):
	color = []
	for val, i in value:
		if val  >= 0.75:
			color.append(_get_color(3))
		elif val >= 0.5:
			color.append(_get_color(2))
		elif val < 0.5:
			color.append(_get_color(1))
	return(color)

def _get_GFS(value):
	color = []
	for val, i in value:
		if val  >= 0.7:
			color.append(_get_color(3))
		elif val >= 0.45:
			color.append(_get_color(2))
		elif val < 0.45:
			color.append(_get_color(1))
	return(color)

def _get_CFS(value):
	color = []
	for val, i in value:
		if val  >= 0.7:
			color.append(_get_color(3))
		elif val >= 0.45:
			color.append(_get_color(2))
		elif val < 0.45:
			color.append(_get_color(1))
	return(color)

def _get_alert(value)
	for val, i in value:
		value[i] = _get_color(val)
	return(value)