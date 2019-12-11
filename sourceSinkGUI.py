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


u_source, v_source = sourceSink.Source()
X, Y = sourceSink.pos()

root = tkinter.Tk()
root.wm_title("Potential Flow Solver")

fig = Figure(figsize=(10, 8), dpi=100)
fig.add_axes([0,0,4,5])
fig.add_subplot(111, xlabel = "X Axis", ylabel = "Y Axis").streamplot(X,Y, u_source, v_source,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->' )

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()
