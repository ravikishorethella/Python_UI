from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

root.title("Tic Tac Toe: Player 1 ")

# Add Buttons

# Button 1
bu1 = ttk.Button(root, text=" ")
bu1.grid(row=0, column=0, sticky='snew', ipadx = 40, ipady = 40)
bu1.config(command=lambda: ButtonClick(1))

# Button 2
bu2 = ttk.Button(root, text=" ")
bu2.grid(row=0, column=1, sticky='snew', ipadx = 40, ipady = 40)
bu2.config(command=lambda: ButtonClick(2))

# Button 3
bu3 = ttk.Button(root, text=" ")
bu3.grid(row=0, column=2, sticky='snew', ipadx = 40, ipady = 40)
bu3.config(command=lambda: ButtonClick(3))

# Button 4
bu4 = ttk.Button(root, text=" ")
bu4.grid(row=1, column=0, sticky='snew', ipadx = 40, ipady = 40)
bu4.config(command=lambda: ButtonClick(4))

# Button 5
bu5 = ttk.Button(root, text=" ")
bu5.grid(row=1, column=1, sticky='snew', ipadx = 40, ipady = 40)
bu5.config(command=lambda: ButtonClick(5))

# Button 6
bu6 = ttk.Button(root, text=" ")
bu6.grid(row=1, column=2, sticky='snew', ipadx = 40, ipady = 40)
bu6.config(command=lambda: ButtonClick(6))

# Button 7
bu7 = ttk.Button(root, text=" ")
bu7.grid(row=2, column=0, sticky='snew', ipadx = 40, ipady = 40)
bu7.config(command=lambda: ButtonClick(7))

# Button 8
bu8 = ttk.Button(root, text=" ")
bu8.grid(row=2, column=1, sticky='snew', ipadx = 40, ipady = 40)
bu8.config(command=lambda: ButtonClick(8))

# Button 9
bu9 = ttk.Button(root, text=" ")
bu9.grid(row=2, column=2, sticky='snew', ipadx = 40, ipady = 40)
bu9.config(command=lambda: ButtonClick(9))


def ButtonClick(id):
    print("ID:{}".format(id))

root.mainloop()
