# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 09:28:18 2019

@author: DIPAK
"""

from tkinter import *
import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

###for separator and all
def donothing():
    x = 0 ;

app = Tk()
app.title('Potential Flow Analysis')
app.geometry('1500x750')
part_label = Label(app, text = 'Part Name', font=('bold, 10'), pady = 30 )
part_label.grid(row = 0, column = 0, sticky = W)

##airfoil_label = Label(app, text ="Airfoil", font =('bold,10'), pady = 30).pack()
##airfoil_label.grid(row = 0, column = 0, sticky = W)

separator = Frame(height=2, bd=1, relief=SUNKEN)
#separator.pack(fill=X, padx=5, pady=5)

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0) #tearoff basically helps you detach the options from the main window
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save As", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Undo", command= donothing)
editmenu.add_command(label = "Redo", command= donothing)
editmenu.add_command(label = "Cut", command= donothing)
editmenu.add_command(label = "Copy", command= donothing)
editmenu.add_command(label = "Paste", command= donothing)
menubar.add_cascade(label = "Edit", menu = editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)
app.mainloop()

