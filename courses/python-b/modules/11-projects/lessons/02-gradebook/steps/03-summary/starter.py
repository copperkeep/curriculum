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

# Write summarise(csv_path, json_path) that reads the gradebook, and writes a
# JSON object mapping each name to their average rounded to 1 decimal place
# (or null if they have no valid scores). Return the dict too.
