def perms(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i, ch in enumerate(s):
        for rest in perms(s[:i] + s[i + 1:]):
            result.append(ch + rest)
    return result
