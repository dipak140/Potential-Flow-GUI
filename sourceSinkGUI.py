# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:43:55 2019
@author: DIPAK
"""
from tkinter import *
from tkinter import ttk
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
sourceStrength_button.grid(row = 1 , column = 2, sticky = W, padx =10)

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
#nb.pack(expand = 1,  fill = tkinter.BOTH, side = tkinter.RIGHT)
nb.grid(row = 0 , column  = 0 , padx = 10)

sinkStrength_label = Label(f2, text = 'Sink Strength', font=('bold, 10'))
sinkStrength_label.grid(row = 1, column =0, sticky = W, pady = 30, padx =10)
sinkStrength_entry = Entry(f2, textvariable = DoubleVar())
sinkStrength_entry.grid(row = 1, column=1, sticky = W)
sinkStrength_button = tkinter.Button(master = f2, text = "Submit")
sinkStrength_button.grid(row = 1 , column = 2, sticky = W, padx =10)

fig2 = Figure(figsize=(9,7), dpi=100)
fig2.add_subplot(111, xlabel = "X Axis", ylabel = "Y Axis").streamplot(X,Y, u_sink, v_sink,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->' )
#fig.add_subplot(111).scatter(0,0)
canvas = FigureCanvasTkAgg(fig2, master=f2)  # A tk.DrawingArea.
canvas.draw()
#canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.NONE, expand=0)
canvas.get_tk_widget().grid(row = 2, column = 3, sticky = S)

#Make 3rd tab
f3 = tkinter.Frame(nb)
#Add 3rd tab 
nb.add(f3, text="                     Source + Sink                         ")
#nb.pack(expand = 1,  fill = tkinter.BOTH, side = tkinter.RIGHT)
nb.grid(row = 0 , column  = 0 , padx = 10)

sourceStrength_label = Label(f3, text = 'Source Strength', font=('bold, 10'))
sourceStrength_label.grid(row = 1, column =0, sticky = W, pady = 20, padx =10)
sourceStrength_entry = Entry(f3, textvariable = DoubleVar())
sourceStrength_entry.grid(row = 1, column=1, sticky = W)
sourceStrength_button = tkinter.Button(master = f3, text = "Submit")
sourceStrength_button.grid(row = 1 , column = 2, sticky = W, padx =10)


sinkStrength_label = Label(f3, text = 'Sink Strength', font=('bold, 10'))
sinkStrength_label.grid(row = 2, column =0, sticky = W, pady = 20, padx =10)
sinkStrength_entry = Entry(f3, textvariable = DoubleVar())
sinkStrength_entry.grid(row = 2, column=1, sticky = W)
sinkStrength_button = tkinter.Button(master = f3, text = "Submit")
sinkStrength_button.grid(row = 2 , column = 2, sticky = W, padx =10)


fig3 = Figure(figsize=(9,7), dpi=100)
fig3.add_subplot(111, xlabel = "X Axis", ylabel = "Y Axis").streamplot(X,Y, u_source + u_sink, v_source + v_sink,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->' )
#fig.add_subplot(111).scatter(0,0)
canvas = FigureCanvasTkAgg(fig3, master=f3)  # A tk.DrawingArea.
canvas.draw()
#canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.NONE, expand=0)
canvas.get_tk_widget().grid(row = 3, column = 3, sticky = S)



###############################4th Tab########################################
#Make 4th tab
f4 = tkinter.Frame(nb)
#Add 4th tab 
nb.add(f4, text="                     Source + Freestream                         ")
#nb.pack(expand = 1,  fill = tkinter.BOTH, side = tkinter.RIGHT)
nb.grid(row = 0 , column  = 0 , padx = 10)
N = 50
u_inf = 1.0        # freestream speed
# compute the freestream velocity field
u_freestream = u_inf * np.ones((N, N), dtype=float)
v_freestream = np.zeros((N, N), dtype=float)

# compute the stream-function
psi_freestream = u_inf * Y
psi_source = sourceSink.streamFunction(5.0, 0.0, 0.0, X, Y)

u_SF = u_freestream + u_source
v_SF = v_freestream + v_source

freestream_label = Label(f4, text = 'Freestream Velocity', font=('bold, 10'))
freestream_label.grid(row = 1, column =0, sticky = W, pady = 10, padx =10)
freestream_entry = Entry(f4, textvariable = DoubleVar())
freestream_entry.grid(row = 1, column=1, sticky = W)
freestream_button = tkinter.Button(master = f4, text = "Submit")
freestream_button.grid(row = 1 , column = 2, sticky = W, padx =10)

sourceStrength_label = Label(f4, text = 'Source Strength', font=('bold, 10'))
sourceStrength_label.grid(row = 2, column =0, sticky = W, pady = 10, padx =10)
sourceStrength_entry = Entry(f4, textvariable = DoubleVar())
sourceStrength_entry.grid(row = 2, column=1, sticky = W)
sourceStrength_button = tkinter.Button(master = f4, text = "Submit")
sourceStrength_button.grid(row = 2 , column = 2, sticky = W, padx =10)

sinkStrength_label = Label(f4, text = 'Sink Strength', font=('bold, 10'))
sinkStrength_label.grid(row = 3, column =0, sticky = W, pady = 10, padx =10)
sinkStrength_entry = Entry(f4, textvariable = DoubleVar())
sinkStrength_entry.grid(row = 3, column=1, sticky = W)
sinkStrength_button = tkinter.Button(master = f4, text = "Submit")
sinkStrength_button.grid(row = 3 , column = 2, sticky = W, padx =10)

fig4 = Figure(figsize=(9,7), dpi=100)
fig4.add_subplot(111, xlabel = "X Axis", ylabel = "Y Axis").streamplot(X,Y, u_SF, v_SF,  density = 2,  linewidth = 1,  arrowsize = 2,  arrowstyle = '->' )
#fig.add_subplot(111).scatter(0,0)
canvas = FigureCanvasTkAgg(fig4, master=f4)  # A tk.DrawingArea.
canvas.draw()
#canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.NONE, expand=0)
canvas.get_tk_widget().grid(row = 4, column = 3, sticky = S)

###############################################################################
nb.select(f1)
nb.enable_traversal()
#Enter the mainloop
root.mainloop()