import psycopg2
import matplotlib.pyplot as plt

def toColumns(records):
    xs=[]
    ys=[]
    zs=[]
    for r in records:
        xs.append(r[0])
        ys.append(r[1])
        zs.append(r[2])
    return (xs,ys,zs)

conn = psycopg2.connect(dbname="myapp", user="accounting", password="1234",host="localhost")

cur = conn.cursor()

query='''select diso, ph, t from river2025;'''
cur.execute(query)
records=cur.fetchall()
xs,ys,zs=toColumns(records)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(xs,ys,zs,s=1,c='red')

K =input("Enter K: example 100 ")
goalT=input("Please enter goal time: example 183.0 ")
goalDiso=input("Please enter goal dissolved oxygen: example 11.11 ")
goalPh=input("Please enter goal ph: example 8.35 ")

query=f'''
        with ranges as (
            select max(t)-min(t) as tRange, 
                max(diso)-min(diso) as dRange, 
                max(ph)-min(ph) as pRange
                from river2025
        )
        select t,diso,ph,
         sqrt(((t-{goalT})/(select tRange from ranges))^2.0
             +((diso-{goalDiso})/(select dRange from ranges))^2.0
             +((ph-{goalPh})/(select pRange from ranges))^2.0) as d 
         from river2025
         order by d limit {K};
    '''

cur.execute(query)
records=cur.fetchall()
xs,ys,zs=toColumns(records)

ax.scatter(xs,ys,zs,s=10,c='green',marker='x')
ax.set_xlabel('t(days)')
ax.set_zlabel('diso(mg/L)')
ax.set_ylabel('ph')

plt.show()
