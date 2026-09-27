def rotate(xs, n):
    if not xs:
        return []
    n = n % len(xs)
    return xs[n:] + xs[:n]
