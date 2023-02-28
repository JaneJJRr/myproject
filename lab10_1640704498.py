import sqlite3
from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry('700x600+100+100')
window.title('Grade Report by janjira watcharawongsri')

def home(parent):
    fm_menu = login(parent)

def createconnection() :
    #global conn,cursor
    conn = sqlite3.connect('D:\CS311jane\week10\week10_1640704498.db')
    cursor = conn.cursor()
    return conn,cursor

def login(parent):
    global box_pwd,box_username
    userinfo = StringVar()
    pwdinfo = StringVar()

    fm = Frame(parent, width=800, height=600, bg='#FFCCCC').place(x=0,y=0)
    profile = Label(fm, image = img1, bg='#FFCCCC').place(x=170,y=170)
    lbl_username = Label(fm, bg= '#FFCCCC', text = 'Username', fg='black', font=('Tahoma', 18)).place(x=350,y=160)
    box_username = Entry(fm , bg='white', borderwidth=0, textvariable=userinfo).place(x=350,y=200)
    lbl_pwd = Label(fm, bg= '#FFCCCC', text = 'Password' ,fg='black', font=('Tahoma', 18)).place(x=350,y=230)
    box_pwd = Entry(fm , bg='white', show='*', borderwidth=0,  textvariable=pwdinfo,width=20).place(x=350,y=270)
    Button(fm, text='Login', font=('Tahoma', 18), width=10, bg='white',command=lambda:loginclick(userinfo.get(),pwdinfo.get(),parent)).place(x=340, y=320)
    return fm

def loginclick(username,password,parent) :
    if username == "" :
        messagebox.showwarning("Admin:","Username or Password is invalid.")
        box_username.focus_force()
    else :
        sql = "select * from Students where username=?"
        cursor.execute(sql,[username])
        result = cursor.fetchall()
        if result :
            if password == "" :
                messagebox.showwarning("Admin:","Username or Password is invalid.")
                box_pwd.focus_force()
            else :
                # print(result)
                sql = "select * from Students where username=? and password=? "
                cursor.execute(sql,[username,password])   
                result = cursor.fetchone()
                if result : #password correct
                    grade(result,parent,username)
                else : #password incorrect
                    messagebox.showwarning("Admin:","Username or Password invalid.")
                    box_pwd.select_range(0,END)
                    box_pwd.focus_force()
        else :
            messagebox.showerror("Admin:","Username or Password is invalid.")
            box_username.select_range(0,END)
            box_username.focus_force()

def grade(result,parent,username) :
    fm = Frame(parent, width=700, height=600, bg='#FFCCCC').place(x=0,y=0)
    profile = Label(fm, image = img1, bg='#FFCCCC').place(x=350,y=50)

    Label(parent, text='Student Id', font=('Tahoma', 18, 'bold'), bg='#FFCCCC').place(x = 100, y= 220)
    Label(parent, text='Name', font=('Tahoma', 18, 'bold'), bg='#FFCCCC').place(x = 100, y= 270)
    Label(parent, text='Score', font=('Tahoma', 18, 'bold'), bg='#FFCCCC').place(x = 100, y= 320)
    Label(parent, text='Grade', font=('Tahoma', 18, 'bold'), bg='#FFCCCC').place(x = 100, y= 370)

    if result[3] >= 80 :
        grade_d = 'A'
    elif result[3] >= 70 :
        grade_d = 'B'
    elif result[3] >= 60 :
        grade_d = 'C'
    elif result[3] >= 50 :
        grade_d = 'D'
    else :
        result[3] = 'F'

    id = Label(fm, text=result[0], font=('Tahoma', 18, 'bold'), bg='#FFCCCC')
    id.place(x = 300, y= 220)
    name = Label(fm, text=result[1]+' '+result[2], font=('Tahoma', 18, 'bold'), bg='#FFCCCC')
    name.place(x = 300, y= 270)
    score = Label(fm, text=result[3], font=('Tahoma', 18, 'bold'), bg='#FFCCCC')
    score.place(x = 300, y= 320)
    grade = Label(fm, text=grade_d, font=('Tahoma', 18, 'bold'), bg='#FFCCCC')
    grade.place(x = 300, y= 370)

    conn = sqlite3.connect('D:\CS311jane\week10\week10_1640704498.db')
    cursor = conn.cursor()

    sql = "SELECT * FROM Students where username = ?"
    cursor.execute(sql,[username])

    result = cursor.fetchone()
    # print(result)

    Button(fm, text='Log Out', font=('Tahoma', 18), width=10, bg='white',command=lambda:login(parent)).place(x=340, y=450)

str_keyword = StringVar()
img1 = PhotoImage(file='D:\CS311jane\week10\profile.png').subsample(2,2)
conn,cursor = createconnection()
home(window)
window.mainloop()