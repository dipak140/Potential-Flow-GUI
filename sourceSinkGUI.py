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

#Make the root widget
root = tkinter.Tk()
root.wm_title("Source Sink")
root.geometry('1500x850')

###importing values for source and sink
u_source, v_source = sourceSink.Source()
X, Y = sourceSink.pos()
u_sink, v_sink = sourceSink.Sink()
#######################################

#Make the notebook
nb = ttk.Notebook(root)
#Make 1st tab
f1 = tkinter.Frame(nb)
#Add the tab
nb.add(f1, text="                     Source                       ")
sourceStrength_label = Label(f1, text = 'Source Strength', font=('bold, 10'))
sourceStrength_label.grid(row = 1, column =0, sticky = W, pady = 30, padx =10)
sourceStrength_entry = Entry(f1, textvariable = DoubleVar())
sourceStrength_entry.grid(row = 1, column=1, sticky = W)
sourceStrength_button = tkinter.Button(master = f1, text = "Submit")
sourceStrength_button.grid(row = 1 , column = 2, sticky = W)

fig1 = Figure(figsize=(9,7), dpi=100)
fig1.add_subplot(111, xlabel = "X Axis", ylabel = "Y Axis").streamplot(X,Y, u_source, v_source,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->' )
#fig.add_subplot(111).scatter(0,0)
canvas = FigureCanvasTkAgg(fig1, master=f1)  # A tk.DrawingArea.
canvas.draw()
#canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.NONE, expand=0)
canvas.get_tk_widget().grid(row = 2, column = 3, sticky = S)


#Make 2nd tab
f2 = tkinter.Frame(nb)
#Add 2nd tab 
nb.add(f2, text="                     Sink                         ")
nb.select(f1)
nb.enable_traversal()
#nb.pack(expand = 1,  fill = tkinter.BOTH, side = tkinter.RIGHT)
nb.grid(row = 0 , column  = 0 , padx = 10)

sinkStrength_label = Label(f2, text = 'Sink Strength', font=('bold, 10'))
sinkStrength_label.grid(row = 1, column =0, sticky = W, pady = 30, padx =10)
sinkStrength_entry = Entry(f2, textvariable = DoubleVar())
sinkStrength_entry.grid(row = 1, column=1, sticky = W)
sinkStrength_button = tkinter.Button(master = f2, text = "Submit")
sinkStrength_button.grid(row = 1 , column = 2, sticky = W)

fig2 = Figure(figsize=(9,7), dpi=100)
fig2.add_subplot(111, xlabel = "X Axis", ylabel = "Y Axis").streamplot(X,Y, u_sink, v_sink,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->' )
#fig.add_subplot(111).scatter(0,0)
canvas = FigureCanvasTkAgg(fig2, master=f2)  # A tk.DrawingArea.
canvas.draw()
#canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.NONE, expand=0)
canvas.get_tk_widget().grid(row = 2, column = 3, sticky = S)

#Make 2nd tab
f3 = tkinter.Frame(nb)
#Add 2nd tab 
nb.add(f3, text="                     Source + Sink                         ")
nb.select(f3)
nb.enable_traversal()
#nb.pack(expand = 1,  fill = tkinter.BOTH, side = tkinter.RIGHT)
nb.grid(row = 0 , column  = 0 , padx = 10)

sinkStrength_label = Label(f3, text = 'Sink Strength', font=('bold, 10'))
sinkStrength_label.grid(row = 1, column =0, sticky = W, pady = 30, padx =10)
sinkStrength_entry = Entry(f3, textvariable = DoubleVar())
sinkStrength_entry.grid(row = 1, column=1, sticky = W)
sinkStrength_button = tkinter.Button(master = f3, text = "Submit")
sinkStrength_button.grid(row = 1 , column = 2, sticky = W)

fig3 = Figure(figsize=(9,7), dpi=100)
fig3.add_subplot(111, xlabel = "X Axis", ylabel = "Y Axis").streamplot(X,Y, u_source + u_sink, v_source + v_sink,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->' )
#fig.add_subplot(111).scatter(0,0)
canvas = FigureCanvasTkAgg(fig3, master=f3)  # A tk.DrawingArea.
canvas.draw()
#canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.NONE, expand=0)
canvas.get_tk_widget().grid(row = 2, column = 3, sticky = S)


#Enter the mainloop
root.mainloop()