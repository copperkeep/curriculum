import csv, json

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

def summarise(csv_path, json_path):
    summary = {}
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            avg = row_average(row)
            summary[row["name"]] = None if avg is None else round(avg, 1)
    with open(json_path, "w") as f:
        json.dump(summary, f)
    return summary
