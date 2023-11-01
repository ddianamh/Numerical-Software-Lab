#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:43:01 2023

@author: dianah
"""

import numpy as np
x = 0.25
conv = np.arctan( x )
summ = 0
N = 0
powx = x
while float(str(conv)[:3]) != float(str(summ)[:3]):
    powx = powx * x * x
    if N % 2 == 1:
        summ = summ - powx / (2 * N + 1)
    else:
        summ = summ + powx / (2 * N + 1)
    N = N + 1
    
print( N )
print( conv )
print( summ ) 