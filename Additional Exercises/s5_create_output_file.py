#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:34:20 2023

@author: dianah
"""

import numpy as np

f, a, da = np.loadtxt("s5_data.txt", skiprows = 0, unpack = True )

info = 'frequency (Hz)    amplitude (mm)    amp error (mm)'


np.savetxt("s5_out.txt", 
           list(zip(f, a, da)),
           fmt  = "%.3f %.1f %.1f",
           header = info )

np.savetxt("s5_out.csv", 
           list(zip(f, a, da)),
           fmt  = "%0.16e" )

