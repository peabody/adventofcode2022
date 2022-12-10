import sys

board = []

stacks = [
    
]

fn = "p5.txt" if len(sys.argv) < 2 else sys.argv[1]

with open(fn) as data:
    # parse the board
    for line in data:
        if line.strip():
            board.append(line)
        else:
            break

    # make thr stacks
    cols = len(board[-1].split())
    rows = len(board) - 1
    stacks = [[] for x in range(0,cols)]
    for col in range(0,cols):
        j = (4*col) + 1
        for i in range(0,rows):
            box = board[i][j]
            if box.strip():
                stacks[col].insert(0,box)

    for line in data:
        line = line.split()
        amount, start, end = list(map(int, [line[1], line[3], line[5]]))
        for x in range(0,amount):
            stacks[end-1].append(stacks[start-1].pop())

    print(stacks)

    for each_stack in stacks:
        print(each_stack[-1], end="")
    print()

