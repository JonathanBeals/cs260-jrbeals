import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2)


#xs=[1,2,3,4]
#ys=[1,4,9,16]

xs=[]
ys=[]

for r in range(1 ,1000):
    xs.append(r)
    ys.append(r*r)

ax[0,0].axis('off')
ax[0,0].text(0.5, 0.5, 'X')
ax[1,1].axis('off')
ax[1,1].text(0.5, 0.5 ,'Y')
ax[0,1].scatter(xs,ys)
ax[1,0].scatter(ys,xs)

plt.show()