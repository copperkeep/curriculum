def first_repeat(xs):
    seen = set()
    for x in xs:
        if x in seen:
            return x
        seen.add(x)
    return None
