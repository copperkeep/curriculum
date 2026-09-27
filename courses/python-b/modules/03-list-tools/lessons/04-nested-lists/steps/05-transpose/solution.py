def transpose(grid):
    result = []
    for c in range(len(grid[0])):
        new_row = []
        for row in grid:
            new_row.append(row[c])
        result.append(new_row)
    return result
