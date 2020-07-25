#Geometric Distribution
p=.5
c=0
l=[]
for num in range(1000):
    def bernoulli(p):
        r=np.random.random()
        if r<p:
            return 1
        else:
            return 0
             
    while(bernoulli(p)==0):
        c+=1
    l.append(c)
    c=0
plt.hist(l)
plt.show()
