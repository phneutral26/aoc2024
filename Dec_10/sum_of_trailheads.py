def trailhead_score(trailmap, x, y):
	# floodfill to see which tiles with 9 are reachable by us
	height = len(trailmap)
	width = len(trailmap[0])
	todo = [(x, y)]
	visited = set()
	score = 0
	while todo:
		(x, y) = todo.pop(0)
		if (x, y) in visited: continue
		visited.add((x, y))
		val = trailmap[y][x]
		if val == 9: score += 1
		for (offX, offY) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
			if x+offX >= 0 and x + offX < width and y+offY >= 0 and y+offY < height and (x+offX, y+offY) not in visited and (x+offX, y+offY) not in todo:
				if trailmap[y+offY][x+offX] != val + 1: continue
				todo.append((x+offX, y+offY))
	return score

with open('input') as f:
	trailmap = [[int(c) for c in line.strip()] for line in f.readlines()]

score = 0
for y, row in enumerate(trailmap):
	for x, c in enumerate(row):
		if c==0:
			tscore = trailhead_score(trailmap, x, y)
			score += tscore
print(score)
