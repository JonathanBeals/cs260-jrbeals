import psycopg2

conn = psycopg2.connect(dbname="myapp",user="accounting",password="1234", host="localhost")

cur = conn.cursor()

def addStudent():
    print("Please enter the data below")
    first=input("First name ")
    last=input("Last name ")
    gpa=input("GPA ")
    major=input("Major ")
    query=f'''insert into students 
        (first, last, gpa, major) values 
        ('{first}','{last}',{gpa},'{major}');'''
    cur.execute(query)
    conn.commit()

def listStudents():
    query='''select (id,first,last) from students;'''
    cur.execute(query)
    records=cur.fetchall()
    print("ID\tFirst\tLast")
    print("+-----------+-----------+-----------+")
    for r in records:
        print(f"|{t[0]}\t|{t[1]}\t|{t[2]}|\t")
        t=tuple(r[0])


def deleteStudent():
    #Write this code to delete a student
    pass



choice=" "
while (choice!="q"):
    print("Menu of items")
    print("A) Add a student")
    print("L) List all students")
    print("D) Delete a student")
    print("Q) Quit")
    choice=input("Enter the number of the menu item ")
    if choice=='a':
        addStudent()
    if choice=='d':
        deleteStudent()
    if choice=='l':
        listStudents()
