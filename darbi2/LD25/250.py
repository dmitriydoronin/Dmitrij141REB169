# -*- coding: utf-8 -*-
# Fails: 250.py
# Autors: Dmitrijs Doronins

import Tkinter as tk

root = tk.Tk();
root.title("Mana tafele")

w = tk.Canvas(root, width=600, height=400,\
              bg="#465",relief="sunken", border=10 )

v = tk.StringVar()
v.set('Teksts uz tafeles')

e = tk.Entry(root,textvariable=v)
e.pack()

def fun():
    print e.get()

b = tk.Button(root, text="Spied", command=fun)
b.pack()
    
w.pack()
t = w.create_text(50, 100, text="2 + 2 = 4",\
                  font="Courier 40 italic",anchor='w', fill = "#ffc")

t2 = w.create_text(25, 75, text="Dmitrijs Doronins",\
                   font="Courier 40 italic",anchor= 'sw',fill = "#ffc")

w.mainloop()
