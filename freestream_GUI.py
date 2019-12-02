# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:04:29 2019

@author: DIPAK
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
import math
import numpy
from matplotlib import pyplot

f = Figure(figsize = (5,5), dpi =100)
a = f.add_subplot(111)

N = 50                                # number of points in each direction
x_start, x_end = -2.0, 2.0            # boundaries in the x-direction
y_start, y_end = -1.0, 1.0            # boundaries in the y-direction
x = numpy.linspace(x_start, x_end, N)    # creates a 1D-array with the x-coordinates
y = numpy.linspace(y_start, y_end, N)    # creates a 1D-array with the y-coordinates

X, Y = numpy.meshgrid(x, y)              # generates a mesh grid

# plot the grid of points
"""
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
pyplot.figure(figsize=(width, height))
pyplot.xlabel('x', fontsize=16)
pyplot.ylabel('y', fontsize=16)
pyplot.xlim(x_start, x_end)
pyplot.ylim(y_start, y_end)
pyplot.scatter(X, Y, s=5, color='#CD2305', marker='o')
"""
a.plot(X,Y)
canvas = FigureCanvasTkAgg(f)
canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)



