#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 00:53:48 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#looking in the given book, we see that we need to import scipy.special
#for special functions like the Bessel ones
import scipy.special

def spherical_bessel(kind, n, rx, ry):
    #creating x, y from the range
    x = np.linspace(rx[0], rx[1], 256)
    y = np.linspace(ry[0], ry[1], 256)
    
    X, Y = np.meshgrid(x, y)
    
    #calculate r
    r = np.sqrt(X*X + Y*Y)
    
    #if kind is 1 then we plot jn for order n and r
    #if it is 2, then yn for order n and r
    if kind == 1:
        f = scipy.special.jn(n,r)
    elif kind == 2:
        f = scipy.special.yn(n,r)
    
    #create the plot for f
    fig = plt.figure ()
    ax = fig.add_subplot( projection = '3d' ) 
    ax.plot_surface(X, Y, f, color = 'C6')
    
    #labeling x and y
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    
    #setting the ticks
    #5 ticks for x axis
    ax.xaxis.set_ticks( np.linspace(rx[0], rx[1], 5 ))
    #5 ticks for y axis
    ax.yaxis.set_ticks( np.linspace(ry[0], ry[1], 5 ))
    #4 ticks for z axis
    #here I used get_zlim() because, in some of my chosen test examples for the
    #bessel functions with x and y not symmetric, I got errors when using 
    #min(f) and max(f)
    minz, maxz = ax.get_zlim()
    ax.zaxis.set_ticks( np.linspace(minz, maxz, 4 ))
    #labeling z axis and putting title according to the kind of the function
    #case 1
    if kind == 1:
        #setting title
        title = "Bessel Spherical Function (first kind) of order n=" + str(n)
        plt.title( title )
        #naming z label
        ax.set_zlabel( "$j_n$")
        #saving as a pdf but not showing on the screen
        plt.savefig("Bessel_3D_Plot_1.pdf")
        plt.close()
    #case 2    
    elif kind == 2:
        #same steps as above
        title = "Bessel Spherical Function (second kind) of order n=" + str(n)
        plt.title( title )
        ax.set_zlabel("$y_n$")
        plt.savefig("Bessel_3D_Plot_2.pdf")
        plt.close()
    
    
#arbitrary test values
print("Input: range of x")
rx = [-20, 20]
print(rx)
print("Input: range of y")
ry = [-20, 20]
print(ry)
print("Input: n")
n = 1
print(n)
#testing both kinds
k1 = 1
print("Input: kind " , k1, " - obtaining plot for j_n")
spherical_bessel(k1, n, rx, ry)
k2 = 2
print("Input: kind " , k2, " - obtaining plot for y_n")
spherical_bessel(k2, n, rx, ry)