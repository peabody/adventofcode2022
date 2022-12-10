import sys

fn = "p6.txt" if len(sys.argv) < 2 else sys.argv[1]

with open(fn) as data:
    for line in data:
        line = line.strip()
        w = len(line)
        must_break = False
        for i in range(0,w+1):
            if len(set(line[i:i+4])) == 4:
                for j in range(i,w+1):
                    if len(set(line[j:j+14])) == 14:
                        print(j+14)
                        must_break = True
                        break
                if must_break:
                    must_break = False
                    break
