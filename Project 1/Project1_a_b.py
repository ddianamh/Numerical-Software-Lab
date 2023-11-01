#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 17:25:04 2023

@author: dianah
"""

#a) 

import numpy as np
import matplotlib.pyplot as plt
#creating the x array
x = np.linspace( -10, 10, 201 )
#creting the y array of cos(x)
y = np.cos(x)

print("The y array is \n")
print(y)
print("\n\n\n")

#arrays with o
f1 = x * 0
f3 = x * 0
f5 = x * 0
f7 = x * 0
f9 = x * 0
f11 = x * 0

#N=1
n = 0

while n <= 1:
    factorial = 1
    i = 1
    while i <= 2*n:
        factorial = factorial * i
        i = i + 1
    f1 = f1 + ((-1) ** n) * (x ** (2 * n)) / factorial
    n = n + 1
print("Function for N=1 is \n")    
print(f1)
print("\n\n\n")

#N=3
n = 0

while n <= 3:
    factorial = 1
    i = 1
    while i <= 2*n:
        factorial = factorial * i
        i = i + 1
    f3 = f3 + ((-1) ** n) * (x ** (2 * n)) / factorial
    n = n + 1
print("Function for N=3 is \n")    
print(f3)
print("\n\n\n")

#N=5
n = 0

while n <= 5:
    factorial = 1
    i = 1
    while i <= 2*n:
        factorial = factorial * i
        i = i + 1
    f5 = f5 + ((-1) ** n) * (x ** (2 * n)) / factorial
    n = n + 1
print("Function for N=5 is \n")    
print(f5)
print("\n\n\n")

#N=7
n = 0

while n <= 7:
    factorial = 1
    i = 1
    while i <= 2*n:
        factorial = factorial * i
        i = i + 1
    f7 = f7 + ((-1) ** n) * (x ** (2 * n)) / factorial
    n = n + 1
print("Function for N=7 is \n")    
print(f7)
print("\n\n\n")

#N=9
n = 0

while n <= 9:
    factorial = 1
    i = 1
    while i <= 2*n:
        factorial = factorial * i
        i = i + 1
    f9 = f9 + ((-1) ** n) * (x ** (2 * n)) / factorial
    n = n + 1
print("Function for N=9 is \n")    
print(f9)
print("\n\n\n")

#N=11
n = 0

while n <= 11:
    factorial = 1
    i = 1
    while i <= 2*n:
        factorial = factorial * i
        i = i + 1
    f11 = f11 + ((-1) ** n) * (x ** (2 * n)) / factorial
    n = n + 1
print("Function for N=11 is \n")    
print(f11)
print("\n\n\n")


#b) 
# create plot
plt.title("Taylor expansion of cos(x)")
plt.figure(1, figsize = (12,8) )
plt.ylim([-10,10])
plt.plot(x, y, 'r-', label='cos(x)')
plt.plot(x, f1, 'b--', label='Taylor function for N=1')
plt.plot(x, f3, 'g-.', label='Taylor function for N=3')
plt.plot(x, f5, 'c:', label='Taylor function for N=5')
plt.plot(x, f7, 'm--', label='Taylor function for N=7')
plt.plot(x, f9, 'y-.', label='Taylor function for N=9')
plt.plot(x, f11, 'k:', label='Taylor function for N=11')
plt.xlabel('x')
plt.ylabel('cos(x)') 
plt.legend(loc='upper right', prop = {'size': 6 })
plt.axhline(color = 'gray', zorder=-1)
plt.axvline(color = 'gray', zorder=-1)
# save plot to file
plt.savefig('TaylorExpansionOfCosX.pdf')
# display plot on screen
plt.show() 














