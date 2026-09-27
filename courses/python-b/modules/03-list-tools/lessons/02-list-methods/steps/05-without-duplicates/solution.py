def dedupe(xs):
    result = []
    for item in xs:
        if item not in result:
            result.append(item)
    return result
