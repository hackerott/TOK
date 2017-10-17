#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


class RidgeRegressor(object):
	"""
	Linear Least Squares Regression with Tikhonov regularization.
	More simply called Ridge Regression.

	Theta = (X'X + G'G)^-1 X'y
	Where X contains the independent variables, y the dependent variable and G
	is matrix alpha * I, where alpha is called the regularization parameter.
	When alpha=0 the regression is equivalent to ordinary least squares.
	
	"""

	def fit(self, X, y, alpha=0):
		"""
		X: mxn matrix of m examples with n independent variables
		y: dependent variable vector for m examples
		alpha: regularization parameter. A value of 0 will model using the
		ordinary least squares regression.
		"""
		X = np.hstack((np.ones((X.shape[0], 1)), X))
		G = alpha * np.eye(X.shape[1])
#		G[0, 0] = 0  # Don't regularize bias
		self.params = np.dot(np.linalg.inv(np.dot(X.T, X) + np.dot(G.T, G)), np.dot(X.T, y))

	def predict(self, X):
		"""
		X: mxn matrix of m examples with n independent variables
		alpha: regularization parameter. Default of 0.
		Returns
		"""
		X = np.hstack((np.ones((X.shape[0], 1)), X))
		return np.dot(X, self.params)

