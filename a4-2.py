import sys

fn = "p4.txt" if len(sys.argv) < 2 else sys.argv[1]

def check(p1, p2):
    return set(range(p1[0],p1[1]+1)) & set(range(p2[0],p2[1]+1))

def check2(p1,p2):
    return (p1[1] >= p2[0] and p1[0] <= p2[0])  or \
           (p2[1] >= p1[0] and p2[0] <= p1[0])

total_pairs = 0

with open(fn) as data:
    for line in data:
        pair = line.strip().split(',')
        pair = [x.split('-') for x in pair]
        pair = [(int(x),int(y)) for x,y in pair]
        if check2(pair[0], pair[1]):
            print(pair)
            total_pairs += 1

print(total_pairs)

        
