def log(message, path):
    with open(path, "a") as f:
        f.write(message + "\n")
