#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:40:43 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
#np.where(condition, output if True, output if False)

def j0(x):
    y = np.where( x == 0, 1.0, np.sin(x) / x )
    return y

def j1(x):
    y = np.where( x == 0, 1.0, np.sin(x) / ( x ** 2 ) - np.cos(x) / x )
    return y

def j2(x):
    res = (3 / (x ** 2) - 1 ) * (np.sin(x) / x) * (3 * np.cos(x) / (x ** 2) )
    y = np.where( x == 0, 1.0, res )
    return y
    
x = np.arange(0, 20., 0.5)