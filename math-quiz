from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title(' ')
root.resizable(FALSE,FALSE)
root.geometry('110x180')
title = Label(root, text='6-3*7?', font=('Arial',20)).pack(pady=5)
modes= [
    ("21",1),
    ("15",2),
    ("-15",3),
    ("4",4),
]

a = StringVar()
a.set(0)

def choice(val):
    if val == "3":
        messagebox.showinfo("result","correct!")
    else:
        messagebox.showerror("result","incorrect!")


for text, mode in modes:
    Radiobutton(root, text=text, variable=a, value=mode).pack(anchor=W)

# opt1 = Radiobutton(root, text='21', variable=z, value=1, command=lambda: choice(z.get())).pack(anchor=W)
# opt2 = Radiobutton(root, text='15', variable=z, value=2, command=lambda: choice(z.get())).pack(anchor=W)
# opt3 = Radiobutton(root, text='-15', variable=z, value=3, command=lambda: choice(z.get())).pack(anchor=W)
# opt4 = Radiobutton(root, text='4', variable=z, value=4, command=lambda: choice(z.get())).pack(anchor=W)

button = Button(root,text='submit',width=7,command=lambda: choice(a.get())).pack(pady=3)

mainloop()
