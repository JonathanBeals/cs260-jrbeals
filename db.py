import psycopg2

conn = psycopg2.connect(dbname="myapp", user="accounting", password="1234",host="localhost")

cur = conn.cursor()

def getIds():
    query="select id,first,last from students;"
    cur.execute(query)
    records=cur.fetchall()
    retVal=[]
    for r in records:
        retVal.append(f"{r[0]}:{r[2]},{r[1]}")
    return retVal

def insertStudent(first,last,gpa,major):
    query=f'''insert into students
         (first,last,gpa,major) values 
         ('{first}','{last}',{gpa},'{major}');'''
    cur.execute(query)
    conn.commit() 

def updateField(field,value,id):
    query=f"update students set {field}='{value}' where id={id};"
    cur.execute(query)
    conn.commit()

def getAll(query):
    cur.execute(query)
    return cur.fetchall()

if __name__ == "__main__":
    print("Hello from the database")

