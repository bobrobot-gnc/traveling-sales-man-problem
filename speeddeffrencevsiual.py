import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from numba import njit
import timeit

n = 100
x = np.zeros(n)
y = np.zeros(n)
T = np.zeros(n)
x[0] = 0
y[0] = 0
score = 0
scorefirst = 0

for i in range(1, n):
    T[i] = i
    x[i] = np.random.random()
    y[i] = np.random.random()
    scorefirst += sqrt((x[i-1]-x[i])**2 + (y[i]-y[i-1])**2)

print(scorefirst)

@njit
def permutation_numba(n, T, iterations, x, y, score, scorefirst):
    for s in range(iterations):
        score = 0
        i = np.random.randint(n)
        j = np.random.randint(n)
        T[i], T[j] = T[j], T[i]
        for k in range(n - 1):
            a = int(T[k])
            b = int(T[k + 1])
            score += sqrt((x[a] - x[b])**2 + (y[a] - y[b])**2)
        if score > scorefirst:
            T[i], T[j] = T[j], T[i]
        else:
            scorefirst = score
    return T, scorefirst

# Warm up numba JIT (first run compiles)
permutation_numba(n, T, 10, x, y, score, scorefirst)

# Measure Numba vs pure Python times
# t1 = timeit.timeit(lambda: permutation_numba(n, T, 1000000, x, y, score, scorefirst), number=1)
# t2 = timeit.timeit(lambda: permutation_numba.py_func(n, T, 1000000, x, y, score, scorefirst), number=1)

# print("Numba time:", t1)
# print("Python time:", t2)

# --- Live plot comparison ---
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, max(0.5, 100) * 1.2)
bars = ax.bar([0.5, 1.5], [0, 0], width=0.3, color=['orange', 'gray'])
ax.set_xticks([0.5, 1.5])
ax.set_xticklabels(['Numba', 'Python'])
ax.set_ylabel('Execution time (s)')
ax.set_title("Performance Comparison")

# Animate the bar filling
steps = 30
for step in range(steps + 1):
    bars[0].set_height(t1 * step / steps)
    bars[1].set_height(t2 * step / steps)
    plt.pause(0.02)

ax.set_title(f"Numba {t2 / t1:.1f}× faster")
plt.pause(2)
plt.ioff()
plt.show()
