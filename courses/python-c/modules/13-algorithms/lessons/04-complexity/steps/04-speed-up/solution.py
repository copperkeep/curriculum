def common(a, b):
    b_set = set(b)
    return [x for x in a if x in b_set]
