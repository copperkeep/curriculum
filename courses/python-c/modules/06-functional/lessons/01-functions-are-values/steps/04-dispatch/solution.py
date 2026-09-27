def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

OPS = {"+": add, "-": sub, "*": mul}

def calc(op, a, b):
    if op not in OPS:
        raise ValueError(f"unknown op {op}")
    return OPS[op](a, b)
