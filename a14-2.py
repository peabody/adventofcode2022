import sys
from pprint import pprint
from itertools import pairwise

fn = "p14.txt" if len(sys.argv) < 2 else sys.argv[1]

coords = set()
line_segs = set()
with open(fn) as fin:
    for line in fin:
        points = [x.strip() for x in line.split('->')]
        points = [x.split(',') for x in points]
        points = tuple((int(x),int(y)) for x,y in points)
        line_segs.add(points)
        coords.update(points)

max_x = max(coords)[0]
max_y = max(coords, key=lambda x: x[1])[1]
min_x = min(coords)[0]
min_y = min(coords, key=lambda x: x[1])[1]

floor = max_y + 2

# adjusting to sufficiently large value to accommodate an infinite floor
min_x = (min_x - 200000)
max_x = (max_x + 200000)

# make as large as necessary for the solution?
grid = [ ['.' for x in range(max_x - min_x + 1)] for x in range(floor + 1) ]

# draw floor
for x in range(len(grid[0])):
    grid[-1][x] = '#'

# fill line segments into grid
for line in line_segs:
    # normalize x by subtracting min_x
    for a,b in pairwise(line):
        a = (a[0] - min_x, a[1])
        b = (b[0] - min_x, b[1])
        # loop by coordinate that changes
        if a[0] == b[0]:
            # x is same, loop by y
            x = a[0]
            top_y = max([a[1],b[1]])
            bottom_y = min([a[1],b[1]])
            for y in range(bottom_y,top_y+1):
                grid[y][x] = '#'
        else:
            # assume y is same, loop by x
            y = a[1]
            top_x = max([a[0],b[0]])
            bottom_x = min([a[0],b[0]])
            for x in range(bottom_x,top_x+1):
                grid[y][x] = '#'


def print_board():
    for line in grid:
        print(''.join(line))


def check_sand(sand):
    x,y = sand
    inbounds_y = y < len(grid)
    inbounds_x1 = (x - 1) > -1
    inbounds_x2 = (x + 1) < len(grid[0])
    if not inbounds_y:
        return "Gone"
    if grid[y][x] == '.':
        return [x,y]
    if not inbounds_x1:
        return "Gone"
    if grid[y][x - 1] == '.':
        return [x - 1,y]
    if not inbounds_x2:
        return "Gone"
    if grid[y][x + 1] == '.':
        return [x + 1,y]
    return "Stop"


# simulate sand
total_sand = 0
sand_gone = False
while True:
    if sand_gone:
        break
    sand = [500 - min_x,0]
    while True:
        # move sand down and check
        sand[1] += 1
        result = check_sand(sand)
        if result == "Gone":
            sand_gone = True
            break
        elif result == "Stop":
            total_sand += 1
            sand[1] -= 1
            x,y = sand
            grid[y][x] = 'o'
            sand_gone = sand == [500 - min_x,0]
            break
        else:
            sand = result

# board's a bit too big to print now
#print_board()
print(total_sand)
        
