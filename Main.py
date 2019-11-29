# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:36:25 2019

@author: DIPAK
"""

from tkinter import *
from db import Database

db = Database('store.db')
#create window object
def populate_list():
    parts_list.delete(0,END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    print('Add')

def remove_item():
    print('Remove')

def update_item():
    print('Update')
    
def clear_item():
    print('Clear')


app = Tk()
app.title('Part Manager')
app.geometry('800x450')


#part
part_text = StringVar()
part_label = Label(app, text = 'Part Name', font=('bold, 10'), pady = 30 )
part_label.grid(row = 0, column = 0, sticky = W)
part_entry = Entry(app, textvariable = part_text)
part_entry.grid(row = 0, column=1)

#customer
cust_text = StringVar()
cust_label = Label(app, text = 'Customer Name', font=('bold, 10'))
cust_label.grid(row = 0, column = 2, sticky = W)
cust_entry = Entry(app, textvariable = cust_text)
cust_entry.grid(row = 0, column=3)

#retail
retail_text = StringVar()
retail_label = Label(app, text = 'Retailer', font=('bold, 10'), pady = 30 )
retail_label.grid(row = 1, column = 0, sticky = W)
retail_entry = Entry(app, textvariable = retail_text)
retail_entry.grid(row = 1, column=1)

#price
price_text = StringVar()
price_label = Label(app, text = 'Price', font=('bold, 10'))
price_label.grid(row = 1, column = 2, sticky = W)
price_entry = Entry(app, textvariable = price_text)
price_entry.grid(row = 1, column=3)

###list box widget

parts_list = Listbox(app, height =6, width = 60)
parts_list.grid(row = 3, column=0, columnspan = 3, rowspan = 6, pady = 20, padx= 20)

##create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row =3, column = 3)

#set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command = parts_list.yview)

#buttons
add_btn = Button(app, text = 'Add part', width =12, command = add_item)
add_btn.grid(row =2, column = 0, pady = 20)

add_btn = Button(app, text = 'Remove part', width =12, command = remove_item)
add_btn.grid(row =2, column = 1, pady = 20)

add_btn = Button(app, text = 'Update part', width =12, command = update_item)
add_btn.grid(row =2, column = 2, pady = 20)

add_btn = Button(app, text = 'Clear part', width =12, command = clear_item)
add_btn.grid(row =2, column = 3, pady = 20)

populate_list()

#start program
app.mainloop()


