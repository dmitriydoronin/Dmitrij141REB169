# Fails: 251.py
# Autors: Dmitrijs Doronins

import Tkinter as tk

root= tk.Tk()

root.title("Mana Bilde")

w = tk.Canvas(root, width=600, height=400, bg="#abc")

w.pack()

linija = w.create_line(50,100,400,300,width='5',fill='#FF0')

root.mainloop()
