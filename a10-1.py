import sys

fn = "p10.txt" if len(sys.argv) < 2 else sys.argv[1]

X = 1

stack = []

def process_stack():
    global X
    if stack:
        X += stack.pop(0)

total = 0

def inc_total():
    global total, X
    if cycle in [20, 60, 100, 140, 180, 220]:
        total += X * cycle

with open(fn) as data:
    cycle = 0
    while True:
        cycle += 1
        # if pending instruction
        # process and don't read
        if stack:
            inc_total()
            process_stack()
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
        
        inc_total()

        print("cycle: %d X: %d" % (cycle, X))

print(total)

