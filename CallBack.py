from tkinter import *
from tkinter import ttk

def BuClick(id):
    print("Id:{}".format(id))

root = Tk()

ttk.Button(root, text="Click Me!", command=lambda :BuClick(10)).pack()

root.mainloop()