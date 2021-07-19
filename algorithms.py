# pylint: disable=W,C

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_array(n):
    if n == 0:
        return 0
    r = [0, 1]
    for i in range(n):
        r.append(r[-1] + r[-2])
    return r[-2]

def fib_iter(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a