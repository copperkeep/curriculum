def shout_short(words):
    return [w.upper() for w in words if len(w) <= 3]
