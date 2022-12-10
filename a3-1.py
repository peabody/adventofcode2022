priorities = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,53)))

with open('p3.txt') as data:
    priority_total = 0
    for line in data:
        line = line.strip()
        l = len(line)//2
        half1 = set(line[:l])
        half2 = set(line[l:])
        item = (half1 & half2).pop()
        priority_total += priorities[item]
    print(priority_total)
