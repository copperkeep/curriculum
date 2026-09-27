def count_lines(path):
    count = 0
    with open(path) as f:
        for line in f:
            if line.strip():
                count = count + 1
    return count
