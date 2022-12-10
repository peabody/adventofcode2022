import sys
import pdb

width = 40
height = 6

screen = [
    list('........................................'),
    list('........................................'),
    list('........................................'),
    list('........................................'),
    list('........................................'),
    list('........................................'),
]

fn = "p10.txt" if len(sys.argv) < 2 else sys.argv[1]

X = 1

stack = []

def process_stack():
    global X
    if stack:
        X += stack.pop(0)

def draw_pixel(cycle):
    # existing bug, not filling in first pixel?
    # all other pixels accurate
    global screen, X
    row = (cycle // width) % height
    col = (cycle % width)
    #pdb.set_trace()
    if col == X or col == (X - 1) or col == (X + 1):
        screen[row][col] = '#'
    else:
        screen[row][col] = '.'

with open(fn) as data:
    cycle = 0
    while True:
        cycle += 1
        # if pending instruction
        # process and don't read
        if stack:
            process_stack()
            draw_pixel(cycle)
            continue
        line = data.readline()
        # if end of file stop
        if not line: break
        # if noop is read do nothing but spend one cycle
        if 'noop' in line:
            pass

        # if addx is read, put operation on stack
        elif 'addx' in line:
            _, amt = line.split()
            amt = int(amt)
            stack.append(amt)

        draw_pixel(cycle)

for row in screen:
    print(''.join(row))

