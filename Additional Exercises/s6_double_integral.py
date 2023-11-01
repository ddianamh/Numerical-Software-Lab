#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:13:38 2023

@author: dianah
"""

import numpy as np
import scipy.special

f = lambda x, y: 3 * x * x * y
h = lambda y: np.sqrt( 4 + 4 * y )
g = lambda y: y
a = int( input() )
b = int( input() )

print(scipy.integrate.dblquad(f, a, b, g, h)) 