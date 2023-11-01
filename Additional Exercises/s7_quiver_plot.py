#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:06:33 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt

def valueV1(x,y):
    return np.exp( - (x-1)**2 - (y+1)**2 )

def valueV2(x,y):
    return np.exp( - (x+1)**2 - (y-1)**2 )

def valueV(x,y):
    V1 = valueV1(x,y)
    V2 = valueV2(x,y)
    return V1-V2

def valueE(x,y):
    V1 = valueV1(x,y)
    V2 = valueV2(x,y)
    Ex = -2*(x-1)*V1 + 2*(x+1)*V2
    Ey = -2*(y+1)*V1 + 2*(y-1)*V2
    return Ex, Ey
    

x = np.linspace(-2,2,15)
y = np.linspace(-2,2,15)
xx, yy = np.meshgrid(x,y)

V = valueV(xx,yy)
plt.contourf(xx,yy,V, 10)
plt.colorbar()

Ex, Ey = valueE(xx,yy)

plt.quiver(xx,yy,Ex,Ey)

plt.xlabel('x coordinate')
plt.ylabel('y coordinate')
plt.title('Electric potential and field')
#plt.show()
plt.savefig('s7_electric_potential_plot.png')