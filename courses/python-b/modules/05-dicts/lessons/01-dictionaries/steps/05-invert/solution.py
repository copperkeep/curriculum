def invert(d):
    result = {}
    for key in d:
        result[d[key]] = key
    return result
