def rank(players):
    return sorted(players, key=lambda p: (-p[1], p[0]))
