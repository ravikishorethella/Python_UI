from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint


# global variables
ActivePlayer = 1
p1=[] #what player 1 selects
p2=[]  #what player 2 selects

root = Tk()
style = ttk.Style()

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
    global ActivePlayer
    global p1
    global p2

    if (ActivePlayer==1):
        SetLayout(id, "X")
        p1.append(id)
        root.title("Tic Tac Toe: Player 2 ")
        ActivePlayer=2
        print("P1:{}".format(p1))
        AutoPlay()
    elif (ActivePlayer==2):
        SetLayout(id, "O")
        p2.append(id)
        root.title("Tic Tac Toe: Player 1 ")
        ActivePlayer=1
        print("P2:{}".format(p2))
    CheckWinner()

def SetLayout(id, PlayerSymbol):
    if id==1:
        bu1.config(text = PlayerSymbol)
        bu1.state(['disabled'])
    elif id==2:
        bu2.config(text=PlayerSymbol)
        bu2.state(['disabled'])
    elif id==3:
        bu3.config(text=PlayerSymbol)
        bu3.state(['disabled'])
    elif id == 4:
        bu4.config(text=PlayerSymbol)
        bu4.state(['disabled'])
    elif id == 5:
        bu5.config(text=PlayerSymbol)
        bu5.state(['disabled'])
    elif id == 6:
        bu6.config(text=PlayerSymbol)
        bu6.state(['disabled'])
    elif id == 7:
        bu7.config(text=PlayerSymbol)
        bu7.state(['disabled'])
    elif id == 8:
        bu8.config(text=PlayerSymbol)
        bu8.state(['disabled'])
    elif id == 9:
        bu9.config(text=PlayerSymbol)
        bu9.state(['disabled'])

def CheckWinner():
    Winner = -1
    if((1 in p1) and (2 in p1) and (3 in p1)):
        Winner = 1
    if((1 in p2) and (2 in p2) and (3 in p2)):
        Winner = 2
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        Winner = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Winner = 2
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        Winner = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        Winner = 2
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        Winner = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        Winner = 2
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        Winner = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        Winner = 2
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        Winner = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        Winner = 2
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        Winner = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        Winner = 2
    if ((3 in p1) and (5 in p1) and (7 in p1)):
        Winner = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        Winner = 2

    if Winner==1:
        messagebox.showinfo(title="Congrats", message="Player 1 is the winner")
    elif Winner==2:
        messagebox.showinfo(title="Congrats", message="Player 2 is the winner")

def AutoPlay():
    EmptyCells=[]
    for cell in range(9):
        if (not((cell+1 in p1) or (cell+1 in p2))):
            EmptyCells.append(cell+1)
    randIndex = randint(0,len(EmptyCells)-1)
    ButtonClick(EmptyCells[randIndex])



root.mainloop()
