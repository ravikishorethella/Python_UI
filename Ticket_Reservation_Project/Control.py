from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

ttk.Label(root, text="Full Name:").grid(row=0, column=0)
EntryFullName = ttk.Entry(root, width=30, font=('Arial',10))
EntryFullName.grid(row=0, column=1, columnspan=2)

SpanGender = StringVar()
SpanGender,set('Male')
ttk.Label(root, text="Gender:").grid(row=1, column=0)
ttk.Radiobutton(root, text='Male', variable=SpanGender, value="Male").grid(row=1, column=1)
ttk.Radiobutton(root, text='Female', variable=SpanGender, value="Female").grid(row=1, column=2)

TextComments = Text(root, width=30, height=10, font=('Arial',10))
TextComments.grid(row=3, column=1,columnspan=2)
ttk.Label(root, text="Comments:").grid(row=3, column=0)
ttk.Button(root, text="Submit").grid(row=4, column=3)


root.mainloop()
