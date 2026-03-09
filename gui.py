from tkinter import *
from tkinter import ttk

def addStudent(first,last):
    print(f"SQL Add to database {first} {last}")

def ourPrint(text):
    print(text)

def addButton(newText,newRow,newCommand=None):
    if newCommand==None:
        newCommand=lambda :ourPrint(newText)
    ttk.Button(frm, text=newText, command=newCommand).grid(column=0, row=newRow,sticky="EW")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="First Name").grid(column=0, row=0,sticky="EW")

first=StringVar()
last=StringVar()

ttk.Entry(frm,textvariable=first).grid(column=1, row=0,sticky="EW")
ttk.Label(frm, text="Last Name").grid(column=0, row=1,sticky="EW")
ttk.Entry(frm,textvariable=last).grid(column=1, row=1,sticky="EW")

addButton("Add a Student",2,lambda :addStudent(first.get(),last.get()))
addButton("List all Students",3)
addButton("Update a student",4)
addButton("Registrations for a student",5)
addButton("Delete a Student",6)
addButton("Quit",7,root.destroy)

root.mainloop()
