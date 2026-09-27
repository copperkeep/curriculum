def add_all(items):
    total = 0
    bad = 0
    for item in items:
        try:
            n = int(item)
        except ValueError:
            bad = bad + 1
        else:
            total = total + n
    return total, bad
