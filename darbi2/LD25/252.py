# Fails: 252.py
# Autors: Dmitrijs Doronins

from Tkinter import *

root= Tk()

root.title("Televizijas krasu tabula")

w = Canvas(root,width=800, height=450,bg="#FFF")

w.pack()

w.create_rectangle(0,0, 100, 450,fill="white")
w.create_rectangle(100,0, 200,450,fill="yellow")
w.create_rectangle(200,0, 300,450,fill="cyan")
w.create_rectangle(300,0, 400,450,fill="green")
w.create_rectangle(400,0, 500,450,fill="purple")
w.create_rectangle(500,0, 600,450,fill="red")
w.create_rectangle(600,0, 700,450,fill="blue")
w.create_polygon(700,0,700,451,800,451,800,0, fill="black")
                   

root.mainloop()
