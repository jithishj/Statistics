import matplotlib.pyplot as plt
lis=[]
lisb=[]
p=0
for num in range(10000):#Repeating the experiment 10000 times
    for val in range(10): #Tossing 10 times is the experiment
        k=np.random.random()
        if k >.5:
            p=1
        else:
            p=0
        lis.append(p)
    nos=sum(lis)
    lis=[]
    lisb.append(nos)
print(sum(lisb)/100000) #Probility of getting a head
plt.hist(lisb)
plt.show()
