#Binomial random variables where n=10
def bernoulli():
    p=0.5
    r=np.random.random()
    if r<p:
        return 1
    else:
        return 0
#Repeat Bernoulli 10 times
c=[]
for i in range(10):
    c.append(bernoulli())
print(c)
