import sys

fn = "p4.txt" if len(sys.argv) < 2 else sys.argv[1]

def check(p1, p2):
    return (p1[0] <= p2[0] and p1[1] >= p2[1])

total_pairs = 0

with open(fn) as data:
    for line in data:
        pair = line.strip().split(',')
        pair = [x.split('-') for x in pair]
        pair = [(int(x),int(y)) for x,y in pair]
        if check(pair[0], pair[1]) or check(pair[1], pair[0]):
            print(pair)
            total_pairs += 1

print(total_pairs)

        
