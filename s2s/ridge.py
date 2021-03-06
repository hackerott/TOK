#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

class RidgeRegressor(object):
	"""
	Linear Least Squares Regression with Tikhonov regularization.
	More simply called Ridge Regression.

	Theta = (X'X + G'G)^-1 X'y
	Where X contains the independent variables, y the dependent variable and G
	is matrix alpha * I, where alpha is called the regularization parameter.
	When alpha=0 the regression is equivalent to ordinary least squares.
	
	"""
	def fit(self, X, y, alpha=1000):
		"""
		X: mxn matrix of m examples with n independent variables
		y: dependent variable vector for m examples
		alpha: regularization parameter. A value of 0 will model using the
		ordinary least squares regression.
		"""
		x = X
		b = np.ones((X.shape[0],1))
		for i in range(1, 20):
			px = np.power(x, i)
#			x = np.add(x, 0.00001)
			X = np.column_stack((px, X))
		X = np.column_stack((b, X))
		G = alpha * np.matrix(np.eye(X.shape[1]))
#		G[0, 0] = 0  # Don't regularize bias
		self.params = (np.dot(np.linalg.inv(np.dot(X.T, X) + np.dot(G.T, G)), np.dot(X.T, y))).T

	def predict(self, X):
		"""
		X: mxn matrix of m examples with n independent variables
		alpha: regularization parameter. Default of 0.
		Returns
		"""
                x = X
		b = np.ones((X.shape[0],1))
                for i in range(1, 20):
			px = np.power(x, i)
                        X = np.column_stack((px, X))
		X = np.column_stack((b, X))
		return np.dot(X, self.params)

