#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:04:43 2023

@author: dianah
"""

import numpy as np
import scipy.special
f = lambda x: 1 / (1 + x*x)
print( scipy.integrate.quad( f, -1, 1 ) )

def g(x):
    return 1 / ( (np.exp(x) + x + 1) ** 2 + np.pi ** 2)
print( scipy.integrate.quad( g, -np.inf, np.inf))