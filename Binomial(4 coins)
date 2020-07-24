#Find the probability of getting all heads in tossing 4 fair coins
c=0
for num in range(10000): #Repeating 10000 times
    s=0 #sum of 4 tosses
    a=np.random.random(4) #4 tosses
    p=.5 #if p>.5 its a head
    s=sum(a>p)
    if s==4: #All tosses leading to heads mean sum=4
        c+=1
print(f'The probability of success is {c/10000}')
