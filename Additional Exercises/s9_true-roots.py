#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:55:07 2023

@author: dianah
"""

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
#defining functions
def f1(x):
     y = 4 * x * x - 3
     return y

def f2(x):
    y = x * x * x - x
    return y

#finding roots for f1
rx1 = scipy.optimize.brentq(f1, 0, 1)
rx2 = scipy.optimize.brentq(f1, -0.9, 0)
rx = np.array([rx1, rx2])
ry = np.zeros(2)

#finding roots for f2
rrx1 = scipy.optimize.brentq(f2, -0.1, 0.1)
rrx2 = scipy.optimize.brentq(f2, -1.1, -0.9)
rrx3 = scipy.optimize.brentq(f2, 0.9, 1.1)
rrx = np.array([rrx1, rrx2, rrx3])
rry = np.zeros(3)

#plotting f1
x = np.linspace(-5, 5, 100)
y = f1(x)

fig = plt.figure ()
ax1 = fig.add_subplot(211)
ax1.set_xlabel("x")
ax1.set_ylabel('$4x^2-3$')
ax1.plot(x, y)
ax1.plot(rx, ry, 'og', label = 'true roots')
ax1.legend(loc='upper center')
#plotting f2
xx = np.linspace(-5, 5, 100)
yy = f2(xx)

ax2 = fig.add_subplot(212)
ax2.set_xlabel("x")
ax2.set_ylabel('$x^3-x$')
ax2.plot(xx, yy)
ax2.plot(rrx, rry, 'og', label = 'true roots')
ax2.legend(loc='upper center')

plt.savefig("True_roots.pdf")
 