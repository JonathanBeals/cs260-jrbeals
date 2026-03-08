from tkinter import *
from tkinter import ttk

def addStudent(first,last):
    print("SQL add to database {first} {last}")

def addButton(newText, newRow, newCommand=None):
    if newCommand==None:
        newCommand=lambda :ourPrint(newText)
    ttk.Button(frm, text=newText, command=newCommand).grid(column=0,row=newRow,sticky="EW")

def ourPrint(text):
    print(text)

root = Tk()
frm= ttk.Frame(root,padding=10)
frm.grid()

ttk.Label(frm, text="First Name").grid(column=0,row=0,sticky="EW")
firstName = ttk.Entry(form).grid(column=0,row=0,sticky="EW")

ttk.Label(frm, text="Last Name").grid(column=0,row=0,sticky="EW")
firstName = ttk.Entry(form).grid(column=1,row=1,sticky="EW")

addButton("Add a student",2,lambda : addStudent(first.get(),last.get()))
addButton("List all students",3)
addButton("Update student",4)
addButton("Student registrations",5)
addButton("Delete a student",6)
addButton("Quit",7,root.destroy)

root.mainloop()