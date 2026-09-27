from functools import reduce

def product(xs):
    return reduce(lambda acc, x: acc * x, xs, 1)
