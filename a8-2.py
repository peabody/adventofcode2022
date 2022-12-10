import sys

fn = "p8.txt" if len(sys.argv) < 2 else sys.argv[1]

grid = []

with open(fn) as data:
    lines = [x.rstrip() for x in data]

#allocate grid
cols = len(lines[0])
rows = len(lines)

grid = [list(lines[i]) for i in range(0,rows)]

# loop grid interior

totals = []
for i in range(1,rows-1):
    for j in range(1,cols-1):
        tree = grid[i][j]
        score_right = 0
        score_left = 0
        score_up = 0
        score_down = 0
        # right
        for tt in grid[i][j+1:]:
            score_right += 1
            if tree <= tt: break
        # left
        for tt in reversed(grid[i][:j]):
            score_left += 1
            if tree <= tt: break
        # up
        for tt in reversed([grid[y][j] for y in range(0,i)]):
            score_up += 1
            if tree <= tt: break
        # down
        for tt in [grid[y][j] for y in range(i+1,rows)]:
            score_down += 1
            if tree <= tt: break
        totals.append((score_right * score_left * score_up * score_down,i+1,j+1))

totals.sort()

print('%d %d %d' % totals[-1])
