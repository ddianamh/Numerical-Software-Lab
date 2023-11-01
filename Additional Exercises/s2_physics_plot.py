#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:40:13 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(10, 0, -0.5)
h0 = 10
g = 9.81
t = np.sqrt( 2*(h0-y) / g )

print( t )

plt.figure(1, figsize = (6,4) )
plt.plot(t, y, 'r-', label="y=$h_0-0.5gt^2$")
plt.xlabel('time')
plt.ylabel('position') 
plt.legend(loc='lower left')
#plt.axhline(color = 'gray', zorder=-1)
#plt.axvline(color = 'gray', zorder=-1)
# save plot to file
plt.savefig('s2_physics_plot.pdf')
# display plot on screen
plt.show()