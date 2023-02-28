from tkinter import *
from tkinter import ttk
def main() : 
    root = Tk()
    root.geometry("500x200")
    root.title("Common widget: Listbox Widget")
    root.configure(bg="pink")
    root.columnconfigure((0,1),weight=1)
    return(root)

def changeclick() :
    combo['values'] 
    ["HTML5","Bootstrap","VueJS","VueSax","ReactJS"]
    combo.set("VueSax")
def resetclick() :
    combo['values'] 
    ["Java","C#","Swift","Python","PHP","NodeJS"]
    combo.set("Python")

def widget(root) :
    langlist = ["Java","C#","Swift","Python","PHP","NodeJS"]
    combo = ttk.Combobox(root,values=langlist,width=20)
    combo.set("Python")
    combo.grid(row=0,column=0,columnspan=2,pady=20)
    btn1 = Button(root,text="Change List",command=changeclick,width=10)
    btn1.grid(row=1,column=0,pady=10,ipadx=10,ipady=10,sticky='e',padx=2)
    btn2 = Button(root,text="Reset",command=resetclick,width=10)
    btn2.grid(row=1,column=1,pady=10,ipadx=10,ipady=10,sticky='w',padx=2)
    return(combo)
root = main()
combo = widget(root)
root.mainloop()
