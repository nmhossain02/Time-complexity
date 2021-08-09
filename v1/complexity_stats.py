# pylint: disable=C,r

import time
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# single variable complexity
def FindComplexity(func, args):
    t = []
    for arg in args:
        current_t = time.perf_counter()
        func(arg)
        t.append((time.perf_counter() - current_t))

    # outlier dropping
    prev_len = len(args)
    data = zip(args, t)
    q1, q3 = np.percentile(t, [25, 75])
    iqr = q3 - q1
    k = 1.5
    data = filter(lambda n: q1 - k * iqr <= n[1] <= q3 + k * iqr, data)
    args, t = zip(*data)

    # plot values
    plt.plot(args, t)
    plt.savefig("plot.png")
    plt.show(block=False)

    d = {}
    d['lin'] = linregress(args, t) # y => n >>> y => [x]
    d['exp'] = linregress([math.log(i + 1) for i in args], t) # y => e^n >>> [y] => ln x
    d['log'] = linregress(args, [math.log(i) for i in t]) # y => ln n >>> ln y => [x]
    d['nln'] = linregress(args, [i * math.log(i) for i in t]) # y => n ln n >>> y ln y => [x]
    d['qdt'] = linregress([i ** 0.5 for i in args], t) # y => n^2 >>> [y] => x^(0.5)

    # find entry in d with highest val.rvalue
    r = 0
    method = 'nan'
    for key in d:
        rval = abs(d[key].rvalue)
        if rval > r:
            r = rval
            method = key

    out = {}
    out['outliers'] = prev_len - len(args)
    for key in d:
        out[key] = (d[key].rvalue)

    out['BEST'] = method
    return out

def Count(n):
    out = 0
    for i in range(n):
        out += 1
        # print(out)
    return out

inrange = range(300)

d = FindComplexity(Count, inrange)

for (key, value) in d.items():
    print (f"{key}: {value}")
plt.show()