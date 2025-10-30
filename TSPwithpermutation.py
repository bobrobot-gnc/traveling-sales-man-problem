#this code is a brute force solutiob by random permutation for the traveling sales man problem with live plotatation u can use this code directly after installing the necessery library 
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

n=100 # the number of points u want to generate randomly and search for the minimum route to go through all the points the algorithm is of the O(n2) complexity therea alot of ways to optimize this but we started with this
x=np.zeros(n)
y=np.zeros(n)
T=np.zeros(n)
x[0]=0
y[0]=0
score=0
scorefirst =0
#below is the generation loop for random points 
for i in range(1,n):
   T[i] = i
   x[i]=np.random.random()
   y[i]=np.random.random()
   scorefirst=scorefirst+sqrt((x[i-1]-x[i])**2+(y[i]-y[i-1])**2)

plt.ion()
fig, ax = plt.subplots()
#this is the nested loop to permute the point randomly this does not gareunte the optimal route but the more brute force the more close and sure u get
for s in range(900): # the number of iteration u allow the loop to go to before stopping or how much brute force are u allowing this can depend on many factors
    score=0
    i=np.random.randint(n)
    j=np.random.randint(n)
    T[i],T[j]=T[j],T[i] # this line if for two elemts in the order vector permutation i think this is the best way to do it
   
    for k in range(n-1):
        a=int(T[k])
        b=int(T[k+1])
        score=score+sqrt((x[a]-x[b])**2+(y[a]-y[b])**2)
    if score>scorefirst:
        T[i], T[j] = T[j], T[i] # if the permutation doesnt optimize the the score we simply reject it
    else:
        scorefirst=score
    ax.clear()
    ax.plot(x[T.astype(int)], y[T.astype(int)], '-o', markersize=4)
    ax.set_title(f"Iteration {s}, Score = {scorefirst:.3f}")
    plt.pause(0.1)



plt.ioff()
plt.show()
