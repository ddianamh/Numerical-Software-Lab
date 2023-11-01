#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dianah
"""

#for 4a my file was in two columns instead of two rows
#but i modified it as follows

#    
    #info = 'time t (first row) and x (second row)  '
    # np.savetxt("ODE_time_x.txt", 
    #           (t, psoln[:,0]),
    #           header = info,
    #           delimiter = ',')
    
#i  will use this one, with t on the first row and x on the second row

import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

width = 2.0
freq = 0.5
#reading t and x
t, x = np.loadtxt('ODE_time_x.txt', skiprows = 1, delimiter = ',' )

#proceeding with the fourier transformation
#increment between times in time array
dt = t[1] - t[0]
#FFT of x
X = fftpack.fft(x)
#frequencies f[i] of x[i]
f = fftpack.fftfreq(x.size, d=dt)
# shift frequencies from min to max
f = fftpack.fftshift(f) 
# shift X order to coorespond to f
X = fftpack.fftshift(X)

fig = plt.figure(1, figsize=(8,6)) 
plt.suptitle("Fourier Transformation Plot", fontsize = 'x-large' )
ax = fig.add_subplot(111)
ax.plot(f, np.real(X), color='blue', label='real part')
ax.plot(f, np.imag(X), color='red', label='imaginary part')
ax.legend()
ax.set_xlabel('f' )
ax.set_ylabel('X(f)') 
plt.savefig("PlotFourier.pdf")
plt.show()