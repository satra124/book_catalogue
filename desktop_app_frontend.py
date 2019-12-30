# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:38:17 2019

@author: esatrse
"""

from tkinter import *
import desktop_app_backend as dab


def view_all():
    list1.delete(0,END)
    for rows in dab.view():
        list1.insert(END, rows)

def search_entry():
    list1.delete(0,END)
    for rows in dab.search(title_text.get(),year_text.get(), author_text.get(), isbn_text.get()):
        list1.insert(END, rows)

def add_entry():
    list1.delete(0,END)
    dab.insert(title_text.get(),year_text.get(), author_text.get(), isbn_text.get())
    for rows in dab.search(title_text.get(),year_text.get(), author_text.get(), isbn_text.get()):
        list1.insert(END, rows)

def get_selected_row_id(event):
    index = list1.curselection()[0]
    selected_row = list1.get(index)
    return selected_row

def delete_entry():
    

window = Tk()
window.title("Book Dictionary")

l1 = Label(window, text='Title')
l1.grid(row=0,column=0)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

l2=Label(window, text='Author')
l2.grid(row=0,column=2)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

l3=Label(window, text='Year')
l3.grid(row=1,column=0)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

l4=Label(window, text='ISBN')
l4.grid(row=1,column=2)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height = 10, width = 35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row_id)

b1 = Button(window, text="View all", width=12, command=view_all)
b1.grid(row=2,column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_entry)
b2.grid(row=3,column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_entry)
b3.grid(row=4,column=3)

b4 = Button(window, text="Delete Entry", width=12, command=delete_entry)
b4.grid(row=5,column=3)

b5 = Button(window, text="Update Entry")
b5.grid(row=6,column=3)

b6 = Button(window, text="Close")
b6.grid(row=7,column=3)

window.mainloop()