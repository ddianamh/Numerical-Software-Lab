#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:58:36 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
Polynomial = np.polynomial.Polynomial

x1 = np.array([10,8,13,9,11,14,6,4,12,7,5])
y1 = np.array([8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68])
x2 = x1
y2 = np.array([9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74])
x3 = x1
y3 = np.array([7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73])

meanx = np.mean(x1)
meany1 = np.mean(y1)
meany2 = np.mean(y2)
meany3 = np.mean(y3)

varx = np.var(x1)
vary1 = np.var(y1)
vary2 = np.var(y2)
vary3 = np.var(y3)

xmin, xmax = min(x1), max(x1)
pfit1, stats1 = Polynomial.fit(x1, y1, 1, full = True, window=(xmin,xmax), domain=(xmin, xmax))
pfit2, stats2 = Polynomial.fit(x2, y2, 1, full = True, window=(xmin,xmax), domain=(xmin, xmax))
pfit3, stats3 = Polynomial.fit(x3, y3, 1, full = True, window=(xmin,xmax), domain=(xmin, xmax))

print("\nRaw fit results 1: ", pfit1, stats1, sep='\n')
print("\nRaw fit results 2: ", pfit2, stats2, sep='\n')
print("\nRaw fit results 3: ", pfit3, stats3, sep='\n')

y01, m1 = pfit1
resid1, rank1, sing_val1, rcond1 = stats1
rms1 = np.sqrt(resid1[0] / len(y1))

y02, m2 = pfit2
resid2, rank2, sing_val2, rcond2 = stats2
rms2 = np.sqrt(resid2[0] / len(y2))

y03, m3 = pfit3
resid3, rank3, sing_val3, rcond3 = stats3
rms3 = np.sqrt(resid3[0] / len(y3))

print("\n")
print( 'Fit 1: y1 = {:.3f}[P] + {:.3f}'.format(m1,y01),
      '(rms residual = {:.4f})'.format(rms1))

print("\n")
print( 'Fit 2: y2 = {:.3f}[P] + {:.3f}'.format(m2,y02),
      '(rms residual = {:.4f})'.format(rms2))

print("\n")
print( 'Fit 3: y3 = {:.3f}[P] + {:.3f}'.format(m3,y03),
      '(rms residual = {:.4f})'.format(rms3))

plt.plot(x1, y1, 'ko')
plt.plot(x1, pfit1(x1), 'k:')

plt.plot(x2, y2, 'b*')
plt.plot(x2, pfit2(x2),'b-.')

plt.plot(x3, y3, 'rs')
plt.plot(x3, pfit3(x3),'r--')

plt.show()






