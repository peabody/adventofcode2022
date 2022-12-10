with open("p1.txt") as data:
    cur_total = 0
    max_cals = 0
    for line in data:
        if line.strip():
            cur_total += int(line)
        else:
            if cur_total > max_cals:
                max_cals = cur_total
            cur_total = 0
    print(max_cals)
