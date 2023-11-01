#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:23:17 2023

@author: dianah
"""
# Given a string of length greater five, e.g., ’Mercator’ return a 
#number yielding the length of the string and create a string made of the third
#and fourth chars of that given string. Use the functions upper and lower to 
#yield the string of the two extracted characters in all upper or all lowercase
#characters.

s = "Mercator"
length = len( s )
print( length )

s2 = s[3] + s[4]
print( s2 )

s3 = s2.upper()
print( s3 )