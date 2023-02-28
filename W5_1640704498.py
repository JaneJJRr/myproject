from tkinter import *

def mainwindow() :
    root = Tk()
    root.title("GUI4: Class Activity of Week4")
    root.geometry("600x650")
    root.configure(bg='lightgreen')
    root.rowconfigure((0,2),weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=4)
    return(root)

def createframe(root) :
    # top = Frame(root,bg='#694E4E')
    # top.rowconfigure(0,weight=1)
    # top.columnconfigure((0,1),weight=1)
    left = Frame(root,bg='#F3C5C5')
    left.rowconfigure((0,1,2),weight=1)
    left.columnconfigure(0,weight=1)
    right = Frame(root,bg='#886F6F')
    right.rowconfigure((0,1,2),weight=1)
    right.columnconfigure(0,weight=1)
    bottom = Frame(root,bg='#694E4E')
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure(0,weight=1)
    left.grid(row=1,column=0,sticky='news')
    right.grid(row=1,column=1,sticky='news')
    bottom.grid(row=3,columnspan=2,sticky='news')
    return(root,left,right,bottom)



def widgetleft(left) :
    tag1 = Label(left,image=img1,bg='#F3C5C5')
    tag1.grid(row=0)
    tag2 = Label(left,image=img2,bg='#F3C5C5')
    tag2.grid(row=1)
    tag3 = Label(left,image=img3,bg='#F3C5C5')
    tag3.grid(row=2,)
    tag4 = Label(left,image=img4,bg='#F3C5C5')
    tag4.grid(row=3)
    tag5 = Label(left,image=img5,bg='#F3C5C5')
    tag5.grid(row=4)
    tag6 = Label(left,image=img5,bg='#F3C5C5')
    tag6.grid(row=5)

def widgetright(right) :
    click1 = Checkbutton(right, variable=v1, command=fnclick, text="Address book1: 100 bahts",bg='#694E4E',fg='#BF9270')
    click1.grid(row=0,sticky='n',padx=20,ipadx=30,pady=20)
    click2 = Checkbutton(right,variable=v2, command=fnclick, text="Address book2: 250 bahts",bg='#694E4E',fg='#EDCDBB')
    click2.grid(row=1,sticky='n',padx=20,ipadx=30)
    click3 = Checkbutton(right, variable=v3, command=fnclick, text="Address book3: 150 bahts",bg='#694E4E',fg='#E3B7A0')
    click3.grid(row=2,sticky='n',padx=20,ipadx=30)
    click4 = Checkbutton(right, variable=v4, command=fnclick, text="Address book3: 300 bahts",bg='#694E4E',fg='#E3B7A0')
    click4.grid(row=3,sticky='n',padx=20,ipadx=30,pady=30)
    click5 = Checkbutton(right, variable=v5, command=fnclick, text="Address book3: 200 bahts",bg='#694E4E',fg='#E3B7A0')
    click5.grid(row=4,sticky='n',padx=20,ipadx=30,pady=50)
    click6 = Checkbutton(right, variable=v6, command=fnclick, text="Address book3: 400 bahts",bg='#694E4E',fg='#E3B7A0')
    click6.grid(row=5,sticky='n',padx=20,ipadx=30,pady=30)
def widgetbottom(bottom) :
    showtotal = Label(bottom,textvariable=output,bg='#694E4E',font=("Helvetica", "16","bold"))
    showtotal.grid(ipady=10,pady=5)
    return(showtotal)

def fnclick() :
    global net
    net = 0
    if v1.get() :
        net = net + 100
    if v2.get() :
        net += 250
    if v3.get() :
        net = net +150
    if v4.get() :
        net = net +300
    if v5.get() :
        net = net +200
    if v6.get() :
        net = net +400   
    #print("Total amount = %0.2f"%net)
    showtotal["bg"] = "#F3C5C5"
    showtotal["fg"] = "#C1A3A3"
    output.set("Total Amount = %0.2f"%net)

root = mainwindow()
net = 0
v1,v2,v3,v4,v5,v6 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
output = StringVar()

img1 = PhotoImage(file='image/book1_1.png')
img2 = PhotoImage(file='image/book3.png')
img3 = PhotoImage(file="image/book1.png")
img4 = PhotoImage(file="image/book2.png")
img5 = PhotoImage(file="image/book3.png")
img6 = PhotoImage(file="image/book1_1.png")
root,left,right,bottom = createframe(root)

widgetleft(left)
widgetright(right)
showtotal = widgetbottom(bottom)
root.mainloop()