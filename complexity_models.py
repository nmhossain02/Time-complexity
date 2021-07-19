# pylint: disable=W,C

import math

def exp(x, a, b):
    return [a * math.exp(i * b) for i in x]

def lin(x, a, b):
    return [a * i + b for i in x]

def log(x, a, b):
    return [a + b * math.log(i) for i in x]