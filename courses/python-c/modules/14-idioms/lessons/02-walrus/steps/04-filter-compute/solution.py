def long_upper(words):
    return [s.upper() for w in words if len(s := w.strip()) > 3]
