from msilib.schema import RadioButton
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

def createconnection() :
    conn = sqlite3.connect('D:\work\lab_11\infomation.db')
    cursor = conn.cursor()
    return conn,cursor

def mainwindow() :
    root = Tk()
    w = 800
    h = 600
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    root.config(bg='#CD5C5C')
    root.title("Application: janjira  watcharawongsri ")
    root.option_add('*font',"tohoma 16 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout() :
    global userentry,pwdentry
    userinfo = StringVar()
    pwdinfo = StringVar()
    loginframe = Frame(root,bg='#FA8072')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    
    Label(loginframe,text="Account Login",font="Garamond 26 bold",image=img2,compound=TOP,bg='#FA8072',fg='#e4fbff').grid(row=0,columnspan=3)
    Label(loginframe,text="Username : ",bg='#FA8072',fg='#e4fbff',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff',width=20,textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff',width=20,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#FA8072',fg='#e4fbff',padx=20).grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,command=lambda:loginclick(userinfo.get(),pwdinfo.get()),bg='#EE82EE').grid(row=3,column=2,pady=20,ipady=15,padx=20)
   
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    Button(loginframe,text="Exit",width=10,command=root.quit).grid(row=3,column=0,pady=20,ipady=15,padx=20)

def loginclick(user,pwd) :
    if user == "" :
        messagebox.showwarning("Admin:","Pleas enter username")
        userentry.focus_force()
    else :
        sql = "select * from login where user=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Admin:","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "select * from login where user=? and pwd=? "
                cursor.execute(sql,[user,pwd])   
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    print(result)
                    welcomepage(result)
                else :
                    messagebox.showwarning("Admin:","Incorrect Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login")
            userentry.select_range(0,END)
            userentry.focus_force()


            

def regislayout() :
    global fullname,lastname,newuser,newpwd,cfpwd,std,year,g
    var = IntVar()
    root.title("Welcome to User Registration : ")
    root.config(bg='lightblue')
    regisframe = Frame(root,bg='#FFC0CB')
    regisframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    Label(regisframe,text="Registration Form",font="tomaho 26 bold",fg='#e4fbff',image=img1,compound=LEFT,bg='#1687a7').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Label(regisframe,text='Student ID : ',bg='#FFC0CB',fg='#f6f5f5').grid(row=1,column=0,sticky='e',padx=10)
    std = Entry(regisframe,width=20,bg='#d3e0ea')
    std.grid(row=1,column=1,sticky='w',padx=10)
    
    Label(regisframe,text='Frist name : ',bg='#FFC0CB',fg='#f6f5f5').grid(row=2,column=0,sticky='e',padx=10)
    fullname = Entry(regisframe,width=20,bg='#d3e0ea')
    fullname.grid(row=2,column=1,sticky='w',padx=10)
    
    Label(regisframe,text='Last name : ',bg='#FFC0CB',fg='#f6f5f5').grid(row=3,column=0,sticky='e',padx=10)
    lastname = Entry(regisframe,width=20,bg='#d3e0ea')
    lastname.grid(row=3,column=1,sticky='w',padx=10)
    
    def viewSelected():
     global g
     choice  = var.get()
     if choice == 1:
       g = "Male"
     elif choice == 2:
       g =  "Female"   
     elif choice == 3:
       g =  "Other"
     return g  
    Label(regisframe,text='Gender : ',bg='#FFC0CB',fg='#f6f5f5').grid(row=4,column=0,sticky='e',padx=10)
    r1 = Radiobutton(regisframe,text='Male',bg='#FFC0CB',value=1,variable=var,command=viewSelected)
    r1.grid(row=4,column=1,sticky='w',padx=10)
    r2 = Radiobutton(regisframe,text='Female',bg='#FFC0CB',value=2,variable=var,command=viewSelected)
    r2.grid(row=5,column=1,sticky='w',padx=10)
    r3 = Radiobutton(regisframe,text='Other',bg='#FFC0CB',value=3,variable=var,command=viewSelected)
    r3.grid(row=6,column=1,sticky='w',padx=10)
    r1.focus_force()
    r2.focus_force()
    r3.focus_force()
    Label(regisframe,text='Year : ',bg='#FFC0CB',fg='#f6f5f5').grid(row=7,column=0,sticky='e',padx=10)
    year = Spinbox(regisframe,from_=1, to=4)
    year.grid(row=7,column=1,sticky='w',padx=10)
    year.focus_force()
    Label(regisframe,text="Username : ",bg='#FFC0CB',fg='#f6f5f5').grid(row=8,column=0,sticky='e',padx=10)
    newuser = Entry(regisframe,width=20,bg='#d3e0ea')
    newuser.grid(row=8,column=1,sticky='w',padx=10)
    Label(regisframe,text="Password : ",bg='#FFC0CB',fg='#f6f5f5').grid(row=9,column=0,sticky='e',padx=10)
    newpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    newpwd.grid(row=9,column=1,sticky='w',padx=10)
    Label(regisframe,text="Confirm Password : ",bg='#FFC0CB',fg='#f6f5f5').grid(row=10,column=0,sticky='e',padx=10)
    cfpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    cfpwd.grid(row=10,column=1,sticky='w',padx=10)
    regisaction = Button(regisframe,text="Register now",command=registration,bg='#FAFAD2')
    regisaction.grid(row=11,column=1,ipady=5,ipadx=5,pady=5,sticky='e')
    fullname.focus_force()
    loginbtn = Button(regisframe,text="Cancel",command=loginlayout)
    loginbtn.grid(row=11,column=0,ipady=5,ipadx=5,pady=5,sticky='w',padx=10)
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def registration() :
    if std.get() == "" :
        messagebox.showwarning("Admin: ","Please enter Student ID frist")
        std.focus_force()
    elif fullname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter firstname")
        fullname.focus_force()
    elif lastname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter lastname")
        lastname.focus_force()
    elif newuser.get() == "" :
        messagebox.showwarning("Admin: ","Please enter username")
        newuser.focus_force()
    elif newpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter password")
        newpwd.focus_force
    elif cfpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter confirm password")
        cfpwd
    else : 
        sql = "select * from Students where username = ?"
       
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchall() 
        if result :
            messagebox.showwarning("Admin:","The username is already exists")
            newuser.select_range(0,END)
            newuser.focus_force()
        else :
            if newpwd.get() == cfpwd.get() : 
                sql = "insert into Students values (?,?,?,?,?,?,?)" 
                param = [std.get(),fullname.get(),lastname.get(),g,year.get(),newuser.get(),newpwd.get()]
                cursor.execute(sql,param)
                conn.commit()
                messagebox.showinfo("Admin:","Registration Successfully")                
            else :  
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                cfpwd.select_range(0,END)
                cfpwd.focus_force


def welcomepage(result) :
    root.config(bg='lightblue')
    welcomeframe = Frame(root,bg='#FFC0CB')
    welcomeframe.rowconfigure((0,1,2,3,4,5,6),weight=2)
    welcomeframe.columnconfigure((0,1),weight=1)
    Label(welcomeframe,bg='#FFC0CB',image=img1,compound=LEFT).grid(row=0,columnspan=2)
    Label(welcomeframe,text="Name :",bg='#FFC0CB').grid(row=1,column=0,sticky='e')
    Label(welcomeframe,text=result[2]+' '+result[3],bg='#FFC0CB').grid(row=1,column=1,sticky='w')

    mytree = ttk.Treeview(welcomeframe,columns=("col1","col2","col3","col4","col5"))
    mytree.grid(rowspan=2,columnspan=3,sticky="news")
    mytree.heading("col1",text="Student ID")
    mytree.heading("col2",text="Firstname")
    mytree.heading("col3",text="Lastname")
    mytree.heading("col4",text="Gender")
    mytree.heading("col5",text="Year")
    mytree.column("#0", width=0, stretch="no")
    mytree.column("col1", width=80, minwidth=1)
    mytree.column("col2", width=80, minwidth=1)
    mytree.column("col3", width=80, minwidth=1)
    mytree.column("col4", width=120, minwidth=1)
    mytree.column("col5", width=80, minwidth=1)

    sql = "select * from Students"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()

    for contact in result:
        mytree.insert('', END, values=contact)



    Button(welcomeframe,text="Logout",width=10,height=1,command= welcomeframe.destroy).grid(row=6,columnspan=2,pady=10,padx=15)
    Button(welcomeframe,text="Add Student",width=10,command=regislayout,bg='#DB7093').grid(row=5,columnspan=2,pady=10,padx=15)
    welcomeframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')














conn,cursor = createconnection()
root = mainwindow()
img1 = PhotoImage(file='D:\CS311jane\week11\lab11\profile_f.png').subsample(7,7)
img2 = PhotoImage(file='D:\CS311jane\week11\lab11\profile_f.png').subsample(4,4)
loginlayout()
root.mainloop()
cursor.close()
conn.close()
