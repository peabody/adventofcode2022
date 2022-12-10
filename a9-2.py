import sys
import pprint

fn = "p9.txt" if len(sys.argv) < 2 else sys.argv[1]

NUM_KNOTS = 10

knots = [[0,0] for x in range(0,NUM_KNOTS)]
visited = set()
dv = []

def move_tail(head,tail):
    # if adjacent, or overlapping,
    # do nothing
    #if head == tail:
    #    visited.add(tuple(tail))
    #    dv.append(tuple(tail))
    #    return
    if abs(head[0] - tail[0]) <= 1 and \
        abs(head[1] - tail[1]) <= 1:
            pass
    # else determine direction to move
    # if in same row, more toward heqf
    elif head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1

    elif head[1] == tail[1]:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1

    # else move diagonally
    else:
        i = head[0] - tail[0]
        i = i//abs(i)
        j = head[1] - tail[1]
        j = j//abs(j)

        tail[0] += i
        tail[1] += j
    
def move_head(line):
    head = knots[0]
    direction, amt = line.split()
    amt = int(amt)
    for x in range(0,amt):
        if direction == 'L':
            head[1] -= 1
        elif direction == 'U':
            head[0] -= 1
        elif direction == 'R':
            head[1] += 1
        elif direction == 'D':
             head[0] += 1
        for i in range(0,NUM_KNOTS-1):
            move_tail(knots[i],knots[i+1])
        visited.add(tuple(knots[-1]))

with open(fn) as data:
    for line in data:
        move_head(line)

pprint.pprint(visited)
#pprint.pprint(dv)
print(len(visited))
