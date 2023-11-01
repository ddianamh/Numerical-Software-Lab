#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:40:08 2023

@author: dianah
"""

import numpy as np
import scipy.special

#for all three triple integrals, we include the factor outside within the function
#that needs to be integrated

#numerically integrating for V
def numerical_V(R,r):
    #function to integrate
    f = lambda z, rho, theta: 2 * rho
    #integration ends for left-most integral
    down1 = 0
    up1 = 2 * np.pi
    #integration ends for middle integral
    down2 = lambda theta: R - r
    up2 = lambda theta: R + r
    #integration ends for right-most integral
    down3 = lambda rho, theta: 0
    up3 = lambda rho, theta: np.sqrt( np.abs( r**2 - (rho - R)**2 ))
    #formula 
    V = scipy.integrate.tplquad(f, down1, up1, down2, up2, down3, up3)
    return V

#numerically integrating for Iz
def numerical_Iz(R,r):
    #the 2/V in the formula contains the value of V from the previous function
    #and is the approximate value (ignoring the numerical error)
    Vvalue, Verror = numerical_V(R,r) 
    #function to integrate
    f = lambda z, rho, theta: (2 / Vvalue) * rho**3
    #integration ends for left-most integral
    down1 = 0
    up1 = 2 * np.pi
    #integration ends for middle integral
    down2 = lambda theta: R - r
    up2 = lambda theta: R + r
    #integration ends for right-most integral
    down3 = lambda rho, theta: 0
    up3 = lambda rho, theta: np.sqrt( np.abs( r**2 - (rho - R)**2 ) )
    #formula
    Iz = scipy.integrate.tplquad(f, down1, up1, down2, up2, down3, up3)
    return Iz


#numerically integrating for Ix and Iy
def numerical_IxIy(R,r):
    Vvalue, Verror = numerical_V(R,r) 
    #function to integrate
    f = lambda z, rho, theta: (2 / Vvalue) * (rho**2 * (np.sin(theta))**2 + z**2) * rho
    #integration ends for left-most integral
    down1 = 0
    up1 = 2 * np.pi
    #integration ends for middle integral
    down2 = lambda theta: R - r
    up2 = lambda theta: R + r
    #integration ends for right-most integral
    down3 = lambda rho, theta: 0
    up3 = lambda rho, theta: np.sqrt( np.abs( r**2 - (rho - R)**2 ) )
    #formula
    Ix = scipy.integrate.tplquad(f, down1, up1, down2, up2, down3, up3)
    Iy = Ix
    return Ix, Iy



#numerical test and comparison
print("Input:")
R = 3
r = 2
print("R =", R, "\nr =", r)
print("\nUsing our triple integration functions, we obtain: ")
VV = numerical_V( R, r )
Izz = numerical_Iz( R, r )
Ixx, Iyy =  numerical_IxIy( R, r )
print("V = ",VV, "\nIz = ", Izz, "\nIx = ", Ixx, "\nIy = ", Iyy)

Vvalue = VV[0]
Izvalue = Izz[0]
Ixvalue= Ixx[0]
Iyvalue = Iyy[0]
print("\nThis means that approximately (ignoring the numerical errors), the values are:\n V = ",Vvalue, "\nIz = ", Izvalue, "\nIx = ", Ixvalue, "\nIy = ", Iyvalue)

print("\nCalculating with the exact formulas, we obtain:")
V = 2 * (np.pi ** 2) * R * (r**2)
Iz = R**2 + (r**2) * 3 / 4
Ix = (R**2) / 2 + (r**2) * 5 / 8
Iy = Ix
print(" V = ",V , "\nIz = ", Iz, "\nIx = ", Ix, "\nIy = ", Iy)

print("\nComparing the values obtained using the different methods we can see that they are not exactly equal, but quite close. Since the value of V is different, then Ix, Iy, Iz will also yield different results.")
print("\nHere are the differences (value from the triple integral minus the value from the exact formula):\n")
print("for V:  ", Vvalue - V, "\nfor Iz: ", Izvalue - Iz, "\nfor Ix: ", Ixvalue - Ix, "\nfor Iy: ", Iyvalue - Iy)

