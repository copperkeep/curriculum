def first_long(words, n):
    return next((w for w in words if len(w) > n), None)
