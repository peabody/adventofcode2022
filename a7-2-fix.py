import sys

fn = "p7.txt" if len(sys.argv) < 2 else sys.argv[1]

total_space = 70_000_000
space_needed = 30_000_000

root = {}
cwd = root


# read data
with open(fn) as fin:
    data = fin.readlines()


# outer loop for commands
for i, line in enumerate(data):
    if '$ ls' in line:
        # inner loop for file parsing
        # loop on list copy to retain
        # command in outer loop
        for next_lines in data[i+1:]:
            if next_lines.startswith('$'): break
            amt, name = next_lines.split()
            if amt == 'dir':
                cwd.setdefault(name, {'..': cwd})
            else:
                cwd[name] = int(amt)
    elif '$ cd' in line:
        _, __, f = line.split()
        if f == '/':
            cwd = root
        else:
            cwd = cwd[f]
    # else: skip file lines since they
    # were processed in above inner loop


totals = {}
pwd = []

# recusive function to calculate totals
def calculate_totals(folder):
    total = 0
    # folder path as tuple for dict keys
    f_name = tuple(pwd)
    for key in folder:
        # ignore parent
        if key == '..': continue
        # recurse folders
        if type(folder[key]) == dict:
            pwd.append(key)
            # recurse and save total
            sub_tot = calculate_totals(folder[key])
            # accumulate totals
            totals.setdefault(f_name, 0)
            totals[f_name] += sub_tot
            total += sub_tot
            pwd.pop()
        # total regular files
        else:
            totals.setdefault(f_name, 0)
            totals[f_name] += folder[key]
            total += folder[key]
    # return total to accumulate to parent call
    return total


calculate_totals(root)


remaining = total_space - totals[()]
size2del = space_needed - remaining

to_del = []

for key in totals:
    if totals[key] >= size2del:
        to_del.append((totals[key], key))

to_del.sort()
print(to_del[0])
