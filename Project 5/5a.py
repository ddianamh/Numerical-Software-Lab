#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
#a) 1000 uniformly distributed random integers between 1 and 10
numbers = np.random.randint(0,10,1000)
#frequency list
ncount = np.zeros(10, dtype = int)
for i in numbers:
    ncount[i] = ncount[i] + 1
    
#making bar chart
#on x axis the numbers, on y axis their frequency
fig = plt.figure()
ax = fig.add_subplot(111)
x = range(10)
ax.bar(x, ncount, width = 0.8, color = 'g', align = 'center')
ax.set_xticks(x)
ax.set_xticklabels({1,2,3,4,5,6,7,8,9,10})
ax.tick_params(axis='x', direction='out')
ax.yaxis.grid(True)
ax.set_xlabel('Number')
ax.set_ylabel('Number frequency')
plt.show()