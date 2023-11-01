#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:43:38 2023

@author: dianah
"""

import numpy as np
import scipy.linalg as la
A = np.array([[1,-2,9,13],[-5,1,6,-7],[4,8,-4,-2],[8,5,-7,1]])
b = np.array([1,-3,-2,5])
x1, x2, x3, x4 = la.solve(A,b)
print("solutions\nx1 = ", x1)
print("\nx2 = ", x2)
print("\nx3 = ", x3)
print("\nx4 = ", x4)