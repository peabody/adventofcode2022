with open("p1.txt") as data:
    cur_total = 0
    elves = []
    for line in data:
        if line.strip():
            cur_total += int(line)
        else:
            elves.append(cur_total)
            cur_total = 0
    elves.sort()
    print(sum(elves[-3:]))
