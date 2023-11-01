#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dianah
"""

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
def f(x):
    y = x * np.sin( (3/x) ) + 0.25
    return y
#Brent method
#finding true roots for f
rx1 = scipy.optimize.brentq(f, 0.01, 0.27)
rx2 = scipy.optimize.brentq(f, 0.27, 0.5)
rx3 = scipy.optimize.brentq(f, 0.5, 0.75)
rx4 = scipy.optimize.brentq(f, 0.75, 1)
rx5 = scipy.optimize.brentq(f, -1, -0.75)
rx6 = scipy.optimize.brentq(f, -0.75, -0.5)
rx7 = scipy.optimize.brentq(f, -0.5, -0.27)
rx8 = scipy.optimize.brentq(f, -0.27, -0.01)
rx = np.array([rx1, rx2, rx3, rx4, rx5, rx6, rx7, rx8])
ry = np.zeros(8)
print("i) Roots using Brent method: \n", rx)

#Newton method
#defining the first derivative
#calculating it on paper
def fprime(x):
    y = np.sin( (3/x) ) - 3.0 * (1/x) * np.cos( (3/x) )
    return y
nrx1 = scipy.optimize.newton(f, 0.26, fprime)
nrx2 = scipy.optimize.newton(f, 0.28, fprime)
nrx3 = scipy.optimize.newton(f, 0.5, fprime)
nrx4 = scipy.optimize.newton(f, 0.8, fprime)
nrx5 = scipy.optimize.newton(f, -0.8, fprime)
nrx6 = scipy.optimize.newton(f, -0.5, fprime)
nrx7 = scipy.optimize.newton(f, -0.28, fprime)
nrx8 = scipy.optimize.newton(f, -0.26, fprime)
nrx = np.array([nrx1, nrx2, nrx3, nrx4, nrx5, nrx6, nrx7, nrx8])
nry = np.zeros(8)
print("ii) Roots using Newton method: \n", nrx)

#plotting
x = np.linspace(-1, 1, 256)
y = f(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.plot(nrx, nry, 'r.')
ax.xaxis.grid(True)
ax.yaxis.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
plt.show()