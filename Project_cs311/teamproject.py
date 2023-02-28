from cProfile import label
from msilib.schema import RadioButton
import sqlite3
from tkinter import font, messagebox
from tkinter import *
from tkinter import ttk
from sympy import expand

def createconnection() :
    conn = sqlite3.connect('Project_cs311\DB_team.db')
    cursor = conn.cursor()
    return conn,cursor

def mainwindow() :
    root = Tk()
    
    root.geometry('650x780')
    root.config(bg='white')
    root.title("Application : Elfin ")
    root.option_add('*font',"CurierNew 18")
    root.rowconfigure((1),weight=3)
    root.rowconfigure((0,2),weight=1)
    root.columnconfigure((0),weight=1)
    return root

def loginlayout() :
    global userentry,pwdentry
    userinfo = StringVar() 
    pwdinfo = StringVar()
    loginframe = Frame(root,bg='white')
    loginframe.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    loginframe.columnconfigure((0,1,2),weight=1)
    
    Label(loginframe,text="Login",font="tamaho 33 bold",compound=TOP,bg='white',fg='blue').grid(row=0,columnspan=3)
    Label(loginframe,text="Username",bg='white',fg='black',padx=7,font="tamaho 22").grid(row=1,column=0)
    Label(loginframe,image=ent,bg='white').grid(row=2,column=0,columnspan=3)
    userentry = Entry(loginframe,bg='white',width=30,textvariable=userinfo,borderwidth=0,font="tamaho 20")
    userentry.grid(row=2,column=0,columnspan=3)
    Label(loginframe,text="Password",bg='white',fg='black',padx=7,font="tamaho 22").grid(row=3,column=0)
    Label(loginframe,image=ent,bg='white').grid(row=4,column=0,columnspan=3)
    pwdentry = Entry(loginframe,bg='white',width=30,show='*',textvariable=pwdinfo,borderwidth=0,font="tamaho 20")
    pwdentry.grid(row=4,column=0,columnspan=3)
    Radiobutton(loginframe,text="Remember me",bg='white',fg='black',padx=20,value=1,font="CurierNew 14").grid(row=5,column=0,sticky='w')
    Label(loginframe,text="Forgot password",bg='white',fg='blue',padx=20,font="CurierNew 14").grid(row=5,column=2,sticky='e')
    Button(loginframe,image=lg,command=lambda:loginclick(userinfo.get(),pwdinfo.get()),bg='white',borderwidth=0).grid(row=6,columnspan=3)
    Button(loginframe,image=rg,command=regislayout,bg='white',borderwidth=0).grid(row=7,columnspan=3,sticky=N)
    loginframe.grid(row=0,column=0,rowspan=3,sticky='news')

def menubar() :
    menuframe = Frame(root,bg='#FF6464')
    menuframe.columnconfigure((0,1,2,3,4),weight=1)
    menuframe.rowconfigure((0),weight=1)
    Button(menuframe,borderwidth=0,fg='white',text="home",compound="top",bg='#FF6464',width=80,height=80,image=img6,font="tomaho 10",command=lambda:welcomepage(result)).grid(row=0,column=0,sticky='NEWS')
    Button(menuframe,borderwidth=0,fg='white',text="Portfolio",compound="top",bg='#FF6464',width=80,height=80,image=img7,font="tomaho 10",command=portfolio).grid(row=0,column=1,sticky='NEWS')
    Button(menuframe,borderwidth=0,fg='white',text="news",compound="top",bg='#FF6464',width=80,height=80,image=img8,font="tomaho 10",command=lambda:newspage()).grid(row=0,column=2,sticky='NEWS')
    Button(menuframe,borderwidth=0,fg='white',text="market",compound="top",bg='#FF6464',width=80,height=80,image=img9,font="tomaho 10",command=market).grid(row=0,column=3,sticky='NEWS')
    Button(menuframe,borderwidth=0,fg='white',text="profile",compound="top",bg='#FF6464',width=80,height=80,image=img10,font="tomaho 10",command=profilee).grid(row=0,column=4,sticky='NEWS')
    menuframe.grid(row=2,column=0,sticky='news')

def loginclick(user,pwd) :
    global result
    if user == "" :
        messagebox.showwarning("Admin:","Pleas enter username")
        userentry.focus_force()
    else :
        sql = "select * from Students where email=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Admin:","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "select * from Students where email=? and password=? "
                cursor.execute(sql,[user,pwd])   
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    welcomepage(result)
                    menubar()
                    
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
    root.config(bg='white')
    regisframe = Frame(root,bg='white')
    regisframe.rowconfigure((0,1,2,3,4,5,6,7),weight=0)
    regisframe.columnconfigure((0,1,2),weight=1)
    Label(regisframe,text="  Registration Form",font="tomaho 26 bold",fg='#0063F5',bg='white',compound=LEFT).grid(row=0,column=0,columnspan=2,pady=10,sticky=NW) #ลบรูปภาพออก,image=img1
    Label(regisframe,text='Name : ',font="tomaho 14",fg='black',bg='white').grid(row=1,column=0,sticky=W,padx=16,pady=4)
    Label(regisframe,image=ent1,bg='white').grid(row=2,columnspan=3)
    fullname = Entry(regisframe,width=20,bg='white',borderwidth=0,font="tomaho 15") #ช่องกรอกชื่อ
    fullname.place(x=40,y=118)
    

    Label(regisframe,text='Surname : ',font="tomaho 14",bg='white',fg='black').grid(row=3,column=0,sticky=W,padx=16,pady=4)
    Label(regisframe,image=ent1,bg='white').grid(row=4,columnspan=3)
    lastname = Entry(regisframe,width=20,bg='white',borderwidth=0,font="tomaho 15") #นามสกุล
    lastname.place(x=40,y=208)
    

    Label(regisframe,text='ID card : ',font="tomaho 14",bg='white',fg='black').grid(row=5,column=0,sticky=W,padx=16,pady=4)
    Label(regisframe,image=ent1,bg='white').grid(row=6,columnspan=3)
    std = Entry(regisframe,width=20,bg='white',borderwidth=0,font="tomaho 15") #ช่องกรอกไอดี
    std.place(x=40,y=298)
 
   
    Label(regisframe,text='Phone number : ',font="tomaho 14",bg='white',fg='black').grid(row=9,column=0,sticky=W,padx=16,pady=4)
    Label(regisframe,image=ent1,bg='white').grid(row=10,columnspan=3)
    year = Entry(regisframe,width=20,bg='white',borderwidth=0,font="tomaho 15")
    year.place(x=40,y=388)
    

    Label(regisframe,text="Email : ",font="tomaho 14",bg='white',fg='black').grid(row=11,column=0,sticky=W,padx=16,pady=4)
    Label(regisframe,image=ent1,bg='white').grid(row=12,columnspan=3)
    newuser = Entry(regisframe,width=20,bg='white',borderwidth=0,font="tomaho 15")#,font="tomaho 13"
    newuser.place(x=40,y=478)
    

    Label(regisframe,text="Password : ",font="tomaho 14",bg='white',fg='black').grid(row=13,column=0,sticky=W,padx=16,pady=4)
    Label(regisframe,image=ent1,bg='white').grid(row=14,columnspan=3)
    newpwd = Entry(regisframe,width=20,bg='white',show='*',borderwidth=0,font="tomaho 15")
    newpwd.place(x=40,y=568)
    

    Label(regisframe,text="Confirm Password : ",font="tomaho 14",bg='white',fg='black').grid(row=15,column=0,sticky=W,padx=16,pady=4)
    Label(regisframe,image=ent1,bg='white').grid(row=16,columnspan=3)
    cfpwd = Entry(regisframe,width=20,bg='white',show='*',borderwidth=0,font="tomaho 10")
    cfpwd.place(x=40,y=658)
    
    
    regisaction = Button(regisframe,image=rn,command=registration,bg='white',borderwidth=0)
    regisaction.grid(row=17,column=1,ipady=5,ipadx=5,pady=5,sticky='e')
    fullname.focus_force()
    loginbtn = Button(regisframe,image=cancel,command=loginlayout,borderwidth=0,bg='white')
    loginbtn.grid(row=17,column=0,ipady=5,ipadx=5,pady=5,sticky='w',padx=10)
    regisframe.grid(row=0,column=0,rowspan=3,sticky='news')

def registration() :
    if fullname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter firstname")
        fullname.focus_force()
    elif lastname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter lastname")
        lastname.focus_force()
    elif std.get() == "" :
        messagebox.showwarning("Admin: ","Please enter ID card")
        std.focus_force()
    elif year.get() == "" :
        messagebox.showwarning("Admin: ","Please enter Phone number")
        std.focus_force()            
    elif newuser.get() == "" :
        messagebox.showwarning("Admin: ","Please enter Email")
        newuser.focus_force()
    elif newpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter password")
        newpwd.focus_force
    elif cfpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter confirm password")
        cfpwd
    else : 
        sql = "select * from Students where email = ?"
       
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchall() 
        if result :
            messagebox.showwarning("Admin:","The username is already exists")
            newuser.select_range(0,END)
            newuser.focus_force()
        else :
            if newpwd.get() == cfpwd.get() : 
                sql = "insert into Students values (?,?,?,?,?,?)" 
                param = [fullname.get(),lastname.get(),std.get(),year.get(),newuser.get(),newpwd.get()]
                cursor.execute(sql,param)
                conn.commit()
                messagebox.showinfo("Admin:","Registration Successfully")
                loginlayout()                
            else :  
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                cfpwd.select_range(0,END)
                cfpwd.focus_force


def welcomepage(result) :
    global welcomeframe
    welcomeframe = Frame(root,bg='white')#F68989
    welcomeframe.columnconfigure((0,1),weight=1)

    #Label(root,text= 'Home',bg='lightgreen',font="tomaho 20").grid(row=0,column=0,sticky='news')
    Label(welcomeframe,text= 'Wellcome '+result[0],bg='white',font="tomaho 20 bold",height=1).grid(row=0,column=0,columnspan=2)   
    Label(welcomeframe,text= 'Trending Coins',bg='#FFA8A8',font="tomaho 14",anchor=W).grid(row=1,columnspan=2,sticky= NSEW)
    Label(welcomeframe,text='Name',bg='white',font="tomaho 10").grid(row=2,column=0)
    Label(welcomeframe,text='Last price',bg='white',font="tomaho 10",width=10,anchor='e').grid(row=2,column=1)

    Button(welcomeframe,bg='white',font="tomaho 10",borderwidth=0,image=imgbit,command=lambda:buyandsell(img18,'Bitcoin(BTC)',1070220.0,gbit)).grid(row=3,column=0,columnspan=2,sticky=N)
    
    Button(welcomeframe,bg='white',font="tomaho 10",borderwidth=0,image=imgeth,command=lambda:buyandsell(img11,'Ethereum(ETH)',79000.0,geth)).grid(row=4,column=0,columnspan=2,sticky=N)
  
    Button(welcomeframe,bg='white',font="tomaho 10",borderwidth=0,image=imgada,command=lambda:buyandsell(img12,'Cardano(ADA)',21.71,gada)).grid(row=5,column=0,columnspan=2,sticky=N)
    
    Button(welcomeframe,bg='white',font="tomaho 10",borderwidth=0,image=imgtrx,command=lambda:buyandsell(img13,'Tron(Trx)',2.65,gtrx)).grid(row=6,column=0,columnspan=2,sticky=N)
    welcomeframe.grid(row=0,column=0,rowspan=2,sticky='news')

#หน้าข่าวสาร
def newspage():  #หน้าข่าว
    newsframe = Frame(root,bg='white')
    newsframe.rowconfigure((0,1,2),weight=0)
    newsframe.columnconfigure((0),weight=1)
    Label(root,text= 'News',bg='white',font="tomaho 20 bold").grid(row=0,column=0,sticky='news')
    Label(newsframe,image = new1,bg='white').grid(row=0,column=0,padx=20)
    Label(newsframe,image = new2,bg='white').grid(row=1,column=0,padx=20)
    Label(newsframe,image = new3,bg='white').grid(row=2,column=0,padx=20)
    newsframe.grid(row=1,column=0,sticky='news')
  
    
conn,cursor = createconnection()
def market() :
    marketframe = Frame(root,bg='white')
    marketframe.columnconfigure((1),weight=1)
    marketframe.columnconfigure((0),weight=1)
    Label(root,text='Market',bg='White',font="tomaho 20 bold").grid(row=0,column=0,sticky='news')
    Label(marketframe,text='Name',bg='white',font="tomaho 10").grid(row=1,column=0)
    
    Label(marketframe,image=ent2,bg='white').grid(row=0,column=0,sticky=W,columnspan=2)
    Ent = Entry(marketframe,bg='white',font="tomaho 14",width=40,borderwidth=0)
    Ent.place(x=7,y=17)
    Button(marketframe,image=imgsearch,bg='white',borderwidth=0,width=32,command=lambda:searchpage(Ent.get())).grid(row=0,column=0,columnspan=2,sticky=E)
    Label(marketframe,text='Last price',bg='white',font="tomaho 10",width=10,anchor='e').grid(row=1,column=1)

    Button(marketframe,bg='white',font="tomaho 10",borderwidth=0,image=imgbit,command=lambda:buyandsell(img18,'Bitcoin(BTC)',1070220.0,gbit)).grid(row=2,column=0,columnspan=2,sticky=N)
    
    Button(marketframe,bg='white',font="tomaho 10",borderwidth=0,image=imgeth,command=lambda:buyandsell(img11,'Ethereum(ETH)',79000.0,geth)).grid(row=3,column=0,columnspan=2,sticky=N)
  
    Button(marketframe,bg='white',font="tomaho 10",borderwidth=0,image=imgada,command=lambda:buyandsell(img12,'Cardano(ADA)',21.7,gada)).grid(row=4,column=0,columnspan=2,sticky=N)
    
    Button(marketframe,bg='white',font="tomaho 10",borderwidth=0,image=imgtrx,command=lambda:buyandsell(img13,'Tron(Trx)',2.65,gtrx)).grid(row=5,column=0,columnspan=2,sticky=N)
    

    marketframe.grid(row=1,column=0,sticky='news')

def searchpage(Ent) :
    marketframe = Frame(root,bg='white')
    marketframe.columnconfigure((1),weight=1)
    marketframe.columnconfigure((0),weight=1)
    Label(root,text='Market',bg='White',font="tomaho 20 bold").grid(row=0,column=0,sticky='news')
    Label(marketframe,text='Name',bg='white',font="tomaho 10").grid(row=1,column=0)
 
    Label(marketframe,image=ent2,bg='white').grid(row=0,column=0,sticky=W,columnspan=2)

    
    Label(marketframe,text='Last price',bg='white',font="tomaho 10",width=10,anchor='e').grid(row=1,column=1)
    if Ent == 'BTC' or Ent == 'Bitcoin' :
     Button(marketframe,bg='white',font="tomaho 10",borderwidth=0,image=imgbit,command=lambda:buyandsell(img18,'Bitcoin(BTC)',1070220.0,gbit)).grid(row=2,column=0,columnspan=2,sticky=N)
    elif Ent == 'ETH' or Ent == 'Ethereum' :
     Button(marketframe,bg='white',font="tomaho 10",borderwidth=0,image=imgeth,command=lambda:buyandsell(img11,'Ethereum(ETH)',79000.0,geth)).grid(row=2,column=0,columnspan=2,sticky=N)
    elif Ent == 'ADA' or Ent == 'Cardano' :
     Button(marketframe,bg='white',font="tomaho 10",borderwidth=0,image=imgada,command=lambda:buyandsell(img12,'Cardano(ADA)',21.7,gada)).grid(row=2,column=0,columnspan=2,sticky=N)
    elif Ent == 'TRX' or Ent == 'Tron' :
     Button(marketframe,bg='white',font="tomaho 10",borderwidth=0,image=imgtrx,command=lambda:buyandsell(img13,'Tron(Trx)',2.65,gtrx)).grid(row=2,column=0,columnspan=2,sticky=N)
    Ent = Entry(marketframe,bg='white',font="tomaho 14",width=40,borderwidth=0)
    Ent.place(x=7,y=17)
    Button(marketframe,image=imgsearch,bg='white',borderwidth=0,width=32,command=lambda:searchpage(Ent.get())).grid(row=0,column=0,columnspan=2,sticky=E)
    marketframe.grid(row=1,column=0,sticky='news')

def portfolio() :
     Label(root,text= 'Portfolio',bg='white',font="tomaho 20 bold").grid(row=0,column=0,sticky='news')
     portframe = Frame(root,bg='white')
     portframe.rowconfigure((0,1),weight=0)
     portframe.columnconfigure((0),weight=1)
     Label(portframe,text='Equity Value (฿) : 10000',bg='white',font="tomaho 15 ",height=5).grid(row=0,column=0,sticky=W,padx=10)
     
     mytree = ttk.Treeview(portframe, show='headings',columns= ("col1","col2","col3","col4"),height=5)
     mytree.grid(row=1,column=0)

     mytree.heading("col1",text="Name")
     mytree.heading("col2",text="Amount")
     mytree.heading("col3",text="Price(฿)")
     mytree.heading("col4",text="Percent(%)")
 
     mytree.column("col1", width=150, minwidth=150)
     mytree.column("col2", width=150, minwidth=150,anchor='center')
     mytree.column("col3", width=150, minwidth=150,anchor='center')
     mytree.column("col4", width=150, minwidth=150,anchor='center')
  
     cursor = conn.cursor()
     sql = '''SELECT Name, amount,Price,Percent 
     FROM coin
     ORDER BY Percent DESC;'''
     cursor.execute(sql)
     result = cursor.fetchall()
  
     for i,record in enumerate (result) :
       mytree.insert('','end',values=record)
    
     portframe.grid(row=1,column=0,sticky='news')

def profilee() :
    sql = "Select * From Students Where first_name = ?"
    cursor.execute(sql, [result[0]])
    item = cursor.fetchone() 
    Label(root,text= 'Profile',bg='white',font="tomaho 20 bold").grid(row=0,column=0,sticky='news')
    profileframe = Frame(root,bg='white')
    profileframe.rowconfigure((0,1,2,3),weight=0)
    profileframe.columnconfigure((0),weight=1) 
    Label(profileframe,bg='white',image=prof).grid(row=0,column=0)
    Label(profileframe,bg='#F68989',text=item[0]+' '+item[1],fg='white',font="tomaho 16").grid(row=0,column=0,sticky='s',pady=80)
    Button(profileframe,image=imgperso,command= personal,bg='white',borderwidth=0).grid(row=1,column=0,sticky='NEWS')
    Button(profileframe,image=imgbank,command= bank,bg='white',borderwidth=0).grid(row=2,column=0,sticky='NEWS')
    Button(profileframe,image=imglog,command=loginlayout,bg='white',borderwidth=0).grid(row=3,column=0,sticky='NEWS')
    profileframe.grid(row=1,column=0,sticky='news')


def personal() :
    global item
    personalframe = Frame(root,bg='white')
    personalframe.rowconfigure((0,1,2,3,4,5),weight=0)
    personalframe.columnconfigure((0,1),weight=1)
    sql = "Select * From Students Where first_name = ?"
    cursor.execute(sql, [result[0]])
    item = cursor.fetchone() 
    Label(personalframe,text= 'Personal information',width=10,height=2,font="tomaho 22",bg='#F68989',fg='white').grid(row=0,column=0,columnspan=2,sticky='NEWS')
    Label(personalframe,text="Name:",bg='white',font="tomaho 15",height=4).grid(row=1,column=0,sticky='e')
    Label(personalframe,text="Last Name :",bg='white',font="tomaho 15",height=4).grid(row=2,column=0,sticky='e')
    Label(personalframe,text="Email :",bg='white',font="tomaho 15",height=4).grid(row=3,column=0,sticky='e')
    Label(personalframe,text="Phone number :",bg='white',font="tomaho 15",height=4).grid(row=4,column=0,sticky='e')
    Label(personalframe,text= item[0],bg='white',font="tomaho 15").grid(row=1,column=1,sticky='w',padx=20)
    Label(personalframe,text= item[1],bg='white',font="tomaho 15").grid(row=2,column=1,sticky='w',padx=20)
    Label(personalframe,text= item[4],bg='white',font="tomaho 15").grid(row=3,column=1,sticky='w',padx=20)
    Label(personalframe,text= item[3],bg='white',font="tomaho 15").grid(row=4,column=1,sticky='w',padx=20)
    Button(personalframe,command=changeinfo,bg='white',borderwidth=0,image=imgchp).grid(row=5,column=0,columnspan=2,ipadx=5,pady=10)
    Button(personalframe,text="Back",font="tomaho 15",command=profilee,borderwidth=0,bg='#F68989',fg='white',image=backw,compound="left").grid(row=0,column=0,sticky='w')
    personalframe.grid(row=0,rowspan=2, column=0,sticky='news')

def changeinfo():
    global e1,e2,e3,e5,cframe
    cframe = Frame(root,bg='white')
    StringVar()
    cframe.rowconfigure((0,1,2,3,4,5),weight=0)
    cframe.columnconfigure((0,1),weight=1) 
    Label(cframe,text= 'Change infomation',width=10,height=2,font="tomaho 22",fg='white',bg="#F68989").grid(row=0,column=0,columnspan=2,sticky='NEWS')
    Label(cframe,text="Name:",bg='white',height=4,font="tomaho 15").grid(row=1,column=0,sticky='e')
    Label(cframe,text="Last Name :",bg='white',height=4,font="tomaho 15").grid(row=2,column=0,sticky='e')
    Label(cframe,text="Email :",bg='white',height=4,font="tomaho 15").grid(row=3,column=0,sticky='e')
    Label(cframe,text="Phone number :",bg='white',height=4,font="tomaho 15").grid(row=4,column=0,sticky='e')
    e1 = Entry(cframe ,bg='lightgray',borderwidth=0,font="tomaho 15")
    e1.grid(row=1,column=1,sticky='w',padx=20)  
    e1.insert(0,item[0])
    e2 =Entry(cframe,bg='lightgray',borderwidth=0,font="tomaho 15")
    e2.grid(row=2,column=1,sticky='w',padx=20)
    e2.insert(0,item[1])
    e3 =Entry(cframe,bg='lightgray',borderwidth=0,font="tomaho 15")
    e3.grid(row=3,column=1,sticky='w',padx=20)
    e3.insert(0,item[4])
    e5 =Entry( cframe,bg='lightgray',borderwidth=0,font="tomaho 15")
    e5.grid(row=4,column=1,sticky='w',padx=20)
    e5.insert(0,item[3])
    Button( cframe,command= updata,bg='white',borderwidth=0,image=imgd).grid(row=5,column=0,columnspan=2,ipadx=5,pady=10)
    Button( cframe,text="Back",font="tomaho 15",command=profilee,borderwidth=0,bg="#F68989",fg='white',image=backw,compound="left").grid(row=0,column=0,sticky='W')
    cframe.grid(row=0,rowspan=2, column=0,sticky='news')

def updata() :
    sql = """UPDATE Students 
            SET first_name = ?,
                last_name = ?,
                email = ?,
                phone = ?
            WHERE first_name = ?"""
    cursor.execute(sql,[e1.get(),e2.get(),e3.get(),e5.get(),result[0]])
    conn.commit()
    messagebox.showinfo("Admin :","Updata infomation Successfully.")
    personal()
    cframe.destroy()

def bank() :
    global b1
    sql = "Select * From Students Where first_name = ?"
    cursor.execute(sql, [result[0]])
    item = cursor.fetchone()
    bankframe = Frame(root,bg='white')
    bankframe.rowconfigure((0,1,2,3),weight=0)
    bankframe.columnconfigure((0,1),weight=1) 
    Label(bankframe,text= 'Bank account',width=10,height=2,font="tomaho 22",bg='#F68989',fg='white').grid(row=0,column=0,columnspan=2,sticky='NEWS')
    Label(bankframe,text="ID Card :",bg='white',height=3,font="tomaho 15").grid(row=2,column=0,sticky='e',padx=10)
    Label(bankframe,image=card,bg='white').grid(row=1,column=0,columnspan=2)
    b1 = Entry(bankframe,bg='lightgray',borderwidth=0,font="tomaho 15")
    b1.grid(row=2,column=1,sticky='w')  
    b1.insert(0,item[2])
    num = item[2]
    x = [int(a) for a in str(num)]
    bx ='%d%d%d%d'%(x[-4],x[-3],x[-2],x[-1])
    Label(bankframe,text=bx,bg='#b980f0',font="tomaho 13 bold",fg='white',width=5).place(x=300,y=216)
    Button(bankframe,command=changebank,bg='white',borderwidth=0,image=imgcha).grid(row=3,column=0,columnspan=2,ipadx=5,pady=20)
    Button(bankframe,text="Back",font="tomaho 15",bg='#F68989',command=profilee,borderwidth=0,fg='white',image=backw,compound="left").grid(row=0,column=0,sticky='W')
    bankframe.grid(row=0,rowspan=2,column=0,sticky='news')

def changebank() :
    sql = """UPDATE Students 
            SET idcard = ?
           WHERE first_name = ?"""
    cursor.execute(sql,[b1.get(),result[0]])
    conn.commit()
    messagebox.showinfo("Admin :","Updata Bank Successfully.")
    bank()

def buyandsell(img,name,price,g) :
    
    bsframe = Frame(root,bg='white')
    bsframe.rowconfigure((0,1,2,3),weight=0)
    bsframe.columnconfigure((0,1),weight=1)
    Button(bsframe,text= 'Back',bg='white',font="tomaho 20",borderwidth=0,command=bsframe.destroy,image=back,compound="left").grid(row=0,column=0,sticky='w',pady=10,padx=20)      
    Label(bsframe,text=' '+name,bg='white',font="tomaho 20",image=img,compound="left").grid(row=0,column=1,sticky='e',padx=20)

    Label(bsframe,image=g,bg='white').grid(row=1,columnspan=2)
    Button(bsframe,image=imgb,borderwidth=0,bg='white',command=lambda:buy(name,price,img)).grid(row=2,column=0,pady=20,padx=20)
    Button(bsframe,image=imgs,borderwidth=0,bg='white',command=lambda:sell(name,price,img)).grid(row=2,column=1,pady=20,padx=20)
    bsframe.grid(row=0,column=0,rowspan=3,sticky='news')

def buy(name,price,img) :
    global operator,cur,textin,textin1
    bsframe = Frame(root,bg='white')
    bsframe.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=0)
    bsframe.columnconfigure((0,1,2),weight=1)
    sql = "select * from coin where Name='Baht(THB)' "
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    cp = result[2]
    cur = DoubleVar()
    cur.set(cp)
    Button(bsframe,text= 'Back',bg='white',font="tomaho 20",command=bsframe.destroy,image=back,compound="left",borderwidth=0).grid(row=0,column=0,sticky='w',pady=10,padx=20,columnspan=3)      
    Label(bsframe,text= name,bg='white',font="tomaho 25",image=img,compound="left").grid(row=1,column=0,padx=20,columnspan=3,sticky='w')
    Label(bsframe,text= 'Current Balance : ฿',bg='white',font="tomaho 20").grid(row=4,column=0,columnspan=3,sticky='w',padx=20,pady=20)
    Label(bsframe,bg='white',font="tomaho 20",textvar=cur).place(x=265,y=214)
    textin=DoubleVar()
    textin1 = DoubleVar()
    operator=""
    def clickbut(number):   
      global operator,op,oper
      operator=operator+str(number)
      textin.set(operator)
      oper = eval(operator)
      op= (eval(operator)*price)
      textin1.set('%.2f'%op)


    def clrbut():
      global operator
      operator=''
      textin.set(0.0)
      textin1.set(0.0)
     
    label = Label(bsframe,bg='white',fg='black',font=("tomaho",26),textvar=textin)
    label.grid(row=2,column=0,columnspan=3,padx=15)

    label = Label(bsframe,bg='white',fg='black',font=("tomaho",16),textvar=textin1)
    label.grid(row=3,column=0,columnspan=3)

    but1=Button(bsframe,bg='white',borderwidth=0,text='Clear',command=clrbut,width=7,height=3)
    but1.grid(row=8,column=2)


    but5=Button(bsframe,bg='white',borderwidth=0,text='1',command=lambda:clickbut(1),width=7,height=3)
    but5.grid(row=5,column=0)

    but6=Button(bsframe,bg='white',borderwidth=0,text='2',command=lambda:clickbut(2),width=7,height=3)
    but6.grid(row=5,column=1)

    but7=Button(bsframe,bg='white',borderwidth=0,text='3',command=lambda:clickbut(3),width=7,height=3)
    but7.grid(row=5,column=2)


    but9=Button(bsframe,bg='white',borderwidth=0,text='4',command=lambda:clickbut(4),width=7,height=3)
    but9.grid(row=6,column=0)

    but10=Button(bsframe,bg='white',borderwidth=0,text='5',command=lambda:clickbut(5),width=7,height=3)
    but10.grid(row=6,column=1)

    but11=Button(bsframe,bg='white',borderwidth=0,text='6',command=lambda:clickbut(6),width=7,height=3)
    but11.grid(row=6,column=2)


    but13=Button(bsframe,bg='white',borderwidth=0,text='7',command=lambda:clickbut(7),width=7,height=3)
    but13.grid(row=7,column=0)

    but14=Button(bsframe,bg='white',borderwidth=0,text='8',command=lambda:clickbut(8),width=7,height=3)
    but14.grid(row=7,column=1)

    but15=Button(bsframe,bg='white',borderwidth=0,text='9',command=lambda:clickbut(9),width=7,height=3)
    but15.grid(row=7,column=2)


    but17=Button(bsframe,bg='white',borderwidth=0,text='0',command=lambda:clickbut(0),width=7,height=3)
    but17.grid(row=8,column=1)

    but18=Button(bsframe,bg='white',borderwidth=0,text='.',command=lambda:clickbut("."),width=7,height=3)
    but18.grid(row=8,column=0)

    Button(bsframe,image=imgb1,bg='white',borderwidth=0,command=lambda:buycal(name,cp,oper)).grid(row=9,column=0,columnspan=3,pady=20,padx=20)
    bsframe.grid(row=0,column=0,rowspan=3,sticky='news')

def sell(name,price,img) :
    global operator,Ava,textin,textin1
    bsframe = Frame(root,bg='white')
    bsframe.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=0)
    bsframe.columnconfigure((0,1,2),weight=1)
    sql = "select * from coin where Name='Baht(THB)' "
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    cp = result[2]
    sql = "select * from coin where Name=? "
    cursor.execute(sql,[name])
    result = cursor.fetchone()
    print(result)
    ap = result[1]
    Ava = DoubleVar()
    Ava.set(ap)
    Button(bsframe,text= 'Back',bg='white',font="tomaho 20",command=bsframe.destroy,borderwidth=0,image=back,compound="left").grid(row=0,column=0,sticky='w',pady=10,padx=20,columnspan=3)      
    Label(bsframe,text= name,bg='white',font="tomaho 25",image=img,compound="left").grid(row=1,column=0,columnspan=3,padx=20,sticky='w')
    Label(bsframe,text= 'Avaliable Balance :',bg='white',font="tomaho 20").grid(row=4,column=0,columnspan=3,sticky='w',padx=20,pady=20)
    Label(bsframe,bg='white',font="tomaho 20",textvar=Ava).place(x=265,y=214)
    textin=DoubleVar()
    textin1 = DoubleVar()
    operator=""
    def clickbut(number):   
      global operator,op,oper
      operator=operator+str(number)
      textin.set(operator)
      oper = eval(operator)
      op= (eval(operator)*price)
      textin1.set('%.2f'%op)


    def clrbut():
      global operator
      operator=''
      textin.set(0.0)
      textin1.set(0.0)
     
    label = Label(bsframe,bg='white',fg='black',font=("tomaho",26),textvar=textin)
    label.grid(row=2,column=0,columnspan=3,padx =15)

    label = Label(bsframe,bg='white',fg='black',font=("tomaho",16),textvar=textin1)
    label.grid(row=3,column=0,columnspan=3)

    but1=Button(bsframe,bg='white',borderwidth=0,text='Clear',command=clrbut,width=7,height=3)
    but1.grid(row=8,column=2)


    but5=Button(bsframe,bg='white',borderwidth=0,text='1',command=lambda:clickbut(1),width=7,height=3)
    but5.grid(row=5,column=0)

    but6=Button(bsframe,bg='white',borderwidth=0,text='2',command=lambda:clickbut(2),width=7,height=3)
    but6.grid(row=5,column=1)

    but7=Button(bsframe,bg='white',borderwidth=0,text='3',command=lambda:clickbut(3),width=7,height=3)
    but7.grid(row=5,column=2)


    but9=Button(bsframe,bg='white',borderwidth=0,text='4',command=lambda:clickbut(4),width=7,height=3)
    but9.grid(row=6,column=0)

    but10=Button(bsframe,bg='white',borderwidth=0,text='5',command=lambda:clickbut(5),width=7,height=3)
    but10.grid(row=6,column=1)

    but11=Button(bsframe,bg='white',borderwidth=0,text='6',command=lambda:clickbut(6),width=7,height=3)
    but11.grid(row=6,column=2)


    but13=Button(bsframe,bg='white',borderwidth=0,text='7',command=lambda:clickbut(7),width=7,height=3)
    but13.grid(row=7,column=0)

    but14=Button(bsframe,bg='white',borderwidth=0,text='8',command=lambda:clickbut(8),width=7,height=3)
    but14.grid(row=7,column=1)

    but15=Button(bsframe,bg='white',borderwidth=0,text='9',command=lambda:clickbut(9),width=7,height=3)
    but15.grid(row=7,column=2)


    but17=Button(bsframe,bg='white',borderwidth=0,text='0',command=lambda:clickbut(0),width=7,height=3)
    but17.grid(row=8,column=1)

    but18=Button(bsframe,bg='white',borderwidth=0,text='.',command=lambda:clickbut("."),width=7,height=3)
    but18.grid(row=8,column=0)

    Button(bsframe,image=imgs1,bg='white',borderwidth=0,command=lambda:sellcal(name,ap,oper,cp,price)).grid(row=9,column=0,columnspan=3,pady=20,padx=20)
    bsframe.grid(row=0,column=0,rowspan=3,sticky='news')

def buycal(name,cp,oper) :
    if op > cp :
        messagebox.showwarning("User :","Your balance is not enough")
    else : 
        cp = cp-op
        per = (op/10000)*100
        textin.set(0.0)
        textin1.set(0.0)
        cur.set(cp)
        perb = (cp/10000)*100
        createconnection()
        sql = '''update coin
        set amount = ?, Price = ?,Percent=?
        where Name = 'Baht(THB)' '''
        parameter = [cp,cp,'%0.2f'%perb]
        cursor.execute(sql,parameter)
        sql = '''update coin
        set amount = ?, Price = ?,Percent=?
        where Name = ?'''
        parameter = [oper,op,'%0.2f'%per,name]
        cursor.execute(sql,parameter)
        conn.commit()
        messagebox.showinfo("User","Successful transaction")

def sellcal(name,ap,oper,cp,price) :
    if oper > ap :
        messagebox.showwarning("User :","Your balance is not enough")
    else : 
        ap = ap-oper
        Ava.set(ap)
        am = op+cp
        perb = (am/10000)*100
        textin.set(0.0)
        textin1.set(0.0)
        pri = ap*price
        per = (pri/10000)*100
        sql = '''update coin
        set amount = ?, Price = ?,Percent=?
        where Name = 'Baht(THB)' '''
        parameter = [am,am,'%0.2f'%perb]
        cursor.execute(sql,parameter)
        sql = '''update coin
        set amount = ?, Price = ?,Percent=?
        where Name = ?'''
        parameter = [ap,pri,'%0.2f'%per,name]
        cursor.execute(sql,parameter)
        conn.commit()
        messagebox.showinfo("User","Successful transaction")



root = mainwindow()
img6 = PhotoImage(file='Project_cs311/image/home.png') # รูปหน้า welcomepage
img7 = PhotoImage(file='Project_cs311\image\wallets.png') # รูปหน้า welcomepage
img8 = PhotoImage(file='Project_cs311\image\info.png') # รูปหน้า welcomepage
img9  = PhotoImage(file='Project_cs311\image\market.png') # รูปหน้า welcomepage
img10 = PhotoImage(file='Project_cs311\image\profile.png') # รูปหน้า welcomepage
img11 = PhotoImage(file='Project_cs311/iconc/ETH.png') # รูปหน้า welcomepage
img12 = PhotoImage(file='Project_cs311/iconc/ADA.png') # รูปหน้า welcomepage
img13 = PhotoImage(file='Project_cs311/iconc/TRX.png') # รูปหน้า welcomepage
img18 = PhotoImage(file='Project_cs311/iconc/BTC.png') # รูปหน้า welcomepage
imgb = PhotoImage(file='Project_cs311/button1/Buy.png')
imgs = PhotoImage(file='Project_cs311/button1/Sell.png')
imgbit = PhotoImage(file='Project_cs311/button1/Bitcoin(P).png').subsample(1,1)
imgeth = PhotoImage(file='Project_cs311/button1/Ethereum.png').subsample(1,1)
imgada = PhotoImage(file='Project_cs311/button1/Cardano.png').subsample(1,1)
imgtrx = PhotoImage(file='Project_cs311/button1/Tron.png').subsample(1,1)
imgdoge = PhotoImage(file='Project_cs311/button1/Doge.png').subsample(1,1)
gbit = PhotoImage(file='Project_cs311/button1/gbit.png')
geth = PhotoImage(file='Project_cs311/button1/geth.png')
gada = PhotoImage(file='Project_cs311/button1/gada.png')
gtrx = PhotoImage(file='Project_cs311/button1/gtrx.png')
lg = PhotoImage(file='Project_cs311/button1\Login.png')
rg = PhotoImage(file='Project_cs311/button1/Register.png')
imgperso = PhotoImage(file='Project_cs311/image/perso.png')
imgbank = PhotoImage(file='Project_cs311/image/bank.png')
imglog = PhotoImage(file='Project_cs311/image/logout.png')
imgchp = PhotoImage(file='Project_cs311/image/chp.png')
imgd = PhotoImage(file='Project_cs311/image/Update.png')   
imgcha = PhotoImage(file='Project_cs311/image/cha.png')
imgb1 = PhotoImage(file='Project_cs311/image/buy1.png')
imgs1 = PhotoImage(file='Project_cs311/image/sell1.png')
back = PhotoImage(file='Project_cs311/image/back.png')
backw = PhotoImage(file='Project_cs311/image/backw.png')
cancel = PhotoImage(file='Project_cs311/regis\cancel.png').subsample(1,1)
rn = PhotoImage(file='Project_cs311/regis/rn.png').subsample(1,1)
card = PhotoImage(file='Project_cs311\image\card.png')
ent = PhotoImage(file='Project_cs311\image\entry.png')
ent1 = PhotoImage(file='Project_cs311\image\entry1.png')
ent2 = PhotoImage(file='Project_cs311\image\entry1.png').subsample(1,1)
imgsearch = PhotoImage(file='Project_cs311/image/search.png')
new1 = PhotoImage(file='Project_cs311/image/new1.png')
new2 = PhotoImage(file='Project_cs311/image/new2.png')
new3 = PhotoImage(file='Project_cs311/image/new3.png')
prof = PhotoImage(file='Project_cs311/image/prof.png')
# profilee()
loginlayout()
root.mainloop()
cursor.close()
conn.close()


