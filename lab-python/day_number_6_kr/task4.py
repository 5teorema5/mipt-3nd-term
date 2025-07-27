grid = []
for i in range(3):
    grid.extend(list(input()))

if grid[0] == grid[1] == grid[2] != '.':
    print(grid[0])
elif grid[3] == grid[4] == grid[5] != '.':
    print(grid[3])
elif grid[6] == grid[7] == grid[8] != '.':
    print(grid[6])
elif grid[0] == grid[3] == grid[6] != '.':
    print(grid[0])
elif grid[1] == grid[4] == grid[7] != '.':
    print(grid[1])
elif grid[2] == grid[5] == grid[8] != '.':
    print(grid[2])
elif grid[0] == grid[4] == grid[8] != '.':
    print(grid[0])
elif grid[2] == grid[4] == grid[6] != '.':
    print(grid[2])
else:
    print('?')
