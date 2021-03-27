from tkinter import *
from PIL import ImageTk,Image
import time

root = Tk()
root.title('Dictionary')
root.geometry('190x100')
root.resizable(False,False)

dic = {
    'apple':'Round fruit; green or red.'
}

def sc(word):
    if word in dic:
        newwin = Toplevel(root)
        newwin.geometry('190x67')
        newwin.title('Dict. > '+word)
        newwin.resizable(False, False)
        rep = Label(newwin, text=' ', font=('Arial', 1)).grid(row=0, column=0, padx=94)
        meaning = Label(newwin, text="Results for '"+word+"'",font=('Arial', 13)).grid(row=1, column=0)
        text = Label(newwin, text=dic.get(word),width=20, font=('Arial', 10)).grid(row=2, column=0,pady=5)
    return

toptext = Label(root, text='Type a word to search',font=('Arial',14)).grid(row=0,column=0, padx=5, pady=3)
search = Entry(root, width=20)
search.grid(row=1,column=0)
button = Button(root,text='Search', width=12, command=lambda: sc(search.get()) ).grid(row=2,column=0,pady=5)

root.mainloop()
