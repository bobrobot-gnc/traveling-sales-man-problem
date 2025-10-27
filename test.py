from numba import njit
import numpy as np
import timeit
import scipy
n=100
a = np.zeros((n, n), dtype=np.float64)
b = np.zeros((n, n), dtype=np.float64)
np.random.seed(1)
for i in range(n):
    for j in range(n):
        a[i, j] = np.random.randint(1, 100)
        b[i, j] = np.random.randint(1, 100)
@njit
def func(a,b):
    for i in range(n):
        for j in range(n):
            a[i, j] = np.random.random()
            b[i, j] = np.random.random()
    return a@b
t1=timeit.timeit(lambda: func(a,b), number=1)
t2=timeit.timeit(lambda: func.py_func(a,b), number=1)
print('t1=%f, t2=%f' % (t1, t2))