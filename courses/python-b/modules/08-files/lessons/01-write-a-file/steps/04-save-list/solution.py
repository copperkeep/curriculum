def save(items, path):
    with open(path, "w") as f:
        for item in items:
            f.write(item + "\n")
