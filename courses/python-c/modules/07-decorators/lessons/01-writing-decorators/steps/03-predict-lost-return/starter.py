def noisy(func):
    def wrapper(*args):
        func(*args)
    return wrapper

@noisy
def add(a, b):
    return a + b

print(add(2, 3))
