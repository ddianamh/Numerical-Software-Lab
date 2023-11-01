#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 00:14:36 2023

@author: dianah
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def plot_creation(file_name, plot_title = "Input data", x_axis = "x axis", y_axis = "y axis"):
    x, y = np.loadtxt(file_name, skiprows=0, unpack=True)
    #max and min for both sequences
    maxx = np.max(x)
    maxy = np.max(y)
    minx = np.min(x)
    miny = np.min(y)
    
    #calculating the range of data for x and y
    rx = maxx - minx
    ry = maxy - miny
    
    # creating the plot
    plt.figure(1, figsize = (6,6) )
    plt.plot(x, y, 'r.')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(plot_title)
    #setting the margins
    plt.axis( [minx - 0.05*rx, maxx + 0.05*rx, miny - 0.05*ry, maxy + 0.05*ry])
    
    # save plot to file
    plt.savefig('InputData.pdf')
    
    #exporting data into a csv file
    #changing ending of the data file from the input data file
    #using Path from pathlib
    csv_file_name = Path(file_name).stem + ".csv"
    np.savetxt(csv_file_name, list(zip(x, y)), fmt  = "%0.1f" )
    
    #returning the output (the sequences)
    return x, y

#testing the function 
plot_creation("test_data2.dat")