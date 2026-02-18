import psycopg2

conn = psycopg2.connect(dbname="myapp",user="accounting",password="1234", host="localhost")

cur = conn.cursor()

phLevel=input("Please enter the ph breakpoint ")

cur.execute(f'''select
    corr(ph.value, discharge.value)
  from ph join discharge
    on left(time,16)=datetime
    where ph.value < {phLevel};''')

records = cur.fetchall()

print(records[0][0])