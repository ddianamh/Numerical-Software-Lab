#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:48:49 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so

#getting data from the file
data = np.loadtxt('signal1.dat')
x = data[:, 0]
y = data[:, 1]
estimate = data[:, 2]

#function
def model(x, a, b, d, e):
    return a*x + b + np.sin(x/d - e)

#applying curve_fit
params, params_covariance = so.curve_fit(model, x, y, sigma=estimate)
xx = np.linspace(x.min(), x.max(), 1000)
yy = model(xx, *params)

#plotting
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.errorbar(x, y, estimate, fmt='ko', label='Data')
ax.plot(xx, yy, 'r-', label='Model Fit')
ax.legend()
plt.savefig('Fitting_Data.pdf')
plt.close()