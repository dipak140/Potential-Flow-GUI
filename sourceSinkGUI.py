# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:43:55 2019

@author: DIPAK
"""

from tkinter import *
import tkinter
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
root.geometry('1500x850')
fig = Figure(figsize=(7,5), dpi=100)
fig.add_subplot(111, xlabel = "X Axis", ylabel = "Y Axis").streamplot(X,Y, u_source, v_source,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->' )
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
#canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.NONE, expand=0)
canvas.get_tk_widget().grid(row = 1, column = 10, sticky = E)

sourceStrength_label = Label(root, text = 'Source Strength', font=('bold, 10'))
sourceStrength_label.grid(row = 0, column =0, sticky = W, pady = 30, padx =10)
sourceStrength_entry = Entry(root, textvariable = DoubleVar())
sourceStrength_entry.grid(row = 0, column=1, sticky = W)
sourceStrength_button = tkinter.Button(master = root, text = "Submit")
sourceStrength_button.grid(row = 0 , column = 2, sticky = W)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.grid(row = 2, column = 2)
tkinter.mainloop()