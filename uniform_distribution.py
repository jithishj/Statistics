l=[]
for num in range(10000):
    x=np.random.random()#Generate a RV betwen 0 and 1
    l.append(x)
plt.hist(l, bins=20)
