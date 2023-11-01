#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:32:02 2023

@author: dianah
"""
import numpy as np

#function for scalar triple product
#using the numpy cross function
def scalar_triple(a,b,c):
    d = np.cross(b, c)
    result = a[0]*d[0] + a[1]*d[1] + a[2]*d[2]
    return result
    
#creating another scalar triple product function
#which also uses the numpy dot function
#using this more to check if the previous function is ok
def scalar_triple_dot(a,b,c):
    d = np.cross(b, c)
    result = np.dot(a,d)
    return result

#function for vector triple product
def vector_triple(a,b,c):
    d = np.cross(b,c)
    result = np.cross(a,d)
    return result

#function for printing the input and products
def printing(a,b,c):
    print("a =", a, "\nb =", b, "\nc =", c )
    print("\nThe scalar triple product is = ")
    print( scalar_triple(a,b,c) )
    #print( scalar_triple_dot(a,b,c) )
    #used the line above un-commented the first time just for checking
    print("\nThe vector triple product is = ")
    print( vector_triple(a,b,c) )

#arbitrary test values
print("\nFirst arbitrary test:")
a = (1,1,1)
b = (-5,0,0)
c = (2,4,6)
printing(a,b,c)


print("\nKeyboard values test:")
#testing on vectors entered from keyboard
a=[]
b=[]
c=[]

#reading vectors a,b,c
print("\nEnter values for vector a: ")
for i in range(0,3):
    val = float(input())
    a.append(val) 

print("\nEnter values for vector b: ")
for i in range(0,3):
    val = float(input())
    b.append(val)
    
print("\nEnter values for vector c: ")
for i in range(0,3):
    val = float(input())
    c.append(val) 
#testing 
printing(a,b,c)