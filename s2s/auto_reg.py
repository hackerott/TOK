#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pandas as pd
# import numpy as np
# import datetime
# from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.arima_model import ARIMA

def fit(value, date):
	ds = pd.Series(data=value, index=date)
	model = ARIMA(ds, order=(15,2,10))
	model_fit = model.fit(iprint=0) 
	predict = model_fit.predict(start=end_date[0], end=end_date[-1])
	predict = model_fit.forecast(steps=30)
	return predict
