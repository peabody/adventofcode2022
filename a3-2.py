priorities = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,53)))

with open('p3.txt') as data:
    priority_total = 0
    lines = data.readlines()
    for i,x in enumerate(range(3,len(lines)+1,3)):
        group = [l.strip() for l in lines[i*3:x]]
        item = set(group[0]) & set(group[1]) & set(group[2])
        item = item.pop()
        priority_total += priorities[item]
    print(priority_total)
