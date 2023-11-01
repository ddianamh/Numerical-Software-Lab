#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:42:25 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt

t, y, dy = np.loadtxt("s6_data.txt", skiprows=0, unpack=True)

plt.figure(1, figsize = (9,8))
plt.plot(t, y, 'o')
plt.xlabel = 'time (s)'
plt.ylabel = 'position (cm)'