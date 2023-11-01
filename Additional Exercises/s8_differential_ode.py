#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:05:43 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y, x):
    derivs = x-y
    return derivs

def ff(x):
    y = x-1+2*np.exp(-x)
    return y


x = np.arange(0., 5, 0.05) 

y0 = 1
psoln = odeint(f, y0, x)
print(psoln)

# fig = plt.figure(1, figsize=(8,8))
# ax1 = fig.add_subplot(311)
# ax1.plot(x, psoln, 'b-')

y = ff(x)
# ax1.plot(x, y, 'r-')

difference = psoln[:,0]-y
plt.semilogy(x, difference)

plt.savefig("First-order_equations.pdf")

plt.show()

