def shares_rows(grid):
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            if grid[i] is grid[j]:
                return True
    return False
