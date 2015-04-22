# Fails: 3 uzdevums ieskaite
# Autors: Dmitrijs Doronins

import Tkinter as tk

root=tk.Tk()
root.title("Formas")

w = tk.Canvas(root, width=300, height=300, bg="#234")
w.pack()

v = tk.StringVar()

e = tk.Entry(root,textvariable=v)
e.pack()



b = tk.Button(root, text="OK", command=fun)


def fun():
    print e.get


z = tk.OptionMenu(root, v, "prece1", "prece2", "prece3")





w.pack()

root.mainloop()
