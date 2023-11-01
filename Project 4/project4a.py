#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:51:17 2023

@author: dianah
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#using the model from lecture notes 8
#putting x0 and v0 at the end because they are default arguments and putting them in the middle
#yields an error
def solve_plot_ODE(y, t, a, b, c, omega, xstart, xend, vstart, vend, x0 = 1, v0 = 0):
    #unpacking y values
    x, v = y
    
    #making array of the parameters from the function arguments
    #parameters should be a,b,c, omega
    #initial values for x and v
    params = np.array([a, b, c, omega])
    y0 = [x0, v0]
    
    #list of dy/dt
    derivs = [v, a*(1-x)*v - b*x*x + c*np.cos(t)]
    
    #calling ODE solver
    psoln = odeint(derivs, y0, t, args=(params,))
    
    #plotting figure
    fig = plt.figure(1, figsize=(8,8))
    
    #plotting x as a function of time
    #with the xstart and xend limits
    ax1 = fig.add_subplot(311) 
    ax1.plot(t, psoln[:,0], 'b-')
    ax1.y_lim = [xstart, xend]
    ax1.set_xlabel('time') 
    ax1.set_ylabel('x')
    ax1.title("x as a function of time")
    
    #plotting v as a function of time
    #with the vstart and vend limits
    ax2 = fig.add_subplot(312) 
    ax2.plot(t, psoln[:,1], 'r-')
    ax2.y_lim = [vstart, vend]
    ax2.set_xlabel('time') 
    ax2.set_ylabel('v')
    ax1.title("v as a function of time")
    
    #adding title and legend to the whole plot
    plt.title("Second Order Differential Equation Plots")
    plt.legend()
    plt.tight_layout()
    plt.savefig("PlotODE.pdf")
    plt.close()
    
    #txt file with time and x and comma delimiter
    info = 'time t    x   '
    np.savetxt("ODE_time_x.txt", 
               list(zip(t, x)),
               header = info,
               delimiter = ',')
    
    return derivs

#main part 
#introducing arbitrary input values
print("TEST 1 input :\n")
a = 1
print("a=", a)
b = -1
print("b=", b)
c = 1
print("c=", c)
omega = 2
print("omega=", omega)
print("Letting default values for x0 and v0, i.e. 1 and 0, respectively.\n")
t = np.arange(0, 10, 0.5)
print("t=", t)
xstart = -10
xend = 10
print("Starting and ending values for x for the plot are: ", xstart, xend )
vstart = -10
vend = 10
print("Starting and ending values for v for the plot are: ", vstart, vend )
print("Calling the function results in: ")
y = [np.empty_like(1),np.empty_like(0)]
solve_plot_ODE(y, t, a, b, c, omega, xstart, xend, vstart, vend)





    
    