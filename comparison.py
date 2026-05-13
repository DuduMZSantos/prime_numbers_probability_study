from prime_funcs import naive_method, optimized_method
from time import time
import matplotlib.pyplot as plt

naive = []
optimized = []
probs = []
x = range(2, 5001)
for n in x:
    beg = time()
    naive_method(n)
    naive.append(time()-beg)
    beg = time()
    prob = optimized_method(n)
    optimized.append(time()-beg)
    probs.append(prob)

fig, ax = plt.subplots(2,2)
ax[0,0].plot(x, naive)
ax[0,0].set_title("Naive Implementation")
ax[0,1].plot(x, optimized)
ax[0,1].set_title("Optimized Implementation")
ax[1,0].plot(x, naive, label="Naive")
ax[1,0].plot(x, optimized, label="Optimized")
ax[1,0].set_title("Naive vs Optimized Implementations")
ax[1,0].legend()
ax[1,1].plot(x, probs)
ax[1,1].set_title("Probabilities function")
plt.show()