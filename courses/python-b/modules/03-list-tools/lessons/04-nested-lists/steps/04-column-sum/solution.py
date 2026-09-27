def column_sum(grid, c):
    total = 0
    for row in grid:
        total = total + row[c]
    return total
