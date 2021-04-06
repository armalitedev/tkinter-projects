from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.title('Color game')
root.geometry('200x140')
root.resizable(False,False)

colto = {
    1:"White",
    2:"Black",
    3:"Red",
    4:"Green",
    5:"Blue",
    6:"Cyan",
    7:"Yellow",
    8:"Magenta"
}

wordto = {
    1:"Test",
    2:"Word",
    3:"AAAA",
    4:"BBBB"
}

tot=0
word=0
color=0
livecount=4
pointscount=0
new=False

def start(typed):
    global tot
    global pointscount
    global livecount
    global color
    global word
    global new
    entry.config(state='normal')
    submit.config(text='Submit')
    if color==typed:
        tot+=1
        pointscount+=1
    else:
        livecount-=1
    if pointscount==3:
        livecount+=1
        pointscount-=3
    if livecount==0:
        end=messagebox.askquestion('Game end!','You lost with '+str(tot)+' points in total! Do you want to replay?')
        if end=='yes':
            entry.config(state='disabled')
            submit.config(text='Start')
            tot = 0
            word = 0
            color = 0
            livecount = 3
            pointscount = 0
            new=True
        else:
            root.destroy()
    word=wordto[int(random.uniform(1,5))]
    color=colto[int(random.uniform(1,9))]
    maincolor.config(text=word,fg=color)
    entry.delete(0,END)
    points.config(text=str(pointscount)+' points')
    lives.config(text=str(livecount)+' lives left')
    if new==True:
        livecount+=1
        new=False

maincolor= Label(root,text='color',font=('Arial',20))
maincolor.place(x=70,y=3)
entry=Entry(root,state='disabled')
entry.place(x=18,y=40)
submit=Button(root,text='Start',command=lambda:start(entry.get()))
submit.place(x=65,y=74)
points= Label(root,text='0 points',bg="Green")
points.place(x=0,y=120)
lives= Label(root,text='3 lives left',bg="Red")
lives.place(x=127,y=120)


root.mainloop()
