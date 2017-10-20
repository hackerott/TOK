#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pandas as pd
from statsmodels.tsa.ar_model import AR

class AutoRegressor(object):
	'''
	Simple auto regressor class
	'''
	def fit(self, X, y):
		'''
		X: independent variable
		y: dependent
		'''
		series = pd.Series(y, X)
		X = series.values
		model=AR(X)
		self = model.fit()

	def predict(self, X):
		return(self.predict(start=X[0], end=X[-1], dynamic=False))