#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:31:06 2023

@author: dianah
"""

#Generate an equidistant grid that divides the time range [0, 10] into N = 250 
#intervals, and then compute two inverted parabola −(x − 5)^2 and
#−(x/2 − 2.5)^2. Produce a plot of the grid functions using solid but 
#differently colored plot lines, including axes annotations, plot title, 
#and a legend. Store the graphics in your local directory as a pdf file.
 
import numpy as np
import matplotlib.pyplot as plt
# create x and y arrays for theory
x = np.linspace(0, 10, 250)
y1 = - (x-5) * (x-5)
y2 = - (x/2 -2.5 ) * (x/2 -2.5 )
# create plot
plt.figure(1, figsize = (6,4) )
plt.plot(x, y1, 'b-', label="y=$−(x − 5)^2$")
plt.plot(x, y2, 'r-', label="y=$−(0.5x − 2.5)^2$") 
plt.xlabel('position')
plt.ylabel('height') 
plt.legend(loc='lower center')
#plt.axhline(color = 'gray', zorder=-1)
#plt.axvline(color = 'gray', zorder=-1)
# save plot to file
plt.savefig('s2_plot.pdf')
# display plot on screen
plt.show()