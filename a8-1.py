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
# check if current grid is max
# of both the column and the row

total_visible = 0
for i in range(1,rows-1):
    for j in range(1,cols-1):
        tree = grid[i][j]
        #max_right = grid[i][j+1]
        #max_left = grid[i][j-1]
        #max_up = grid[i-1][j]
        #max_down = grid[i+1][j]
        max_right = max(grid[i][j+1:])
        max_left = max(grid[i][:j])
        max_up = max([grid[y][j] for y in range(0,i)])
        max_down = max([grid[y][j] for y in range(i+1,rows)])
        #print(tree, max_right, max_left, max_up, max_down)
        #input()
        if (tree > max_right or tree > max_left or
            tree > max_up or tree > max_down):
            total_visible += 1

# add perimeter to total visible
total_visible += (rows*2) + (cols*2 - 4)

print(total_visible)
