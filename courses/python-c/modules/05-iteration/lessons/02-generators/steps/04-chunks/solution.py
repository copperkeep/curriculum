def chunks(xs, size):
    for i in range(0, len(xs), size):
        yield xs[i:i + size]
