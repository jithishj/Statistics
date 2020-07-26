import random as rnd
import math
l=[]
ulis=[]
for i in range(10000):
    lmda = 3 # Arrival Rate
    count = 0 # Number of Arrivals
    b = math.exp(-lmda)
    u = rnd.random()
    
    while u >= b:
        count = count + 1
        u = u * rnd.random()
    l.append(count)
plt.hist(l)
plt.show()
