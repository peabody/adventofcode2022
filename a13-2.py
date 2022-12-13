import sys
import pprint
import functools

fn = "p13.txt" if len(sys.argv) < 2 else sys.argv[0]

lines = []

with open(fn) as fin:
    for line in fin:
        if line.strip():
            lines.append(eval(line))

# divider packets
lines.append([[2]])
lines.append([[6]])

def get(p,i):
    try:
        return p[i]
    except IndexError:
        return None

def check(packet1, packet2):
    if type(packet1) == int and type(packet2) == int:
        return packet2 - packet1
    elif type(packet1) == list and type(packet2) == list:
        for i in range(max(len(packet1), len(packet2))):
            test_val1 = get(packet1, i)
            test_val2 = get(packet2, i)         
            if test_val1 == None:
                return 1
            if test_val2 == None:
                return -1
            test = check(test_val1, test_val2)
            if test != 0:
                # prematurely end loop
                return test
        # return 0 in case lists were exact
        return 0
    elif (type(packet1) == list and type(packet2) == int):
        packet2 = [packet2]
        return check(packet1, packet2)
    elif (type(packet2) == list and type(packet1) == int):
        packet1 = [packet1]
        return check(packet1, packet2)

lines.sort(key=functools.cmp_to_key(check), reverse=True)

key1 = None
key2 = None
for i in range(len(lines)):
    if [[2]] == lines[i]:
        key1 = i + 1
    elif [[6]] == lines[i]:
        key2 = i + 1

print("Decoder key %d" % (key1 * key2))