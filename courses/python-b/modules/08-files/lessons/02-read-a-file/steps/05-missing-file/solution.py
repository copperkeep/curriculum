def read_or_default(path, default):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return default
