import random

def roll(n, seed):
    random.seed(seed)
    return [random.randint(1, 6) for _ in range(n)]
