import matplotlib.pyplot as plt
lis=[]
lisb=[]
p=0
for num in range(10000):
    for val in range(10):
        k=np.random.random()
        if k >.8:
            p=1
        else:
            p=0
        lis.append(p)
    nos=sum(lis)
    lis=[]
    lisb.append(nos)
print(sum(lisb)/100000)
plt.hist(lisb)
plt.show()
