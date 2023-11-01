#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:48:01 2023

@author: dianah
"""
import numpy as np
import scipy.integrate

#creating the function
def f(p,a,b):
    #creating the polynomial ready for integration
    poly = lambda x : np.polyval(p,x)
    #integrating and saving result in two variables
    value, est_error = scipy.integrate.quad(poly, a, b)
    #returning value and estimated error
    return value, est_error

#main part of the script
#printing input
print("Input: vector p of coefficients: ")
p = [1,1,1,1]
#poly should be x^3+x^2+x+1
print(p)
print("Input: starting point a: ")
a = 0
print(a)
print("Input: end point b: ")
b = 10
print(b)
#applying function
v, e = f(p,a,b)
#indefinite integral is x^4/4 + x^3/3 + x^2/2 + x
#mathematically calculating, integral from 0 to 10 should be
#2893.(333...)
#printing output
print("Output: value of the integral: ", v )
print("Output: estimated error: ", e )
#correct values

