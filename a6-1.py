import sys

fn = "p6.txt" if len(sys.argv) < 2 else sys.argv[1]

with open(fn) as data:
    for line in data:
        line = line.strip()
        w = len(line)
        for i in range(0,w+1):
            if len(set(line[i:i+4])) == 4:
                print(line[i:i+4])
                print(i+4)
                break
