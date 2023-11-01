#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:24:17 2023

@author: dianah
"""

import numpy as np
import scipy.linalg

B = np.array([[1,2,3],[4,-5,6],[7,-8,9]])
#determinant
d = scipy.linalg.det(B)
print("\ndeterminant = ", d)
#eigenvalues and eigenvectors
lam, evec = scipy.linalg.eig(B)
print("\neigenvalues = ", lam)
print("\neigenvectors = ", evec)
#transpose 
C = B.T
#inverse
D = scipy.linalg.inv(B)
#transpose of the inverse
Dt = D.T
#inverse of the transpose
Ci = scipy.linalg.inv(C)
#difference
X = Dt - Ci
print("\nfirst difference = ", X)
#product with inverse
P = np.dot(B, D)
#identity matrix
I = np.eye(3)
#difference
Y = P - I
print("\nsecond difference = ", Y)