def dot(xs, ys):
    total = 0
    for x, y in zip(xs, ys):
        total = total + x * y
    return total
