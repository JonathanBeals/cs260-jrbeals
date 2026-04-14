import psycopg2
import matplotlib.pyplot as plt

conn = psycopg2.connect(dbname="myapp", user="accounting", password="password",host="localhost")

cur = conn.cursor()

query='''select 
     housing_median_age as age,
     total_bedrooms as bedrooms,
     median_income as income 
     from housing;'''
cur.execute(query)
records=cur.fetchall()
#print(records)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
xs=[]
ys=[]
zs=[]
for r in records:
    xs.append(r[0])
    ys.append(r[1])
    zs.append(r[2])
ax.scatter(xs,ys,zs,s=1,c='red')

query="select min(housing_median_age)-max(housing_median_age) from housing;"
record=cur.fetchone()
rangeAge=record[0]

query="select min(total_bedrooms)-max(total_bedrooms) from housing;"
record=cur.fetchone()
bedroomsRange=record[0]

query="select min(median_income)-max(median_income) from housing;"
record=cur.fetchone()
incomeRange=record[0]

query=f'''select housing_median_age as age,
         total_bedrooms as bedrooms,
         median_income as income,
         sqrt(((housing_median_age-20)/{rangeAge})^2.0
              +((total_bedrooms-3000)/{bedroomsRange})^2.0
              +((median_income-6.0)/{incomeRange})^2.0) as d 
         from housing
         order by d limit 100;'''
cur.execute(query)
records=cur.fetchall()
xs=[]
ys=[]
zs=[]
for r in records:
    xs.append(r[0])
    ys.append(r[1])
    zs.append(r[2])
ax.scatter(xs,ys,zs,s=3,c='green')

plt.show()
