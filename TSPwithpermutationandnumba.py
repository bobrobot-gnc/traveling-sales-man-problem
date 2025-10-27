
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from numba import njit
import timeit
n=900
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
print(scorefirst)
scorefirstcopy=scorefirst
plt.plot(x,y)
plt.show()
@njit
def permutation_numba(n,T,iterations,x,y,score,scorefirst):

    for s in range(iterations):
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
    return T,scorefirst

# t1=timeit.timeit(lambda: permutation_numba(n,T,1000000,x,y,score,scorefirst),number=1)
# t2=timeit.timeit(lambda: permutation_numba.py_func(n,T,10000,x,y,score,scorefirst),number=1)
# print(t1)
# print(t2)
Tc=T.copy()
scorecopy=0
T,scorefirst=permutation_numba(n,T,100000000,x,y,score,scorefirst)
# Tfunc,scorefirstfunc=permutation_numba.py_func(n,Tc,100000,x,y,scorecopy,scorefirstcopy)

print(scorefirst)

plt.plot(x[T.astype(int)], y[T.astype(int)], '-o', markersize=4)
plt.show()