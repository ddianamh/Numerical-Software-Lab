#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:12:22 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#using the model from lecture notes 8

def f(y, t,  params):
    #unpacking y values
    x, v = y
    #unpacking parameters
    a,b,c,omega = params
    #list of dy/dt
    derivs = [v, a*(1-x)*v - b*x*x + c*np.cos(omega*t)]
    return derivs

#putting x0 and v0 at the end because they are default arguments and putting them in the middle
#yields an error
def solve_plot_ODE(t, a, b, c, omega, xstart, xend, vstart, vend, x0 = 1, v0 = 0):
    #making array of the parameters from the function arguments
    #parameters should be a,b,c, omega
    #initial values for x and v
    params = [a, b, c, omega]
    y0 = [x0, v0]
    
    #calling ODE solver
    psoln = odeint(f, y0, t, args=(params,))
    
    #plotting figure
    fig = plt.figure(1, figsize=(10,10) )
    #adding title to the whole plot
    plt.suptitle("Second Order Differential Equation Plots", fontsize = 'x-large' )
    
    #plotting x as a function of time
    #with the xstart and xend limits
    ax1 = fig.add_subplot(321) 
    ax1.set_title("x as a function of time")
    ax1.plot(t, psoln[:,0], 'r-')
    ax1.set_ylim(xstart, xend)
    ax1.set_xlabel('time') 
    ax1.set_ylabel('x')
    ax1.legend("x", loc = 'upper left')
    
    #plotting v as a function of time
    #with the vstart and vend limits
    ax2 = fig.add_subplot(322) 
    ax2.set_title("v as a function of time")
    ax2.plot(t, psoln[:,1],'b-')
    ax2.set_ylim(vstart, vend)
    ax2.set_xlabel('time') 
    ax2.set_ylabel('v')
    ax2.legend("v", loc = 'upper left')
    
    #plotting x and v as functions of time
    ax3 = fig.add_subplot(312) 
    ax3.set_title("x and v as functions of time")
    ax3.plot(t, psoln[:,0],'r-')
    ax3.plot(t, psoln[:,1],'b-')
    ax3.set_xlabel('time') 
    ax3.set_ylabel('x and v')
    ax3.legend("xv", loc = 'upper left')

    fig.tight_layout()
    plt.savefig("PlotODE.pdf")
    plt.close()
    
    #txt file with time and x and comma delimiter
    info = 'time t                       x   '
    np.savetxt("ODE_time_x.txt", 
               list(zip(t, psoln[:,0])),
               header = info,
               delimiter = ',')
    
    return psoln

#main part 
#introducing arbitrary input values
print("Input :\n")
a = 3
print("a =", a)
b = -1
print("b =", b)
c = 1
print("c =", c)
omega = 2
print("omega=", omega)
print("Letting default values for x0 and v0, i.e. 1 and 0, respectively.\n")
t = np.arange(0, 10, 0.05)
print("t=", t)
xstart = 0
xend = 100
print("Starting and ending values for x for the plot are: ", xstart, xend )
vstart = 0
vend = 20
print("Starting and ending values for v for the plot are: ", vstart, vend )
print("\nCalling the function results in: ")
y = [np.empty_like(1),np.empty_like(0)]
solve_plot_ODE(t, a, b, c, omega, xstart, xend, vstart, vend)
print(solve_plot_ODE(t, a, b, c, omega, xstart, xend, vstart, vend))




    
    