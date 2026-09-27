def root(x):
    if x < 0:
        raise ValueError("negative")
    return x ** 0.5

try:
    root(-1)
except ValueError as e:
    print("no:", e)
