#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:18:02 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    res = np.where( (x == 0.0 and y == 0.0), 0.0, (x ** 3) * y / ( x ** 6 + y ** 2 ) )
    return np.asarray(res)



x = np.arange(0, 5., 0.5)
y = [0, 1, 3, 5]
plt.figure(1, figsize = (6,4) )
plt.plot(x, f(x,y[0]), 'b-')
plt.plot(x, f(x,y[1]), 'r-')
plt.plot(x, f(x,y[2]), 'g-')
plt.plot(x, f(x,y[3]), 'y-')
plt.xlabel('x')
plt.ylabel('f') 
plt.legend(loc='upper right')
plt.axhline(color = 'gray', zorder=-1)
plt.axvline(color = 'gray', zorder=-1)
# save plot to file
# display plot on screen
plt.show()