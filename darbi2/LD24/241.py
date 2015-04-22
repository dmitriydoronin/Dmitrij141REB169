# -*- coding: utf-8 -*-
# Autors: Dmitrijs Doronins
# Fails: 241.py

from Tkinter import *

w = Tk()
w.title('Stundu saraksts')

uzr01 = Label(w,fg='blue', text='Lekc.Datormācības(speckurss)', font="ITALIC")
uzr01.place(x=0, y = 20 )

uzr02 = Label(w,fg='green', text='Lekc.ETP')
uzr02.place(x=0, y = 40 )

uzr03 = Label(w, fg='yellow',text='Lekc.Fizika', font="Courier 13 italic")
uzr03.place(x=0, y = 60 )

uzr04 = Label(w,fg='blue', text='Lab.Datormācību')
uzr04.place(x=0, y = 80 )

uzr05 = Label(w, text='Dmitrijs.Doronins')
uzr05.place(x=0, y = 120 )

uzr06 = Label(w, text='141REB169.REBCO4')
uzr06.place(x=0, y = 140 )

uzr07 = Label(w, text='RTU.ETF.2015')
uzr07.place(x=0, y = 160 )


w.geometry('300x200')
w.mainloop()

