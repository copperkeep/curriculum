def by_length(words):
    groups = {}
    for word in words:
        n = len(word)
        if n not in groups:
            groups[n] = []
        groups[n].append(word)
    return groups
