# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:44:25 2019

@author: DIPAK
"""
###MAtplotlib imbedding

from matplotlib.figure import figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkagg, NavigationToolbar2TkAgg

def matplotCanvas(self):
    f = Figure(figsize = (5,5), dpi = 100) #dpi?
    a = f.aff_subplot(111)
    a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])
    
    canvas = FigureCanvasTkAgg(f,self)
    canvas.show()
    canvas.get_tk_widget.pack(side = BOTTOM, fill = BOTH, expand = True)
    

