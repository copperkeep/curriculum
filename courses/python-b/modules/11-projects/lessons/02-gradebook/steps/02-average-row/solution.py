def row_average(row):
    scores = []
    for key, value in row.items():
        if key == "name":
            continue
        try:
            scores.append(float(value))
        except ValueError:
            pass
    if not scores:
        return None
    return sum(scores) / len(scores)
