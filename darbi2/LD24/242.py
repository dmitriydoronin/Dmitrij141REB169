# Autors: Dmitrijs Doronins
# Fails: 242.py

from Tkinter import *
import time

w = Tk(); f = Frame(); f.pack()

w.title('Pulkstenis')

time_var = StringVar()

time_labelis = Label(f, textvariable=time_var, font="Courier 60", bg= "black", fg="green")

time_labelis.pack()

def mirgot():
    """Funkcija datu atjaunossanai"""
    t=time.localtime(time.time())
    if t[6] %2:
        fmt = "%H:%M:%S"
    else:
        fmt ='%H %M %S'
        time_var.set(time.strftime(fmt, t))
        time_labelis.after(100, mirgot)

time_labelis.after(100, mirgot)

w.mainloop()
