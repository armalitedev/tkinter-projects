from tkinter import *
from tkinter import messagebox

root = Tk()
root.resizable(False, False)
root.title('TIC-TAC-TOE')

turnx = 0
turno = 0
used1=0
used2=0
used3=0
used4=0
used5=0
used6=0
used7=0
used8=0
used9=0

def grid(loc):
    global turnx
    global turno
    global used1
    global used2
    global used3
    global used4
    global used5
    global used6
    global used7
    global used8
    global used9
    if turnx == turno:
        if loc == 1 and used1==0:
            opt1.config(text='X')
            used1=1
            turnx+=1
            turn.config(text="O's turn")
        if loc == 2 and used2==0:
            opt2.config(text='X')
            used2 = 1
            turnx += 1
            turn.config(text="O's turn")
        if loc == 3 and used3==0:
            opt3.config(text='X')
            used3 = 1
            turnx += 1
            turn.config(text="O's turn")
        if loc == 4 and used4==0:
            opt4.config(text='X')
            used4 = 1
            turnx += 1
            turn.config(text="O's turn")
        if loc == 5 and used5==0:
            opt5.config(text='X')
            used5 = 1
            turnx += 1
            turn.config(text="O's turn")
        if loc == 6 and used6==0:
            opt6.config(text='X')
            used6 = 1
            turnx += 1
            turn.config(text="O's turn")
        if loc == 7 and used7==0:
            opt7.config(text='X')
            used7 = 1
            turnx += 1
            turn.config(text="O's turn")
        if loc == 8 and used8==0:
            opt8.config(text='X')
            used8 = 1
            turnx += 1
            turn.config(text="O's turn")
        if loc == 9 and used9==0:
            opt9.config(text='X')
            used9 = 1
            turnx += 1
            turn.config(text="O's turn")
    if turnx > turno:   #2
        if loc == 1 and used1==0:
            opt1.config(text='O')
            used1=1
            turno+=1
            turn.config(text="X's turn")
        if loc == 2 and used2==0:
            opt2.config(text='O')
            used2 = 1
            turno += 1
            turn.config(text="X's turn")
        if loc == 3 and used3==0:
            opt3.config(text='O')
            used3 = 1
            turno += 1
            turn.config(text="X's turn")
        if loc == 4 and used4==0:
            opt4.config(text='O')
            used4 = 1
            turno += 1
            turn.config(text="X's turn")
        if loc == 5 and used5==0:
            opt5.config(text='O')
            used5 = 1
            turno += 1
            turn.config(text="X's turn")
        if loc == 6 and used6==0:
            opt6.config(text='O')
            used6 = 1
            turno += 1
            turn.config(text="X's turn")
        if loc == 7 and used7==0:
            opt7.config(text='O')
            used7 = 1
            turno += 1
            turn.config(text="X's turn")
        if loc == 8 and used8==0:
            opt8.config(text='O')
            used8 = 1
            turno += 1
            turn.config(text="X's turn")
        if loc == 9 and used9==0:
            opt9.config(text='O')
            used9 = 1
            turno += 1
            turn.config(text="X's turn")
    if opt1['text']=='X' and opt2['text']=='X' and opt3['text']=='X':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results','X is the winner!')
        root.destroy()
    if opt1['text']=='O' and opt2['text']=='O' and opt3['text']=='O':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results', 'O is the winner!')
        root.destroy()
    if opt4['text']=='X' and opt5['text']=='X' and opt6['text']=='X':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results','X is the winner!')
        root.destroy()
    if opt4['text']=='O' and opt5['text']=='O' and opt6['text']=='O':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results', 'O is the winner!')
        root.destroy()
    if opt7['text']=='X' and opt8['text']=='X' and opt9['text']=='X':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results','X is the winner!')
        root.destroy()
    if opt7['text']=='O' and opt8['text']=='O' and opt9['text']=='O':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results', 'O is the winner!')
        root.destroy()
    if opt1['text']=='X' and opt4['text']=='X' and opt7['text']=='X':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results','X is the winner!')
        root.destroy()
    if opt1['text']=='O' and opt4['text']=='O' and opt7['text']=='O':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results', 'O is the winner!')
        root.destroy()
    if opt2['text']=='X' and opt5['text']=='X' and opt8['text']=='X':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results','X is the winner!')
        root.destroy()
    if opt2['text']=='O' and opt5['text']=='O' and opt8['text']=='O':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results', 'O is the winner!')
        root.destroy()
    if opt3['text']=='X' and opt6['text']=='X' and opt9['text']=='X':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results','X is the winner!')
        root.destroy()
    if opt3['text']=='O' and opt6['text']=='O' and opt9['text']=='O':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results', 'O is the winner!')
        root.destroy()
    if opt3['text']=='X' and opt5['text']=='X' and opt7['text']=='X':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results','X is the winner!')
        root.destroy()
    if opt3['text']=='O' and opt5['text']=='O' and opt7['text']=='O':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results', 'O is the winner!')
        root.destroy()
    if opt1['text']=='X' and opt5['text']=='X' and opt9['text']=='X':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results','X is the winner!')
        root.destroy()
    if opt1['text']=='O' and opt5['text']=='O' and opt9['text']=='O':
        turn.config(text="Game ended!")
        messagebox.showinfo('Game results', 'O is the winner!')
        root.destroy()


opt1 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(1))
opt1.grid(row=0, column=0, ipadx=20, ipady=20)
opt2 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(2))
opt2.grid(row=0, column=1, ipadx=20, ipady=20)
opt3 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(3))
opt3.grid(row=0, column=2, ipadx=20, ipady=20)
opt4 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(4))
opt4.grid(row=1, column=0, ipadx=20, ipady=20)
opt5 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(5))
opt5.grid(row=1, column=1, ipadx=20, ipady=20)
opt6 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(6))
opt6.grid(row=1, column=2, ipadx=20, ipady=20)
opt7 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(7))
opt7.grid(row=2, column=0, ipadx=20, ipady=20)
opt8 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(8))
opt8.grid(row=2, column=1, ipadx=20, ipady=20)
opt9 = Button(root, text='   ', font=('Arial', 40), command=lambda: grid(9))
opt9.grid(row=2, column=2, ipadx=20, ipady=20)
turn = Label(root, text="X's turn")
turn.grid(row=3, column=1)

root.mainloop()
