#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:32:20 2023

@author: dianah
"""

#Consider the matrix list x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. 
#Write a list comprehension to extract the last column of the matrix [3, 6, 9].
#Write another list comprehension to create a vector of twice the square of 
#the middle column [8, 50, 128].

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

last_col = [ x[i][2] for i in [0,1,2] ]
print( last_col )

new_vector = [ 2 * x[i][1] * x[i][1] for i in [0,1,2] ]
print( new_vector )