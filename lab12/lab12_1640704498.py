import code
from tkinter import*
import sqlite3
from tkinter import ttk
from tkinter import messagebox

def dpinput() : 
    global conn
    global cursor
    conn = sqlite3.connect('lab12\week14_1640704498.db')
    cursor = conn.cursor()
    print("Connection Succesfully")

def mainwindow() :
    root = Tk()
    w = 1000
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.config(bg='#CD5C5C')
    root.title("Application: janjira  watcharawongsri ")
    root.option_add('*font',"tohoma 16 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def windowlogin(root) :
    global loginframe
    global username
    global pwd

    loginframe = Frame(root,bg='#FA8072')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    Label(loginframe,text="Account Login",font="Garamond 26 bold",image=img1,compound=TOP,bg='#FA8072',fg='#e4fbff').grid(row=0,columnspan=3)
    Label(loginframe,text="Username : ",bg='#FA8072',fg='#e4fbff',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff',width=20,textvariable=userr)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff',width=20,show='*',textvariable=pwdd)
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#FA8072',fg='#e4fbff',padx=20).grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,command=loginclick,bg='#EE82EE').grid(row=3,column=2,pady=20,ipady=15,padx=20)
   
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    Button(loginframe,text="Exit",width=10,command=quit).grid(row=3,column=0,pady=20,ipady=15,padx=20)

def loginclick() :
    global result
    sql2 = "SELECT * from students WHERE username=? and password=? "
    cursor.execute(sql2,[userr.get(),pwdd.get()])
    result = cursor.fetchone()
    if result :
        messagebox.showinfo("Admin :","Login Successfully")
        welcomepage(root)
    
    else :
        messagebox.showwarning("Admin : ","Username or Passowrd is invalid")

def welcomepage(root) :
    global codebox,namebox,daybox,roombox,mytree
    welcome = Frame(root,bg='#FFC0CB')
    welcome.rowconfigure((0,1,2,3,4,5,6),weight=2)
    welcome.columnconfigure((0,1,2,3,4,),weight=1)
    welcome.grid(row=0,column=0,rowspan=6,columnspan=5,sticky="nsew")
    Label(welcome,bg='#FFC0CB',image=img1,compound=LEFT).grid(row=0,columnspan=4)
    Label(welcome,text="Name :",bg='#FFC0CB').grid(row=1,column=0,sticky='e')
    Label(welcome,text=result[2]+' '+result[3],bg='#FFC0CB').grid(row=1,column=1,sticky='w')
    Label(welcome,text="ID :",bg='#FFC0CB').grid(row=2,column=0,sticky='e')
    Label(welcome,text=result[1],bg='#FFC0CB').grid(row=2,column=1,sticky='w')
    mytree = ttk.Treeview(welcome,columns=("col1","col2","col3","col4","col5"))
    mytree.grid(rowspan=1,columnspan=4,sticky="news")
    mytree.heading("col1",text="ID")
    mytree.heading("col2",text="Course Code")
    mytree.heading("col3",text="Cours Name")
    mytree.heading("col4",text="Day")
    mytree.heading("col5",text="Room")
    mytree.column("#0", width=0, stretch="no")
    mytree.column("col1", width=80, minwidth=1)
    mytree.column("col2", width=80, minwidth=1)
    mytree.column("col3", width=80, minwidth=1)
    mytree.column("col4", width=80, minwidth=1)
    mytree.column("col5", width=80, minwidth=1)

    sql = '''select * from course'''
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()

    for contact in data:
        mytree.insert('', END, values=contact)


    Label(welcome,text="Course Code : ",bg='#FA8072',fg='#e4fbff',padx=20).grid(row=4,column=0,sticky='nwse')
    Label(welcome,text="Course Name : ",bg='#FA8072',fg='#e4fbff',padx=20).grid(row=4,column=1,sticky='nwse')
    Label(welcome,text="day : ",bg='#FA8072',fg='#e4fbff',padx=20).grid(row=4,column=2,sticky='nwse')
    Label(welcome,text="Room : ",bg='#FA8072',fg='#e4fbff',padx=20).grid(row=4,column=3,sticky='nwse')
    codebox = Entry(welcome,bg="#d2e0ea",textvariable=codee)
    codebox.grid(row=5,column=0,sticky="nsew")
    namebox = Entry(welcome,bg="#d2e0ea",textvariable=namee)
    namebox.grid(row=5,column=1,sticky="nsew")
    daybox = Entry(welcome,bg="#d2e0ea",textvariable=dayy)
    daybox.grid(row=5,column=2,sticky="nsew")
    roombox = Entry(welcome,bg="#d2e0ea",textvariable=roomm)
    roombox.grid(row=5,column=3,sticky="nsew")
    Button(welcome,text="Add course",command=addcourse).grid(row=6,column=0)
    Button(welcome,text="Update record",command=update).grid(row=6,column=1)
    Button(welcome,text="Delete selected",command=delete).grid(row=6,column=2)
    Button(welcome,text="Clear",command=clear).grid(row=6,column=3)
    Button(welcome,text="Log out",command=lambda:windowlogin(root)).grid(row=7,column=0,columnspan=4)
    mytree.bind("<Double-1>",mytreeviewclick)

def mytreeviewclick(e) :
    global data
    data = mytree.item(mytree.focus(),'values')
    print("DATA",data)
    codebox['state'] = 'normal' 
    codebox.delete(0,END)
    namebox.delete(0,END)
    daybox.delete(0,END)
    roombox.delete(0,END)
    codebox.insert(0,data[1])
    namebox.insert(0,data[2])
    daybox.insert(0,data[3])
    roombox.insert(0,data[4])
    codebox['state'] = 'normal'

def addcourse() :
    if codebox.get() == "" :
        messagebox.showwarning("Admin :","Enter Coures Code first")
    elif namebox.get() == "" :
        messagebox.showwarning("Admin :","Enter Course Name first")
    elif daybox.get() == "" :
        messagebox.showwarning("Admin :","Enter Day first")
    elif roombox.get() == "" :
        messagebox.showwarning("Admin :","Enter Room first")
    else :
        sql = "insert into course values(NULL,?,?,?,?)"
        cursor.execute(sql,[codee.get(),namee.get(),dayy.get(),roomm.get()])
        conn.commit()
        messagebox.showinfo("Admin : ","Add Course Successfully")

def update() :
    if codebox.get() == "" :
        messagebox.showwarning("Admin :","Enter Coures Code first")
    elif namebox.get() == "" :
        messagebox.showwarning("Admin :","Enter Course Name first")
    elif daybox.get() == "" :
        messagebox.showwarning("Admin :","Enter Day first")
    elif roombox.get() == "" :
        messagebox.showwarning("Admin :","Enter Room first")
    else :
        sql = "update course set course_code = ?,course_name=?,day=?,room=? where id=?"
        cursor.execute(sql,[codee.get(),namee.get(),dayy.get(),roomm.get(),data[0]])
        conn.commit()
        messagebox.showinfo("Admin : ","Update Successfully")

def delete() :
    sql = '''delete from course where id=?'''
    cursor.execute(sql,[data[0]])
    conn.commit()
    messagebox.showinfo("Admin : ","Delete Successfully")

def clear() :
    codebox.delete(0,END)
    namebox.delete(0,END)
    daybox.delete(0,END)
    roombox.delete(0,END)

dpinput()
root = mainwindow()
img1= PhotoImage(file="lab12\profile_f.png").subsample(7,7)
userr,pwdd= StringVar(),StringVar()
codee,namee,dayy,roomm = StringVar(),StringVar(),StringVar(),StringVar()

windowlogin(root)

root.mainloop()
cursor.close()
conn.close()