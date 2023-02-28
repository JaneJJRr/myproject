from tkinter import *
from tkinter.tix import WINDOW
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()

dic_images = [
    'lab3\png1lab.png',
    'lab3\png2lab.png',
    'lab3\png3lab.png',
    'lab3\png4lab.png'
    ]


def widgettop(window) : 
    label_1 = Label(window,text='Takeout Order From',fg='black',font=('Tahoma', 16, 'bold'),bg='#FFBC80')
    label_1.grid(row=0,columnspan=2)


O_img1 = Image.open('lab3\png1lab.png').resize((150,150),Image.ANTIALIAS)
icon1 = ImageTk.PhotoImage(O_img1)
O_img2 = Image.open('lab3\png2lab.png').resize((150,150),Image.ANTIALIAS)
icon2 = ImageTk.PhotoImage(O_img2)
O_img3 = Image.open('lab3\png3lab.png').resize((150,150),Image.ANTIALIAS)
icon3 = ImageTk.PhotoImage(O_img3)
O_img4 = Image.open('lab3\png4lab.png').resize((150,150),Image.ANTIALIAS)
icon4 = ImageTk.PhotoImage(O_img4)


def widgetleft() :

    f_b1 = Button(window, image = icon1, compound=TOP, text='condogb', bg='#F6EAE3', height=200, width=200,command=corndog)
    f_b2 = Button(window, image = icon2, compound=TOP, text='fried ckiken', bg='#F6EAE3', height=200, width=200,command=chicken)
    f_b3 = Button(window, image = icon3, compound=TOP, text='rown sauce with rice', bg='#F6EAE3', height=200, width=200,command=ckrice)
    f_b4 = Button(window, image = icon4, compound=TOP, text='Garlic Beef with Rice', bg='#F6EAE3', height=200, width=200,command=Beef)
    f_b1.grid(row=2, column=0)
    f_b2.grid(row=2, column=1)
    f_b3.grid(row=3, column=0)
    f_b4.grid(row=3, column=1)



def corndog() :
    messagebox.showinfo("food Inspection:","You want to choose corndog?")
def chicken() :
    messagebox.showinfo("food Inspection:","You want to choose fried chicken ?")
def ckrice() :
    messagebox.showinfo("food Inspection:","You want to choose Chicken in brown sauce with rice?")
def Beef() :
    messagebox.showinfo("food Inspection:","You want to choose Garlic Beef with Rice?")

widgettop(window)
widgetleft()
window.mainloop()