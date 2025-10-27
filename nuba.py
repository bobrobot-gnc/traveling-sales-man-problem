from numba import njit
import numpy as np
import timeit
nsamples=10000000
@njit
def monte_carlo_pi(nsamples):
    acc = 0
    np.random.seed(1)
    for i in range(nsamples):
        x = np.random.random()
        y = np.random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples
t1=timeit.timeit(lambda: monte_carlo_pi(nsamples), number=1)
t2=timeit.timeit(lambda: monte_carlo_pi.py_func(nsamples), number=1)
print(t1)
print(t2)