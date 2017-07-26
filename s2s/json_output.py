#!/usr/bin/env python
#-*- coding:utf-8 -*-

#import json

#######################################
'''
This module receives the resulting arrays and format then in to
json, any other type of output cold be created, just adding new 
output scripts
'''
#######################################
def _get_OUT(date, prob, color, value, maxi, mini, fig, model, var_id):

	if model == 'card':
		success, dic = _get_card(date, prob, color, value, maxi, mini, fig, var_id, model)

	elif model == 'table':
		success, dic = _get_table(date, prob, color, value, maxi, mini, fig, var_id, model)

	elif model == 'calendar':
		success, dic = _get_calendar(date, prob, color, value, maxi, mini, fig, var_id, model)

	return(success, dic)

def _get_table(date, prob, color, value, maxi, mini, fig, var_id, model):

	if var_id == 1 :
		# for i in range(0, len(value)):
		values = {"rain"	:	[value]}
		units = {"rain" : {                "current" : "mm",
                "label" : "rain",
                "options" : [
                    {
                        "id" : "mm",
                        "label" : "mm"
                    }
                ]}}
		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 2:
                self_value = []
                for i in range(0, len(value)):
                        d = {
                                "speed" : "%.2f" %value[i,0],
                                "direction" : "%.2f" %value[i,1]
                        }
                        self_value.append(d)
                values = {"wind"        :       [self_value]}
 		units = {"wind" : {
                "current" : "ms",
                "label" : "wind",
                "options" : [
                    {
                        "id" : "ms",
                        "label" : "m/s"
                    },
                    {
                        "id" : "kmh",
                        "label" : "km/h"
                    }
                ]
                }}
		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 3:
		# for i in range(0, len(value)):
		values = {"temperature"	:	[value]}
		units = {
			"temperature" : {
                "current" : "c",
                "label" : "Temperature",
                "options" : [ 
                    {
                        "id" : "c",
                        "label" : "˚C"
                    },
                    {
                        "id" : "f",
                        "label" : "˚F"
                    }
                ]
					            },}
       		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True
	elif var_id == 4:
		# for i in range(0, len(value)):
		values = {"radiation"	:	[value]	}
		units = {"radiation" : {
                "current" : "wm2",
                "label" : "radiation",
                "options" : [
                    {
                        "id" : "wm2",
                        "label" : "W/m²"
                    }
                ]},}
       		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 5:
		# for i in range(0, len(value)):
		values = {"humidity"	:	[value]}
		units = {"humidity" : {
                "current" : "per",
                "label" : "humidity",
                "options" : [
                    {
                        "id" : "per",
                        "label" : "%"
                    }
                ]
	  		       },}
       		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 6:	
		# for i in range(0, len(value)):
		values = {
			{"rain"			:	[value[:0]]
				},
			{"wind"			:	[value[:1]]
				},
			{"temperature"	:	[value[:2]]
				},
			{"radiation"	:	[value[:3]]
				},
			{"humidity"		:	[value[:4]]
				}
				}
		units = {
			"temperature" : {
                "current" : "c",
                "label" : "Temperature",
                "options" : [ 
                    {
                        "id" : "c",
                        "label" : "˚C"
                    },
                    {
                        "id" : "f",
                        "label" : "˚F"
                    }
                ]
					            },
	        "rain" : {
                "current" : "mm",
                "label" : "rain",
                "options" : [
                    {
                        "id" : "mm",
                        "label" : "mm"
                    }
                ]
     				       },
	        "radiation" : {
                "current" : "wm2",
                "label" : "radiation",
                "options" : [
                    {
                        "id" : "wm2",
                        "label" : "W/m²"
                    }
                ]},
	        "humidity" : {
                "current" : "per",
                "label" : "humidity",
                "options" : [
                    {
                        "id" : "per",
                        "label" : "%"
                    }
                ]
	  		       },
            "wind" : {
                "current" : "ms",
                "label" : "wind",
                "options" : [
                    {
                        "id" : "ms",
                        "label" : "m/s"
                    },
                    {
                        "id" : "kmh",
                        "label" : "km/h"
                    }
                ]
                }
             }
		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	else:
		success, dic = _get_ERROR(var_id, model)

	return(success, dic)

def _get_card(date, prob, color, value, maxi, mini, fig, var_id, model):

	if var_id == 1 :
		# for i in range(0, len(value)):
		values = {"rain"	:	[value], 
			  "max"		:	[maxi],
			  "min"		:	[mini],}

		units = {"rain" : {                "current" : "mm",
                "label" : "rain",
                "options" : [
                    {
                        "id" : "mm",
                        "label" : "mm"
                    }
                ]}}
       		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Card OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 2:
		self_value = []
		a = 0
		b = 1
		for i in range(0, len(value)+1):
			if b >= len(value):
				break
			d = {
				"speed" : "%.2f" %value[a], 
				"direction" : "%.2f" %value[b]
			}
			self_value.append(d)
			a = b + 1
			b = b + 2
		values = {"wind"	:	[self_value], 
			  "max"		:	"%.2f" %maxi,
			  "min"		:	"%.2f"%mini,}

 		units = {"wind" : {
			                "current" : "ms",
			                "label" : "wind",
			                "options" : [
				                    {
				                        "id" : "ms",
                        				"label" : "m/s"
                    				     },
				                    {
				                        "id" : "kmh",
				                        "label" : "km/h"
                    				}]}}
       		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 3:
		# for i in range(0, len(value)):
		values = {"temperature"	:	[value],
			  "max"		:	"%.2f" %maxi,
			  "min"		:	"%.2f"%mini,}

		units = {
			"temperature" : {
                "current" : "c",
                "label" : "Temperature",
                "options" : [ 
                    {
                        "id" : "c",
                        "label" : "˚C"
                    },
                    {
                        "id" : "f",
                        "label" : "˚F"
                    }
                ]
					            },}
       		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 4:
		# for i in range(0, len(value)):
		values = {"radiation"	:	[value],
			  "max"		:	"%.2f" %maxi,
			  "min"		:	"%.2f"%mini,}
		units = {"radiation" : {
                "current" : "wm2",
                "label" : "radiation",
                "options" : [
                    {
                        "id" : "wm2",
                        "label" : "W/m²"
                    }
                ]},}
       		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 5:
		# for i in range(0, len(value)):
		values = {"humidity"	:	[value],
			  "max"		:	"%.2f" %maxi,
			  "min"		:	"%.2f"%mini,}
		units = {"humidity" : {
                "current" : "per",
                "label" : "humidity",
                "options" : [
                    {
                        "id" : "per",
                        "label" : "%"
                    }
                ]
	  		       },}
       		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 6:	
		# for i in range(0, len(value)):
		values = {
			{"rain"			:	[value[:0]],
			  "max"		:	[maxi[:0]],
			  "min"		:	[min[:0]]
				},
			{"wind"			:	[value[:1]],
			  "max"		:	[maxi[:1]],
			  "min"		:	[min[:1]]
				},
			{"temperature"	:	[value[:2]],
			  "max"		:	[maxi[:2]],
			  "min"		:	[min[:2]]
				},
			{"radiation"	:	[value[:3]],
			  "max"		:	[maxi[:3]],
			  "min"		:	[min[:3]]
				},
			{"humidity"	:	[value[:4]],
			  "max"		:	[maxi[:0]],
			  "min"		:	[min[:0]]
				}
			}
		units = {
			"temperature" : {
                "current" : "c",
                "label" : "Temperature",
                "options" : [ 
                    {
                        "id" : "c",
                        "label" : "˚C"
                    },
                    {
                        "id" : "f",
                        "label" : "˚F"
                    }
                ]
					            },
	        "rain" : {
                "current" : "mm",
                "label" : "rain",
                "options" : [
                    {
                        "id" : "mm",
                        "label" : "mm"
                    }
                ]
     				       },
	        "radiation" : {
                "current" : "wm2",
                "label" : "radiation",
                "options" : [
                    {
                        "id" : "wm2",
                        "label" : "W/m²"
                    }
                ]},
	        "humidity" : {
                "current" : "per",
                "label" : "humidity",
                "options" : [
                    {
                        "id" : "per",
                        "label" : "%"
                    }
                ]
	  		       },
            "wind" : {
                "current" : "ms",
                "label" : "wind",
                "options" : [
                    {
                        "id" : "ms",
                        "label" : "m/s"
                    },
                    {
                        "id" : "kmh",
                        "label" : "km/h"
                    }
                ]
                }
             }
		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date.strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Table OK!",
					"status" : 0 
					}
				}
		success = True

	else:
		success, dic = _get_ERROR(var_id, model)
			
	return(success, dic)

def _get_calendar(date, prob, color, value, maxi, mini, fig, var_id, model):

	dic = {}
#	else:
#		success, dic = _get_ERROR(var_id, model)
	success, dic = _get_ERROR(var_id, model)

	return(success, dic)

def _get_ERROR(var_id, model):

	dic = {}

	return(False, dic)

def _get_aux():
	dic ={"data" : 
		{"models" : 
			{"WRF" : [	{'rain' : w_out[0]},
						{'wind' : w_out[1]},
						{'temperature' : w_out[2]},
						{'radiation' : w_out[3]},
						{'humidity' : w_out[4]}
					]
			},
			{"GFS" : [	{'rain' : g_out[0]},
						{'wind' : g_out[1]},
						{'temperature' : g_out[2]},
						{'radiation' : g_out[3]},
						{'humidity' : g_out[4]}
					]
			},
			{"CFS" : [	{'rain' : c_out[0]},
						{'wind' : c_out[1]},
						{'temperature' : c_out[2]},
						{'radiation' : c_out[3]},
						{'humidity' : c_out[4]}
					]
			}
		}, 
		"message"	: "System is UP",
		"status"	: 0,
		"sun_set"	: sun_set,
		"sun_rise"	: sun_rise,
		"timezone"	: utc,


	}
	return(success, dic)