import matplotlib.pyplot as plt
import psycopg2

conn = psycopg2.connect(dbname="myapp", user="accounting", password="1234",host="localhost")

cur = conn.cursor()

table="river2025"
# Middle of year
where=" where t>=183.0 and t<184.0"
# Happy fish
#where=" where diso>6 and ph>=6.5 and ph<=8.5"
# Not Happy fish
#where=" where not (diso>6 and ph>=6.5 and ph<=8.5)"
fields=[("t","t(s)"),("turb","Turbidity()"),("ph","pH"),
 ("diso","Dissolved Oxygen()"),("cond","Conductivity()"),
 #("discharge","Discharge()"),
 ("height","Height (ft)"),("temp","Temperature (degC)")
  ]

def doCorrelation(rowField,colField,where):
    query=f'''select 
        corr({rowField},{colField}) as cor, 
        covar_samp({rowField},{colField}) as covar, 
        regr_intercept({rowField},{colField}) as b, 
        regr_slope({rowField},{colField}) as m 
        from {table} {where} limit 1;'''
    cur.execute(query)
    return cur.fetchone();

def doStats(field,where):
    query=f'''select 
        avg({field}) as m, 
        stddev_samp({field}) as s, 
        min({field}) as min, 
        max({field}) as max 
        from {table} {where} limit 1;'''
    cur.execute(query)
    return cur.fetchone();



#make a cols only list from the fields list/labels 
cols=""
for f in fields:
    if len(cols)>0:
        cols+=","
    cols+=f"{f[0]}"

query=f'''select {cols} from {table} {where};'''
cur.execute(query)
records=cur.fetchall()

fig, ax = plt.subplots(len(fields),len(fields))

for row in range(0,len(fields)):
    for col in range(0,len(fields)):
        if row==col:
            ax[row,col].axis('off')
            stats=doStats(fields[row][0],where)
            ax[row,col].text(0.1, 1.0,fields[row][1])
            ax[row,col].text(0.1,0.0, f"{stats[3]:.2f}") 
            ax[row,col].text(0.1,0.25,  f"{stats[2]:.2f}") 
            ax[row,col].text(0.1,0.5, f"{stats[1]:.2f}") 
            ax[row,col].text(0.1,0.75,  f"{stats[0]:.2f}" ) 
        elif row>col:
            xs=[]
            ys=[]
            for r in records:
                xs.append(r[col])
                ys.append(r[row])
            ax[row,col].scatter(xs,ys,s=1)
        else:
            ax[row,col].axis('off')
            correlation=doCorrelation(fields[row][0],fields[col][0],where)
            #print(correlation)
            ax[row,col].text(0.1,0.25, f"{correlation[3]:.2f}") 
            ax[row,col].text(0.1,0.5,  f"{correlation[2]:.2f}") 
            ax[row,col].text(0.1,0.75, f"{correlation[1]:.2f}") 
            ax[row,col].text(0.1,1.0,  f"{correlation[0]:.2f}" ) 
        if row<len(fields)-1: 
            ax[row,col].xaxis.set_visible(False)
        if  col!=0:
            ax[row,col].yaxis.set_visible(False)
plt.show()
