
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

n=100
x=np.zeros(n)
y=np.zeros(n)
T=np.zeros(n)
x[0]=0
y[0]=0
score=0
scorefirst =0
for i in range(1,n):
   T[i] = i
   x[i]=np.random.random()
   y[i]=np.random.random()
   scorefirst=scorefirst+sqrt((x[i-1]-x[i])**2+(y[i]-y[i-1])**2)

plt.ion()
fig, ax = plt.subplots()
for s in range(900):
    score=0
    i=np.random.randint(n)
    j=np.random.randint(n)
    T[i],T[j]=T[j],T[i]
    for k in range(n-1):
        a=int(T[k])
        b=int(T[k+1])
        score=score+sqrt((x[a]-x[b])**2+(y[a]-y[b])**2)
    if score>scorefirst:
        T[i], T[j] = T[j], T[i]
    else:
        scorefirst=score
    ax.clear()
    ax.plot(x[T.astype(int)], y[T.astype(int)], '-o', markersize=4)
    ax.set_title(f"Iteration {s}, Score = {scorefirst:.3f}")
    plt.pause(0.1)



plt.ioff()
plt.show()