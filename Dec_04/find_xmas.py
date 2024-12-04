import os
path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "input")

with open(file_path, 'r') as reader:
    grid = [line.rstrip('\n') for line in reader]

MAX_X = len(grid) 
MAX_Y = len(grid[0])

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

def is_xmas(grid: list, x: int, y: int, dx: int, dy: int) -> bool:
    if not ((0 <= x + 3 * dx < MAX_X) and (0 <= y + 3 * dy < MAX_Y)):
        return False
    
    return (grid[x + dx][y + dy] == 'M') and (grid[x + 2 * dx][y + 2 * dy] == 'A') and (grid[x + 3 * dx][y + 3 * dy] == 'S')

xmas_count = 0
for x in range(MAX_X):
    for y in range(MAX_Y):
        current = grid[x][y]
        if current == 'X':
            for dx, dy in dirs:
                if is_xmas(grid, x, y, dx, dy):
                    xmas_count += 1
print(xmas_count)