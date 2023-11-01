#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def test_func(t, amp, freq):
    return amp * np.cos( 2 * np.pi * freq * t)

def noisycosine(t, N, amp, freq, gausswidth, gaussamp):
    #gaussian normal noise 
    gaussiandata = np.random.normal(scale=gausswidth, size = N)
    #cosine function
    #searched for the formula of cosine in terms of amplitude, freq, time
    values = amp * np.cos ( 2 * np.pi * freq * t) + gaussamp * gaussiandata
    return (values, t)

N = 100
t = np.linspace(0, 10, N)
amp = 2
freq = 0.5
gausswidth = 0.5
gaussamp = 0.5
y_data, x_data = noisycosine(t, N, amp, freq, gausswidth, gaussamp)

#using scipy.optimize.curve_fit()
params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[amp,freq])

#plotting the curve fit
fig = plt.figure(1, figsize=(8,6)) 
ax = fig.add_subplot(111)
ax.plot(t, test_func(t, params[0], params[1]), 'b-', label = 'curve fit')
ax.plot(t, y_data, 'ro', label = 'noisy data')
ax.legend(loc = 'upper right')
ax.set_xlabel('time' )
ax.set_ylabel('values') 
plt.show()

#doing the scipy.optimize.minimize

#checking with Newton conjugate gradient trust-region algorithm

#res = optimize.minimize(test_func, -2, args=(params[0], params[1]), method = "trust-ncg", jac = None)
#print(res)

#but it gives the following error "Jacobian is required for Newton-CG trust-region minimization"

#if i give the jacobian, it gives the error for the hessian and so on

#same if i try with the Newton-CG method (only jacobian needed)
#res1 = optimize.minimize(test_func, -2, args=(params[0], params[1]), method = 'Newton-CG')

#so i will calculate the jacobian and hessian too

#calculating the jacobian
#jacobian = derivative
def J(t, a, b):
    return -a * 2 * np.pi * b * np.sin(2 * np.pi * b * t)

#calculating the hessian
#hessian = second derivative
def H(t, a, b):
    return -4 * np.pi * np.pi * b * b * a * np.cos(2 * np.pi * b * t)

res = optimize.minimize(test_func, -2,  args=(params[0], params[1]), method = "trust-ncg", jac = J, hess = H)
print("\nUsing the Newton conjugate gradient trust-region method we get:\n ", res)

#checking with Newton-CG
res1 = optimize.minimize(test_func, -2,  args=(params[0], params[1]), method = "Newton-CG", jac = J)
print("\nUsing the Newton conjugate gradient method we get:\n ",res1)


#checking with Nelder-Mead algorithm
res2 = optimize.minimize(test_func, -2, args=(params[0], params[1]), method = 'Nelder-Mead')
print("\nUsing the Nelder-Mead method we get: \n",res2)