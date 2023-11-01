#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:16:34 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

TWOPI = 2*np.pi
fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
s = np.sin(t)
l = plt.plot(t,s)

ax = plt.axis([0, TWOPI, -1, 1])

redDot, = plt.plot([0], [np.sin(0)], 'ro')
 
def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,

myAnimation = animation.FuncAnimation(fig, animate, frames = np.arange(0.0, TWOPI, 0.1), interval = 10, blit = True, repeat = True)

plt.show() 