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
	for i in range(0, len(value)):
		if value[i]  >= 0.75:
			color.append(_get_color(3))
		elif value[i] >= 0.5:
			color.append(_get_color(2))
		elif value[i] < 0.5:
			color.append(_get_color(1))
	return(color)

def _get_GFS(value):
	color = []
	for i in range(0, len(value)):
		if value[i]  >= 0.7:
			color.append(_get_color(3))
		elif value[i] >= 0.45:
			color.append(_get_color(2))
		elif value[i] < 0.45:
			color.append(_get_color(1))
	return(color)

def _get_CFS(value):
	color = []
	for i in range(0, len(value)):
		if value[i]  >= 0.7:
			color.append(_get_color(3))
		elif value[i] >= 0.45:
			color.append(_get_color(2))
		elif value[i] < 0.45:
			color.append(_get_color(1))
	return(color)

def _get_ALERT(value):
	for i in range(0, len(value)):
		value[i] = _get_color(value[i])
	return(value)
