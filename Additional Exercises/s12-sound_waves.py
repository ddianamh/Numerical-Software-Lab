#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:36:24 2023

@author: dianah
"""

import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
rate, data = wav.read('bird.wav')
fft_out = fft(data[:,0])
plt.plot(data, np.abs(fft_out))
plt.show()
 