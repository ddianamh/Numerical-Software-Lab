#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:00:55 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so

#function
def temperatures(t, a, w, t0, Tbar ):
    T = Tbar + a * np.cos( w * ( t + t0) )
    return T

#data arrays
maxT = np.array([17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18])
minT = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])

#applying curve_fit
p0 = [20, 2*np.pi/12, 0, -40] 
params_max, params_covariance_max = so.curve_fit(temperatures, range(12), maxT, p0)
params_min, params_covariance_min = so.curve_fit(temperatures, range(12), minT, p0)
t = np.linspace(0, 11, 100)

#plotting
plt.plot(range(12), maxT, 'ro', label='Max Temperatures')
plt.plot(range(12), minT, 'go', label='Min Temperatures')
plt.plot(t, temperatures(t, *params_max), 'k-', label='Max Temperatures Fit')
plt.plot(t, temperatures(t, *params_min), 'b-', label='Min Temperstures Fit')
plt.legend()
plt.show()

