#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:05:48 2023

@author: dianah
"""

#Write a Python function that evaluates the mathematical functions f(x) = sin(3x),
#f′(x) = 3cos(3x), and f′′(x) = −9sin(3x). Return these three values. 
#Write out the results of these values for x = pi/2
#
import numpy as np

def f(x):
    return np.sin(3 * x)

def f1(x):
    return 3 * np.cos(3 * x)

def f2(x):
    return -9 * np.sin(3 * x)

print( f(np.pi/2) )
print( f1(np.pi) )
print( f2(np.pi/2) )