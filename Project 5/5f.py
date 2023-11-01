#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dianah
"""

import numpy as np
from scipy import fftpack
from scipy import optimize
import matplotlib.pyplot as plt
Polynomial = np.polynomial.Polynomial

x, y = np.loadtxt('nsl23_5.dat', dtype = 'float',
                  skiprows=0, usecols=(4,6), unpack=True)

#plotting as linear fit
#linear fit means poly of degree 1
#examples from the "Learning scientific programmin with Python" book from lecture 11
xmin = min(x)
xmax = max(x)
p1, stats1 = Polynomial.fit(x, y, 1, full=True, window=(xmin, xmax),
                             domain=(xmin, xmax) )
fig = plt.figure(1, figsize=(15,30)) 
ax1 = fig.add_subplot(711)
ax1.plot(x, p1(x), 'b-', label = 'linear fit')
ax1.plot(x, y, 'ro', label = 'data')
ax1.legend(loc = 'lower right')
ax1.set_xlabel('x' )
ax1.set_ylabel('y') 


#plotting as second degree polynomial fit
p2, stats2 = Polynomial.fit(x, y, 2, full=True, window=(xmin, xmax),
                             domain=(xmin, xmax) )
ax2 = fig.add_subplot(712)
ax2.plot(x, p2(x), 'b-', label = '2nd degree polynomial fit')
ax2.plot(x, y, 'ro', label = 'data')
ax2.legend(loc = 'lower right')
ax2.set_xlabel('x' )
ax2.set_ylabel('y') 


#plotting as second degree polynomial fit
p5, stats5 = Polynomial.fit(x, y, 5, full=True, window=(xmin, xmax),
                             domain=(xmin, xmax) )
ax3 = fig.add_subplot(713)
ax3.plot(x, p5(x), 'b-', label = '5th degree polynomial fit')
ax3.plot(x, y, 'ro', label = 'data')
ax3.legend(loc = 'lower right')
ax3.set_xlabel('x' )
ax3.set_ylabel('y') 


#plotting for that curve fit
def test_func(x, a, b, c, d):
    y = a * np.sin(b-x) + c * x * x+ d
    return y

params, params_covariance = optimize.curve_fit(test_func, x, y)

y_curve = test_func(x, params[0], params[1], params[2], params[3])

ax4 = fig.add_subplot(714)
ax4.plot(x, y_curve, 'b-', label = 'miscellaneous curve fit')
ax4.plot(x, y, 'ro', label = 'data')
ax4.legend(loc = 'lower right')
ax4.set_xlabel('x' )
ax4.set_ylabel('y') 


#the FFT plot of the original data
#increment between times in x array
dx = x[1] - x[0]
#FFT of y
Y = fftpack.fft(y)
Ycopy = Y
#frequencies f1[i] of y[i]
f1 = fftpack.fftfreq(y.size, d=dx)
# shift frequencies from min to max
f1 = fftpack.fftshift(f1) 
# shift Y order to coorespond to f1
Y = fftpack.fftshift(Y)

ax5 = fig.add_subplot(715)
ax5.plot(f1, np.real(Y), color='blue', label='real part - FFT')
ax5.plot(f1, np.imag(Y), color='red', label='imaginary part - FFT')
ax5.legend()


#the FFT plot of the data from the curve in iv) 
#FFT of y_curve
YC = fftpack.fft(y_curve)
#frequencies f2[i] of y_curve[i]
f2 = fftpack.fftfreq(y_curve.size, d=dx)
# shift frequencies from min to max
f2 = fftpack.fftshift(f2) 
# shift YC order to coorespond to f2
YC = fftpack.fftshift(YC)

ax6 = fig.add_subplot(716)
ax6.plot(f1, np.real(YC), color='blue', label='real part - FFT curve iv)')
ax6.plot(f1, np.imag(YC), color='red', label='imaginary part - FFT curve iv)')
ax6.legend()


#inverse FFT
yy = fftpack.ifft(Ycopy)
ax7 = fig.add_subplot(717)
ax7.plot(x, yy, 'ko', label = 'data from Fourier back-transformation')
ax7.plot(x, yy, 'r*', label = 'original data')
ax7.legend(loc = 'lower right')
#saving the figure to see better
plt.savefig("AllPlots.pdf")
plt.show()
