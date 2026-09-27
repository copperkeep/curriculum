import copy
grid = [[1, 2], [3, 4]]
dup = copy.deepcopy(grid)
dup[0][0] = 9
print(grid)
