import psycopg2

conn = psycopg2.connect(dbname="myapp", user="accounting", password="1234",host="localhost")

cur = conn.cursor()

def addStudent():
    print("Please enter the data below")
    first=input("First name:")
    last=input("Last name:")
    gpa=input("GPA:")
    major=input("Major:")
    query=f'''insert into students
         (first,last,gpa,major) values 
         ('{first}','{last}',{gpa},'{major}');'''
    cur.execute(query)
    conn.commit() 

def updateField(field,value,id):
    query=f"update students set {field}='{value}' where id={id};"
    cur.execute(query)
    conn.commit()

def updateStudent():
    choice=" "
    print("Update Student Menu of items")
    listStudents()
    id=input("Enter the id of the student to update")
    while (choice!="q"):
        print("F)irst name change")
        print("L)ast name change")
        print("G)PA change")
        print("M)ajor change")
        print("Q)uit this menu")
        choice=input("Enter the number of the menu item ").lower()
        if choice=='f':
            updateField('first',input("Enter the new first name: "),id)
        elif choice=='l':
            updateField('last',input("Enter the new last name: "),id)
        elif choice=='g':
            updateField('gpa',input("Enter the new gpa: "),id)
        elif choice=='m':
            updateField('major',input("Enter the new major: "),id)

# [('id',4),('first',16),('last',16),('gpa',3),('major',8)]
def addLine(fields):
    for f in fields:
        print(f"+{'-':{(f[1]-1)}}-",end="")
    print("+")

def addHeader(fields):
    for f in fields:
        print(f"|{f[0]:{f[1]}}",end="")
    print("|")

def addRow(values,fields):
    index=0
    for f in fields:
        print(f"|{values[index]:{f[1]}}",end="")
        index+=1
    print("|")

def showTable(fields,query):
    #fields is an array that contains User Interface column name , width and database column
    #  example fields could be [('Id',4,'id'),('First',16,'first')]
    #query is the Postgres SQL query of the data to put in table
    cur.execute(query)
    records = cur.fetchall()
    addLine(fields)
    addHeader(fields)
    #addLine(fields)  Looks slightly cleaner without this line
    for r in records:
       addRow(r,fields)
    addLine(fields)

def makeColsList(fields):
    #fields is an array that contains User Interface column name , width and database column
    #  example fields could be [('Id',4,'id'),('First',16,'first')]

    cols=""
    for f in fields:
        if (len(cols)>0):
             cols+=","
        cols+=f[2]
    return cols

def listStudents():
    fields=[('Id',4,'id'),('First',16,'first'),('Last',16,'last'),('GPA',3,'gpa'),('Major',8,'major')]
    cols=makeColsList(fields)
  #  print(cols)
    query=f"select {cols} from students;"
    showTable(fields,query)

def registration():
    listStudents();
    id=input("Please enter id of student:")
    stuFields=[('Id',4,'id'),('First',16,'first'),('Last',16,'last'),('Major',8,'major'),('GPA',3,'gpa')]
    stuCols=makeColsList(stuFields)
    stuQuery=f"select {stuCols} from students where id={id}"
    regFields=[('Dept.',5,'dept'),('#',4,'number')]
    regCols=makeColsList(regFields)
    regQuery=f'''select {regCols} from registrations 
       join students on students_id=students.id 
       join courses on courses_crn=courses.crn 
       where students.id={id};'''
    print("--==Student information==--")
    showTable(stuFields,stuQuery)
    print("--==Current registrations==--")
    showTable(regFields,regQuery)

def deleteStudent():
    # Write this code to delete a student
    # I took the basic logic from add a student then realized that I didnt need
    # first or last names and i could just delete the student using their id.
    print("Please enter Students ID to delete: ")
    id=input("Id: ")
    query=f'''delete from students where id={id}'''
    cur.execute(query)
    conn.commit() 
    print("Student has been deleted")

choice=" "
while (choice!="q"):
    print("Menu of items")
    print("A)dd a Student")
    print("L)ist all students")
    print("U)pdate a student")
    print("R)egistrations for a student")
    print("D)elete a Student")
    print("Q)uit")
    choice=input("Enter the number of the menu item ").lower()
    if choice=='a':
        addStudent()
    elif choice=='d':
        deleteStudent()
    elif choice=='l':
        listStudents()
    elif choice=='r':
        registration()
    elif choice=='u':
        updateStudent()
