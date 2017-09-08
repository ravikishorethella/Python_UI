from tkinter import *
from tkinter import ttk

root = Tk()

frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height=200, width=200, relief=RIDGE, padding=(10,10))

ttk.Button(frame1, text="Click Me").grid(row=0, column=0)
ttk.Button(frame1, text="Click Me2").grid(row=0, column=3)

frame2 = ttk.Frame(root)
frame2.pack()
frame2.config(height=200, width=200, relief=RIDGE, padding=(10,10))
ttk.Button(frame2, text="Click Me").pack()
ttk.Button(frame2, text="Click Me").pack()

ttk.LabelFrame(height=100, width=100, text="Third frame").pack()
root.mainloop()