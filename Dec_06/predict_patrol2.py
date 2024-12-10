input = []
with open('input', 'r') as f:
    for line in f:
        input.append([char for char in line[:-1]])


def guard_route(lab, guard_pos):
    path = {}
    direction = (-1, 0)
    while True:
        if guard_pos not in path: path[guard_pos] = [direction]
        elif direction in path[guard_pos]: return "loop"
        else: path[guard_pos].append(direction)


        if not (0 <= guard_pos[0] + direction[0] < len(lab) and 0 <= guard_pos[1] + direction[1] < len(lab[0])):
            return path
        if lab[guard_pos[0]+direction[0]][guard_pos[1]+direction[1]] != '#':
            guard_pos = guard_pos[0]+direction[0], guard_pos[1]+direction[1]
        else:
            direction = direction[1], -direction[0]

for i, line in enumerate(input):
    for j, char in enumerate(line):
        if char == "^":
            guard = i, j

route = guard_route(input, guard)

loops = 0
for path_pos in route:
    if path_pos != guard:
        obstructed_route = [[char for char in line] for line in input]
        obstructed_route[path_pos[0]][path_pos[1]] = '#'
        if guard_route(obstructed_route, guard) == "loop":
            loops += 1


print(f"The guard moves over {len(route)} fields until she moves off the map")
print(f"There are {loops} possible loops by obstruction to get past the guard")
