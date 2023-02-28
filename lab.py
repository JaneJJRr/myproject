from tkinter import*
root = Tk() 
root.geometry("600x500")

root.rowconfigure((0),weight=1)
root.rowconfigure((1),weight=10)
root.rowconfigure((2),weight=1)
root.columnconfigure((0,1),weight=4)
top = Frame(root,bg="lightpink").grid(row=0,columnspan=2,sticky="news")
center1 = Frame(root,bg="lightblue").grid(rowspan=5,column=0,sticky="news")
center2 = Frame(root,bg="lightgreen").grid(row=1,column=1,sticky="news")
low = Frame(root,bg="lightpink").grid(row=2,columnspan=2,sticky="news")
#top
Label(root,text="MY CAKE SHOP",bg="lightpink").grid(row=0,columnspan=2)

#center1
cakevanilia = PhotoImage(file="/Users/faith/Desktop/cs311/week4/Lab/png/cake_vanilia.png").subsample(14,14)
cakestraw = PhotoImage(file="/Users/faith/Desktop/cs311/week4/Lab/png/chesscake_strawberry.png").subsample(14,14)
cakegreentea = PhotoImage(file="/Users/faith/Desktop/cs311/week4/Lab/png/cake_greentea.png").subsample(14,14)

img1 = Label(image=cakevanilia,bg="lightblue").place(x=15,y=95)
img2 = Label(image=cakestraw,bg="lightblue").place(x=15,y=200)
img3 = Label(image=cakegreentea,bg="lightblue").place(x=15,y=300)
menu = Label(root,text="MENU CAKE",bg="lightblue",font="verdana").place(y=75,x=100)

#center1 ลายละเอียดสินค้า


name1 = Label(root,text="Vanilia Cake",bg="lightblue",font="verdana").place(y=100,x=160)
Label(root,text="Price 400 Bahts",bg="lightblue",font="verdana").place(y=120,x=150)
box1 = Spinbox(root,width=10,from_=0,to=10)
box1.place(x=150,y=150)

neme2 = Label(root,text="Starwberry Chesscake",bg="lightblue",font="verdana").place(x=135,y=195)
Label(root,text="Price 600 Bahts",bg="lightblue",font="verdana").place(y=220,x=150)
box2 = Spinbox(root,width=10,from_=0,to=10)
box2.place(x=150,y=250)

name3 = Label(root,text="Matha Cake",bg="lightblue",font="verdana").place(x=160,y=300)
Label(root,text="Price 550 Bahts",bg="lightblue",font="verdana").place(y=320,x=150)
box3 = Spinbox(root,width=10,from_=0,to=10)
box3.place(x=150,y=350)

#check
def check() :
    total = 0
    cakeva = int(box1.get()) * 400
    cakestraw = int(box2.get()) * 600
    cakegreen = int(box3.get()) * 550
    total = cakeva+cakestraw+cakegreen

    et1 = StringVar()
    et1 = Entry(width=10)
    et1.insert(0,cakeva)
    et1.place(x=480,y=110)

    et2 = StringVar()
    et2 = Entry(width=10)
    et2.insert(0,cakestraw)
    et2.place(x=480,y=205)

    et3 = StringVar()
    et3 = Entry(width=10)
    et3.insert(0,cakegreen)
    et3.place(x=480,y=310)

    tt = StringVar()
    tt = Entry(width=10)
    tt.insert(0,total)
    tt.place(x=480,y=380)    
    

#ปุ่มchekout
Button(center1,text="Check Out",width=29,height=3,font="Verdana",command=check).place(y=400)

#center2

Label(center2,text="Checkout".upper(),bg="lightgreen",font="verdana").place(x=400,y=75)

Label(center2,text="Vanilia Cake",bg="lightgreen",font="verdana").place(x=345,y=100)
Label(center2,text="Price 400 Bahts",bg="lightgreen",font="verdana").place(x=335,y=120)


Label(center2,text="Starwberry Chesscake",bg="lightgreen",font="verdana").place(x=310,y=195)
Label(center2,text="Price 600 Bahts",bg="lightgreen",font="verdana").place(x=335,y=220)


Label(center2,text="Matha Cake",bg="lightgreen",font="verdana").place(x=345,y=300)
Label(center2,text="Price 550 Bahts",bg="lightgreen",font="verdana").place(x=335,y=320)



Label(center2,text="Total Price : ",bg="lightgreen",font="verdana").place(x=355,y=380)


#exit
exit = Button(low,width=20,height=2, text='Exit program', compound=LEFT, command=quit).place(x=380,y=460)
root.mainloop()