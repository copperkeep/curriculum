def load(path):
    with open(path) as f:
        return [line.strip() for line in f]
