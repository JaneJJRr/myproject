from tkinter import *
root = Tk()
root.geometry("500x200")
root.title("Common widget: Radio Button")
root.configure(bg="pink")
v1,v2,v3,v4 = IntVar(),IntVar(),IntVar(),IntVar()
ck1 = Checkbutton(text="อ่างอาบน้ำ",bg='pink',variable=v1)
ck2 = Checkbutton(text="ห้องวิวกระจก",bg='pink',variable=v2)
ck3 = Checkbutton(text="อาหารเช้า",bg='pink',variable=v3)
ck4 = Checkbutton(text="บริการเตียงเสริม",bg='pink',variable=v4)
ck1.pack(anchor='w')
ck2.pack(anchor='w')
ck3.pack(anchor='w')
ck4.pack(anchor='w')
root.mainloop()