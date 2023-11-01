#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:22:17 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
t = np.sin(x) ** 2
u = np.cos(x) ** 2

fig = plt.figure(1, figsize = (9,8))
ax1 = fig.add_subplot(221)
ax1.plot(x, y, 'g-', label = 'sin(x)')
ax1.set_xlim( -np.pi, np.pi )
ax1.legend(loc = 'upper left')

ax2 = fig.add_subplot(222)
ax2.plot(x, z, 'k-', label = 'cos(x)')
ax2.set_xlim( -np.pi, np.pi )
ax2.legend(loc = 'upper left')

ax3 = fig.add_subplot(223)
ax3.plot(x, t, 'r-', label = 'sin(x)^2')
ax3.set_xlim( -np.pi, np.pi )
ax3.legend(loc = 'upper center')

ax4 = fig.add_subplot(224)
ax4.plot(x, y, 'b-', label = 'cos(x)^2')
ax4.set_xlim( -np.pi, np.pi )
ax4.legend(loc = 'upper left')

fig.tight_layout()
plt.show()
fig.savefig('Subplots_Trig.pdf')
