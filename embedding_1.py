# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:43:55 2019

@author: DIPAK
"""

import tkinter
import math
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import sourceSink


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

u_source, v_source = sourceSink.Source()
x_start, x_end = -2.0, 2.0 
y_start, y_end = -1.0 , 1.0
height= (y_end- y_start) /(x_end - x_start) * 10.0
X, Y = sourceSink.pos()
f = plt.streamplot(X,Y, u_source, v_source,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->')
canvas = FigureCanvasTkAgg(f, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
tkinter.mainloop()
