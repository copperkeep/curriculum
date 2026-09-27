# This is correct but far too slow for fib(80). Make it fast without changing
# the body.
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
