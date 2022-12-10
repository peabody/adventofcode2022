import sys
import pprint

fn = "p7.txt" if len(sys.argv) < 2 else sys.argv[1]

root = {}
cwd = root

lines = open(fn).readlines()

i = 0
while i < len(lines):
    line = lines[i]
    line = line.rstrip()
    print(line)
    if '/' in line:
        pwd = []
        cwd = root
        i += 1
        continue
    if '$ ls' in line:
        j = 0
        for next_lines in lines[i+1:]:
            next_lines = next_lines.rstrip()
            print(next_lines)
            if next_lines.startswith('$'): break
            j += 1
            data, name = next_lines.split()
            if data == 'dir':
                cwd.setdefault(name, {'..': cwd})
            else:
                cwd[name] = int(data)
        i += j
    elif '$ cd' in line:
        _, __, f = line.split()
        if f == '..':
            pwd.pop()
            cwd = cwd['..']
        else:
            pwd.append(f)
            cwd = cwd[f]

    i += 1

pprint.pprint(root)

totals = {}
pwd = []

def df(folder):
    total = 0
    f_name = tuple(pwd)
    for key in folder:
        if key == '..': continue
        if type(folder[key]) == dict:
            pwd.append(key)
            sub_tot = df(folder[key])
            totals.setdefault(f_name, 0)
            totals[f_name] += sub_tot
            total += sub_tot
            pwd.pop()
        else:
            totals.setdefault(f_name, 0)
            totals[f_name] += folder[key]
            total += folder[key]
    return total

df(root)
pprint.pprint(totals)

final_sum = 0
for key in totals:
    if totals[key] <= 100000:
        final_sum += totals[key]

print(final_sum)
