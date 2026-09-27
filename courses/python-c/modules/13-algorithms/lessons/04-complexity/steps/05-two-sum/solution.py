def two_sum(xs, target):
    seen = {}
    for j, x in enumerate(xs):
        if target - x in seen:
            return seen[target - x], j
        seen[x] = j
    return None
