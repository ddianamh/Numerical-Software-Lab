#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:33:40 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

fig, ax = plt.subplots(1,2, figsize=(9.2, 4), subplot_kw={'projection': '3d'})
a=2
b=3
for i in range(2):
    ax[i].set_zlim(-2, 2)
    ax[i].xaxis.set_ticks(range(a+1))
    ax[i].yaxis.set_ticks(range(b+1))
    ax[i].set_xlabel('x')
    ax[i].set_ylabel('y')
    ax[i].set_zlabel('$V(x,y)$')
    ax[i].view_init(40, -30)

fig.subplots_adjust(left=0.04, bottom=0.04, right = 0.96, top = 0.96, wspace = 0.05)
p0 = ax[0].plot_wireframe(xx,yy,V, rcount=40, ccount=40, color='C1')
p1 = ax[1].plot_surface(xx,yy,V, rcount=50, ccount=50, color='C2')
fig.subplots_adjust(left=0.0)
fig.savefig('s7_wireframe_surface.pdf')

plt.show()