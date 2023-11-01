#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 18:33:27 2023

@author: dianah
"""
import random
#function that prints number of C and A for a string
def numberCA( s ):
    c = 0
    a = 0
    for i in s:
        if i == 'C':
            c = c+1
        elif i == 'A':
            a = a+1
    print("For the string ", s, " there are ", c, "C and ", a, "A.\n" )        
        

#written tests that I used 
s1 = "AAAAACCCGTAA"
numberCA(s1)
#7A, 3C
s2 = "TG"
numberCA(s2)
#0A, 0C
s3 = "ACACGT"
numberCA(s3)
#2A, 2C

#read a string from keyboard and test on it 
print("\nIntroduce input from keyboard:  ")
s = input()
numberCA(s)
