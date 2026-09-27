import csv

def total_amount(path):
    total = 0
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            total = total + float(row["amount"])
    return total
