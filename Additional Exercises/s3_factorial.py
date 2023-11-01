#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:08:07 2023

@author: dianah
"""

#Write a program to calculate the factorial of a positive integer 
#input by the user.

#using while loop
x = int(input())
i = 1 
product = 1
while i <= x:
    product = product * i
    i = i+1
print( product )

#using for loop
product = 1
for i in range(1,x+1,1) :
    product = product * i
print( product )