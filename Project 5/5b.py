#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dianah
"""

import numpy as np
import random
import scipy.linalg
i = 0
j = 0
#creating matrix
#at first it has elts from 0 to 99 but will get overwritten
matrix = np.arange(100, dtype = 'float')
#reshaping to get 10x10 matrix
matrix = np.reshape(matrix, (10,10))

for i in range(0,10) :
    for j in range(0,i+1) :
        matrix[i][j] = random.uniform(-10,10)
        matrix[j][i] = matrix[i][j]
#print(matrix)
#eigenvalues and eigenvectors
lam, evec = scipy.linalg.eig(matrix)
#saving in a file
np.savetxt("5b.txt", 
           list(zip(lam, evec)),
           fmt  = "%s", 
           delimiter = '\n',
           header = "Eigenvalues and the corresponding eigenvectors\n"
           )

