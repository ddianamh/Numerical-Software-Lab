#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:10:57 2023

@author: dianah
"""

import numpy as np

f, a, da = np.loadtxt('s5_data.txt', skiprows = 0, unpack = True )

np.set_printoptions( precision = 3 )
print("frequency: ", f )

np.set_printoptions( precision = 1 )
print("amplitude: ", a ) 
print("amp error: ", da)