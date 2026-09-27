def memoize(f):
    cache = {}
    def wrapper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return wrapper
