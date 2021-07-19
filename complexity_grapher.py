# pylint: disable=W,C

# step 1: find the performance of the algorithm in question
# step 2: analyze and fit performance to a known regression model
# step 3: find the strength of model
# step 4: repeat steps 2 and 3 with different models and choose best one


import math
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# self written
import complexity_models as models
import algorithms as alg

test_alg = alg.fib_iter
in_range = range(1000);
model = models.lin

t_arr = []
for i in in_range:
    t = time.perf_counter()
    print(f"n = {i}: {test_alg(i)}")
    t_arr.append(1000 * (time.perf_counter() - t))

# step 2
opt_pars, pcov = curve_fit(model, in_range, t_arr)
estimates = model(in_range, *opt_pars)

fig, ax = plt.subplots()
ax.set_title("Algorithm performance")
ax.set_xlabel("n-value")
ax.set_ylabel("Time in msecs")

ax.plot(in_range, estimates, label="Estimate", c="green")
ax.plot(in_range, t_arr, label="Performance")
ax.legend()

plt.savefig("testplot.png")
plt.show()
