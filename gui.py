from tkinter import *
from tkinter import ttk
import tkinter as tk
from db import *

def doAddStudent(first:str,last:str):
    print(f"SQL Add to database {first} {last}")
    # print(f"insert into student (first,last) values ('{first}','{last}')");
    insertStudent(first,last,0.0,"")

def studentDialog(root):
    dialog = tk.Toplevel(root)
    dialog.title("Add A Student")
    frm = ttk.Frame(dialog, padding=10)
    frm.grid()
    
    dialog.transient(root)
    dialog.grab_set()
    
    ttk.Label(frm, text="First Name").grid(column=0, row=0,sticky="EW")
    first=StringVar()
    last=StringVar()
    ttk.Entry(frm,textvariable=first).grid(column=1, row=0,sticky="EW")
    ttk.Label(frm, text="Last Name").grid(column=0, row=1,sticky="EW")
    ttk.Entry(frm,textvariable=last).grid(column=1, row=1,sticky="EW")
    
    addButton(frm,"Save Student",2,lambda :doAddStudent(first.get(),last.get()))
    button = ttk.Button(frm, text="Close", command=dialog.destroy).grid(column=1, row=2,sticky="EW")
    
    root.wait_window(dialog)

def doUpdateStudent(idStr,first,last):
    id=idStr.split(':')[0]
    print(id)
    if len(first)>0:
        updateField('first',first,id)
    if len(last)>0:
        updateField('last',last,id)

def updateStudent(root):
    dialog = tk.Toplevel(root)
    dialog.title("Update A Student")
    frm = ttk.Frame(dialog, padding=10)
    frm.grid()
    
    dialog.transient(root)
    dialog.grab_set()
    ttk.Label(frm, text="Student Id").grid(column=0, row=0,sticky="EW")
    selectIds=getIds()
    comboChoice=StringVar()
    ttk.Combobox(frm,state="readonly",values=selectIds,textvariable=comboChoice).grid(column=1, row=0,sticky="EW")
    ttk.Label(frm, text="First Name").grid(column=0, row=1,sticky="EW")
    first=StringVar()
    last=StringVar()
    ttk.Entry(frm,textvariable=first).grid(column=1, row=1,sticky="EW")
    ttk.Label(frm, text="Last Name").grid(column=0, row=2,sticky="EW")
    ttk.Entry(frm,textvariable=last).grid(column=1, row=2,sticky="EW")
    
    addButton(frm,"Update Student",3,lambda :doUpdateStudent(comboChoice.get(),first.get(),last.get()))
    button = ttk.Button(frm, text="Cancel", command=dialog.destroy).grid(column=1, row=3,sticky="EW")
    
    root.wait_window(dialog)

def doDeleteStudent(idStr):
    id=idStr.split(':')[0]
    deleteStudent(id)

def deleteStudent(root):
    dialog = tk.Toplevel(root)
    dialog.title("Delete A Student")
    frm = ttk.Frame(dialog, padding=10)
    frm = grid()

    dialog.transient(root)
    dialog.grab_set()
    ttk.Label(frm, text="Student Id").grid(column=0,row=0, sticky="EW")
    ttk.Combobox(frm,state='readonly',values=selectIds,textvariable=comboChoice).grid(column=1,row=0,sticky="EW")
    id=StringVar()
    selectIds = getIds()
    comboChoice=StringVar()
    ttk.Label(frm, text="Enter Student ID").grid(column=0,row=1,sticky="EW")

    addButton(frm,"Delete Student",4,lambda : doDeleteStudent(comboChoice.get()))
    button =ttk.Button(frm, text="Cancel",command=dialog.destroy).grid(column=1,row=3,sticky="EW")

    root.wait_window(dialog)


def listStudents(root):
    dialog = tk.Toplevel(root)
    dialog.title("List of students")
    frm = ttk.Frame(dialog, padding=10)
    frm.grid()
    
    dialog.transient(root)
    dialog.grab_set()
    query="select id,first,last,gpa,major from students;"
    records=getAll(query)
    ttk.Label(frm,text="Id").grid(column=0, row=0,sticky="EW")
    ttk.Label(frm,text="First").grid(column=1, row=0,sticky="EW")
    ttk.Label(frm,text="Last").grid(column=2, row=0,sticky="EW")
    ttk.Label(frm,text="GPA").grid(column=3, row=0,sticky="EW")
    ttk.Label(frm,text="Major").grid(column=4, row=0,sticky="EW")
    currentRow=1
    for r in records:
        currentRow+=1
        currentCol=0
        for f in r:
            ttk.Label(frm,text=f, background="white").grid(column=currentCol, row=currentRow,sticky="EW")
            currentCol+=1
    currentRow+=1
    button = ttk.Button(frm, text="Close", command=dialog.destroy).grid(column=0, row=currentRow,sticky="EW")    
    root.wait_window(dialog)

def ourPrint(text):
    print(text)

def addButton(frm,newText,newRow,newCommand=None):
    if newCommand==None:
        newCommand=lambda :ourPrint(newText)
    ttk.Button(frm, text=newText, command=newCommand).grid(column=0, row=newRow,sticky="EW")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

addButton(frm,"Add a Student",2,lambda :studentDialog(root))
addButton(frm,"List all Students",3,lambda :listStudents(root))
addButton(frm,"Update a student",4,lambda :updateStudent(root))
addButton(frm,"Registrations for a student",5)
addButton(frm,"Delete a Student",6)
addButton(frm,"Quit",7,root.destroy)

root.mainloop()
