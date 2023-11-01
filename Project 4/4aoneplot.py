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
def solve_plot_ODE(t, a, b, c, omega, start, end, x0 = 1, v0 = 0):
    #making array of the parameters from the function arguments
    #parameters should be a,b,c, omega
    #initial values for x and v
    params = [a, b, c, omega]
    y0 = [x0, v0]
    
    #calling ODE solver
    psoln = odeint(f, y0, t, args=(params,))
    
    #plotting figure
    plt.figure(1, figsize=(6,6) )
    #adding title to the whole plot
    plt.title("Second Order Differential Equation Plot" )
    
    #plotting x and v as a function of time
    #with the start and end limits
    plt.plot(t, psoln[:,0], 'r-')
    plt.plot(t, psoln[:,1], 'b-')
    plt.ylim(start, end)
    plt.xlabel('time') 
    plt.ylabel('x and v')
    plt.legend("xv", loc = 'upper left')
    plt.savefig("PlotProject4.pdf")
    plt.close()
    
    #txt file with time and x and comma delimiter
    info = 'time t                       x   '
    np.savetxt("Project4_ODE_time_x.txt", 
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
start = 0
end = 60
print("Starting and ending values for the plot are: ", start, end )

print("\nCalling the function results in: ")
y = [np.empty_like(1),np.empty_like(0)]
solve_plot_ODE(t, a, b, c, omega, start, end)
print(solve_plot_ODE(t, a, b, c, omega, start, end))




    
    