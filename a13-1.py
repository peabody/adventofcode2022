import sys
import pprint

fn = "p13.txt" if len(sys.argv) < 2 else sys.argv[0]

data = []

lines = []

with open(fn) as fin:
    lines = fin.readlines()

for i in range(0,len(lines),3):
    try:
        line1 = eval(lines[i])
        line2 = eval(lines[i+1])
        data.append([line1,line2])
    except SyntaxError:
        print("Bad lines:")
        print("line1:", lines[i], "line2:", lines[i+1])
        input()

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
    

total_in_order = 0
for i,(p1,p2) in enumerate(data):
    test = check(p1,p2)
    if test > 0:
        total_in_order += i + 1

print(total_in_order)