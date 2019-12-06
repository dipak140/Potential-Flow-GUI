# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:25:59 2019

@author: DIPAK
"""

import math   #math library
import numpy as np ## numerical python library
from matplotlib import pyplot as plt  ##plotting library

N = 50 #number of grid points
x_start, x_end = -2.0, 2.0 
y_start, y_end = -1.0 , 1.0 
x = np.linspace(x_start, x_end, N)   ##numbers generated beweeen -2 and 2
y = np.linspace(y_start, y_end, N)

print('x= ', x)
print('y= ', y)

X , Y = np.meshgrid(x, y)   #creates 50X50 grid for both x and y


source_strength = 5.0
x_source, y_source = 0.0,0.0

u_source = source_strength/(2 * math.pi) * (X - x_source)/((X - x_source)**2 + (Y - y_source)**2)
v_source = source_strength/(2 * math.pi) * (Y - y_source)/((X - x_source)**2 + (Y - y_source)**2)

width = 10.0
height= (y_end- y_start) /(x_end - x_start) * width
plt.figure(figsize =(width, height))
plt.xlabel('x', fontsize = 16)
plt.ylabel('y', fontsize = 16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.streamplot(X,Y, u_source, v_source,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->')
plt.scatter(x_source, y_source, s= 20 , color = '#CD2305',marker = 'o')
plt.show()

