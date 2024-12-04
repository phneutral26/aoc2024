import os
path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, "input")

with open(file_path, 'r') as reader:
    grid = [line.rstrip('\n') for line in reader]

MAX_X = len(grid) 
MAX_Y = len(grid[0])

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

def is_x_mas(grid: list, x: int, y: int) -> bool:
    diagonals = [
        ((-1, -1), (1, 1)),
        ((-1, 1), (1, -1))
    ]
    for diagonal in diagonals:
        new_positions = [(x + dx, y + dy) for dx, dy in diagonal]
        if not all(0 <= new_x < MAX_X and 0 <= new_y < MAX_Y for new_x, new_y in new_positions):
            return False
        
        characters = [grid[new_x][new_y] for new_x, new_y in new_positions]
        if characters.count('M') != 1 or characters.count('S') != 1:
            return False
          
    return True

x_mas_count = 0
for x in range(MAX_X):
    for y in range(MAX_Y):
        current = grid[x][y]
        if current == 'A' and is_x_mas(grid, x, y):
            x_mas_count += 1
print(x_mas_count)