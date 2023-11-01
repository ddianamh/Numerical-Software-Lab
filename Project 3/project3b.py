#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:48:01 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#looking in the given book, we see that we need to import scipy.special
#for special functions like the Bessel ones
import scipy.special

def spherical_bessel(x, y, kind, n):
    r = np.sqrt( x*x + y*y ) 
    #if kind is 1 then we plot jn for order n and r
    #if it is 2, then yn for order n and r
    if kind == 1:
        f = scipy.special.jn(n, r)
    elif kind == 2:
        f = scipy.special.yn(n, r)
    #create the plot for f
    fig = plt.figure ()
    ax = fig.add_subplot( projection = '3d' ) 
    #making a 3D line plot like the one in session 7 slide 6
    ax.plot( x, y, f, 'r')
    #labeling x and y
    ax.set_xlabel("x", fontweight = 'bold')
    ax.set_ylabel("y", fontweight = 'bold')
    #setting the ticks
    #5 ticks for x axis
    minx = np.min(x)
    maxx = np.max(x)
    ax.xaxis.set_ticks( np.linspace(minx, maxx, 5 ))
    #5 ticks for y axis
    miny = np.min(y)
    maxy = np.max(y)
    ax.yaxis.set_ticks( np.linspace(miny, maxy, 5 ))
    #4 ticks for z axis
    #here I used get_zlim() because, in my chosen examples for the
    #bessel functions, the plot didn't include min and values (too small
    #or to big) and I got errors when I tried using 
    #minz and maxz as min(f) and max(f)
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
        plt.savefig("Bessel_Spherical_Function_1.pdf")
        plt.close()
    #case 2    
    elif kind == 2:
        #same steps as above
        title = "Bessel Spherical Function (second kind) of order n=" + str(n)
        plt.title( title )
        ax.set_zlabel("$y_n$")
        plt.savefig("Bessel_Spherical_Function_2.pdf")
        plt.close()
    
    
#arbitrary test values
print("Input: x")
x = np.linspace(-10, 10, 256)
print(x)
print("Input: y")
y = np.linspace(0, 20, 256)
print(y)
print("Input: n")
n = 1
print(n)
#testing both kinds
spherical_bessel(x,y,1,n)
spherical_bessel(x,y,2,n)