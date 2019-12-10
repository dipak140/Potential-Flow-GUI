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
import sourceSink.py


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

u_source, v_source = sourceSink.source()

tkinter.mainloop()
