def merge(a, b):
    result = sorted(a + b)
    assert len(result) == len(a) + len(b), "lost items"
    return result
