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
def _get_Name(var):
	return {
	1	:	'RAIN',
	2	:	'WIND',
	3	:	'TEMP',
	4	:	'RADIATION',
	5	:	'HUMIDITY',
	6	:	'FIGURES',  
	7	:	'all'
		}.get(var, 'Null')
#######################################
def _get_OUT(date, prob, alert, color, value, maxi, mini,  model, var_id, cur):

	if model == 'card':
		success, dic = _get_card(date, prob, color, value, maxi, mini,  var_id, model, cur)

	elif model == 'table':
		success, dic = _get_table(date, prob, color, value, maxi, mini,  var_id, model, cur)

	elif model == 'calendar':
		success, dic = _get_calendar(date, prob, alert, color, value, maxi, mini, var_id, model, cur)

	elif model == 'gcard':
		success, dic = _get_gcard(date, value, var_id, model, cur)

	elif model == 'meteo':
		success, dic = _get_meteogram(date, value)

	return(success, dic)


def _get_table(date, prob, color, value, maxi, mini, var_id, model, cur):

	if var_id == 1 :
		# for i in range(0, len(value)):
		values = {"rain"	:	[value]}
		units = {"rain" : {                "current" : cur,
                "label" : "rain",
                "options" : [
                    {
                        "id" : "metric",
                        "label" : "mm"
                    },
                    {
                        "id" : "imperial",
                        "label" : "inch"
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
                                "speed" : "%.0f" %value[i,0],
                                "direction" : "%.0f" %value[i,1]
                        }
                        self_value.append(d)
                values = {"wind"        :       [self_value]}
 		units = {"wind" : {
                "current" : cur,
                "label" : "wind",
                "options" : [
                    {
                        "id" : "metric",
                        "label" : "m/s"
                    },
                    {
                        "id" : "imperial",
                        "label" : "mph"
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
                "current" : cur,
                "label" : "Temperature",
                "options" : [ 
                    {
                        "id" : "metric",
                        "label" : "˚C"
                    },
                    {
                        "id" : "imperial",
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
                "current" : cur,
                "label" : "radiation",
                "options" : [
                    {
                        "id" : "metric",
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
                "current" : cur,
                "label" : "humidity",
                "options" : [
                    {
                        "id" : "metric",
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
		values = {"figures"	:	[value]}
		units = {"figures" : {
                "current" : "metric",
                "label" : "cond_figures",
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


	elif var_id == 7:	
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

def _get_card(date, prob, color, value, maxi, mini, var_id, model, cur):

	if var_id == 1 :
		# for i in range(0, len(value)):
		values = {"rain"	:	"%.1f" %value, 
			  "max"		:	"%.1f" %maxi,
			  "min"		:	"%.1f" %mini,}

		units = {"rain" : {                "current" : cur,
                "label" : "rain",
                "options" : [
                    {
                        "id" : "metric",
                        "label" : "mm"
                    },
                    {
                        "id" : "imperial",
                        "label" : "inch"
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
				"speed" : "%.0f" %value[a], 
				"direction" : "%.0f" %value[b]
			}
			self_value.append(d)
			a = b + 1
			b = b + 2
		values = {"wind"	:	[self_value], 
			  "max"		:	"%.0f" %maxi,
			  "min"		:	"%.0f"%mini,}

 		units = {"wind" : {
			                "current" : cur,
			                "label" : "wind",
			                "options" : [
				                    {
				                        "id" : "metric",
                        				"label" : "m/s"
                    				     },
				                    {
				                        "id" : "imperial",
				                        "label" : "mph"
                    				}]}}
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

	elif var_id == 3:
		# for i in range(0, len(value)):
		values = {"temperature"	:	"%.0f" %value,
			  "max"		:	"%.0f" %maxi,
			  "min"		:	"%.0f"%mini,}

		units = {
			"temperature" : {
                "current" :cur,
                "label" : "Temperature",
                "options" : [ 
                    {
                        "id" : "metric",
                        "label" : "˚C"
                    },
                    {
                        "id" : "imperial",
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
					"message" : "Card OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 4:
		# for i in range(0, len(value)):
		values = {"radiation"	:	"%.0f," %value,
			  "max"		:	"%.0f" %maxi,
			  "min"		:	"%.0f"%mini,}
		units = {"radiation" : {
                "current" : cur,
                "label" : "radiation",
                "options" : [
                    {
                        "id" : "metric",
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
					"message" : "Card OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 5:
		# for i in range(0, len(value)):
		values = {"humidity"	:	"%.0f" %value,
			  "max"		:	"%.0f" %maxi,
			  "min"		:	"%.0f"%mini,}
		units = {"humidity" : {
                "current" : cur,
                "label" : "humidity",
                "options" : [
                    {
                        "id" : "metric",
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
					"message" : "Card OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 6:
		# for i in range(0, len(value)):
		values = {"figures"	:	'%s' %value,}
		units = {"figures" : {
                "current" : cur,
                "label" : "cond_figures",
	  		       },}
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

	elif var_id == 7:	
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
					"message" : "Card OK!",
					"status" : 0 
					}
				}
		success = True

	else:
		success, dic = _get_ERROR(var_id, model)
			
	return(success, dic)

def _get_calendar(date, prob, alert, color, value, maxi, mini, var_id, model, cur):

	dic = {}
	values = []
	success = True
	if var_id == 1:
		for i in range(0, len(value)):
			resp	=	{
        	        	"main" : {
            	        			"color" : alert[i],
                	    			"value" : value[i]

                    			},
	                	"otherValues" : {
    	                					"max" : maxi[i], 
        	            					"min" : mini[i]
            	    					},
                		"percentage" : {
                    					"value" : int(prob[i]*100),
                    					"color" : color[i]
                						}
	            		}
			values.append(resp)

		units = {"rain" : {                "current" : cur,
        	        "options" : [
            	        {
                	        "id" : "metric",
                    	    "label" : "mm"
                    	},
                    	{
                        	"id" : "imperial",
                        	"label" : "inch"
                    	}
                	]}}

		dic = {"data" : {
							"startDate" : date[0].strftime('%Y-%m-%d 00:00:00'),
							"endDate" : date[-1].strftime('%Y-%m-%d 00:00:00'),
							"type" : "rain", 
							"success" : 0,
							"message" : "Calendário carregado com sucesso",
							"units"	  : units,
							"data" : values      
							}
				}

	elif var_id == 2:
		for i in range(0, len(alert)):
			val = value[i]
			resp	=	{
        	        	"main" : {
            	        			"color" : alert[i],
                	    			"value" : { "speed" : val[0],
                                                "direction" : val[1]},
                	    			# "value" : value[i, 0],
                                               
                    			},
	                	"otherValues" : {
    	                					"max" : maxi[i], 
        	            					"min" : mini[i]
            	    					},
                		"percentage" : {
                    					"value" : int(prob[i]*100),
                    					"color" : color[i]
                						}
	            		}
			values.append(resp)

		units = {"wind" : {                "current" : cur,
        	        "options" : [
            	        {
                	        "id" : "metric",
                    	    "label" : "m/s"
                    	},
                    	{
                        	"id" : "imperial",
                        	"label" : "mph"
                    	}
                	]}}

		dic = {"data" : {
							"startDate" : date[0].strftime('%Y-%m-%d 00:00:00'),
							"endDate" : date[-1].strftime('%Y-%m-%d 00:00:00'),
							"type" : "wind",
							"success" : 0,
							"message" : "Calendário carregado com sucesso",
							"units"	  : units,
							"data" : values      
							}
				}

	elif var_id == 3:
		for i in range(0, len(value)):
			resp	=	{
        	        	"main" : {
            	        			"color" : alert[i],
                	    			"value" : value[i]
                    			},
	                	"otherValues" : {
    	                					"max" : maxi[i], 
        	            					"min" : mini[i]
            	    					},
                		"percentage" : {
                    					"value" : int(prob[i]*100),
                    					"color" : color[i]
                						}
	            		}
			values.append(resp)

		units = {"temp" : {                "current" : cur,
        	        "options" : [
            	        {
                	        "id" : "metric",
                    	    "label" : "ºC"
                    	},
                    	{
                        	"id" : "imperial",
                        	"label" : "ºF"
                    	}
                	]}}

		dic = {"data" : {
							"startDate" : date[0].strftime('%Y-%m-%d 00:00:00'),
							"endDate" : date[-1].strftime('%Y-%m-%d 00:00:00'),
							"type" : "temp",
							"success" : 0,
							"message" : "Calendário carregado com sucesso",
							"units"	  : units,
							"data" : values      
							}
				}
	elif var_id == 4:
		for i in range(0, len(value)):
			resp	=	{
        	        	"main" : {
            	        			"color" : alert[i],
                	    			"value" : value[i]
                    			},
	                	"otherValues" : {
    	                					"max" : maxi[i], 
        	            					"min" : mini[i]
            	    					},
                		"percentage" : {
                    					"value" : int(prob[i]*100),
                    					"color" : color[i]
                						}
	            		}
			values.append(resp)

		units = {"radiation" : {                "current" : cur,
        	        "options" : [
            	        {
                	        "id" : "metric",
                    	    "label" : "W"
                    	},
                	]}}

		dic = {"data" : {
							"startDate" : date[0].strftime('%Y-%m-%d 00:00:00'),
							"endDate" : date[-1].strftime('%Y-%m-%d 00:00:00'),
							"type" : "radiation",
							"success" : 0,
							"message" : "Calendário carregado com sucesso",
							"units"	  : units,
							"data" : values      
							}
				}
	elif var_id == 5:
		for i in range(0, len(value)):
			resp	=	{
        	        	"main" : {
            	        			"color" : alert[i],
                	    			"value" : value[i]
                    			},
	                	"otherValues" : {
    	                					"max" : maxi[i], 
        	            					"min" : mini[i]
            	    					},
                		"percentage" : {
                    					"value" : int(prob[i]*100),
                    					"color" : color[i]
                						}
	            		}
			values.append(resp)

		units = {"humidity" : {                "current" : cur,
        	        "options" : [
            	        {
                	        "id" : "metric",
                    	    "label" : "%"
                    	},
                	]}}

		dic = {"data" : {
							"startDate" : date[0].strftime('%Y-%m-%d 00:00:00'),
							"endDate" : date[-1].strftime('%Y-%m-%d 00:00:00'),
							"type" : "humidity",
							"success" : 1,
							"message" : "Calendário carregado com sucesso",
							"units"	  : units,
							"data" : values      
							}
				}
	elif var_id == 6:
		values = {"figures"	:	[value]}
		units = {"figures" : {
                "current" : cur,
                "label" : "cond_figures",
	  		       },}
		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d 00:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d 00:00:00'),
					"units" : units,
					"values" : values,
					"message" : "Card OK!",
					"status" : 0 
					}}
	
	else:
		success, dic = _get_ERROR(var_id, model)				
	return(success, dic)

def _get_gcard(date, value, var_id, model, cur):
	if var_id == 1 :
		values = {"rain"	:	[value],}
		units = {"rain" : {                "current" : cur,
                "label" : "rain",
                "options" : [
                    {
                        "id" : "metric",
                        "label" : "mm"
                    },
                    {
                        "id" : "imperial",
                        "label" : "inch"
                    }
                ]}}
		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "GCard OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 2:
		values = {"wind"	:	[value],}
 		units = {"wind" : {
			                "current" : cur,
			                "label" : "wind",
			                "options" : [
				                    {
				                        "id" : "metric",
                        				"label" : "m/s"
                    				     },
				                    {
				                        "id" : "imperial",
				                        "label" : "mph"
                    				}]}}
		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "GCard OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 3:
		self_value = []
		for i in range(0, len(value)):
			val = value[i]
			d = {
				"max" : int(val[0]*10)/10.0, 
				"min" : int(val[1]*10)/10.0
			}
			self_value.append(d)
		values = {"temperature"	:	[self_value],}
		units = {
			"temperature" : {
                "current" :cur,
                "label" : "Temperature",
                "options" : [ 
                    {
                        "id" : "metric",
                        "label" : "˚C"
                    },
                    {
                        "id" : "imperial",
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
					"message" : "GCard OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 4:
		values = {"radiation"	:	[value],}
		units = {"radiation" : {
                "current" : cur,
                "label" : "radiation",
                "options" : [
                    {
                        "id" : "metric",
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
					"message" : "GCard OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 5:
		values = {"humidity"	:	[value],}
		units = {"humidity" : {
                "current" : cur,
                "label" : "humidity",
                "options" : [
                    {
                        "id" : "metric",
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
					"message" : "GCard OK!",
					"status" : 0 
					}}
		success = True

	elif var_id == 6:
		values = {"figures"	:	[value]}
		units = {"figures" : {
                "current" : cur,
                "label" : "cond_figures",
	  		       },}
		dic = {"data" :{
					"type"  : "horizontal",
					"stepLength" : "1",
					"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
					"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
					"units" : units,
					"values" : values,
					"message" : "GCard OK!",
					"status" : 0 
					}}
		success = True

	else:
		success, dic = _get_ERROR(var_id, model)
			
	return(success, dic)

def _get_meteogram(dat, value):
	value0 = []
	value1 = []
	value2 = []
	value3 = []
	value4 = []
	value5 = []
	value6 = []
	value7 = []
	value8 = []
	date=[]
	# for i in range(0, len(value)):
	for val, i in value:
#		val = value[i]
		value0.append(val[0])
		value1.append(val[1])
		value2.append(val[2])
		value3.append(val[3])
		value4.append(val[4])
		value5.append(val[5])
		value6.append(val[6])
		value7.append(val[7])
		value8.append(val[8])
		date.append(dat[i])
	values = {	
				"temp"		:	[value0[:]],
				"wind"		:	[value1[:]],
				"humidity"	:	[value2[:]],
				"cloud"		:	[value3[:]],
				"rain"		:	[value4[:]],
				"pressure"	:	[value5[:]],
				"dew"		:	[value6[:]],
				"cape"		:	[value7[:]],
				"gust"		:	[value8[:]],
			}
	units = {"label"	:[	{"temp"		:	"C"},
							{"wind"		:	"m/s"},
							{"humidity"	:	"%"},
							{"cloud"	:	"%"},
							{"rain"		:	"mm"},
							{"pressure"	:	"hPa"},
							{"dew"		:	"C"},
							{"cape"		:	"%"},
							{"gust"		:	"m/s"},
						]
			}
	dic = {"data" :{
				"type"  : "horizontal",
				"stepLength" : "1",
				"startDate" : date[0].strftime('%Y-%m-%d %H:00:00'),
				"endDate" : date[-1].strftime('%Y-%m-%d %H:00:00'),
				"units" : units,
				"values" : values,
				"message" : "Meteogram OK!",
				"status" : 0 
				}}
	success = True
	return(success, dic)

def _get_ERROR(var_id, model):
	import datetime
	var = _get_Name(var_id)
	if model == "calendar":
		mess = "%s Calendar  not working" %(var)
	elif model == "card":
		mess = "%s Card  not working" %(var)
	elif model == "table":
		mess = "%S Table not working" %(var)
	else:
		mess = "Sytem is Down"

	dic = {
			"message"	: mess,
			"status"	: 1,
			"time"		: datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			}

	return(False, dic)

def _get_AUX(utc, sun_set, sun_rise, point, w_out, g_out, c_out):
	dic ={"data" : 
		{"models" :[ 
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
		]}, 
		"message"	: "System is UP",
		"status"	: 0,
		"sun_set"	: sun_set,
		"sun_rise"	: sun_rise,
		"timezone"	: utc,


	}
	success = True
	return(success, dic)
