import sys
import pprint

fn = "p11.txt" if len(sys.argv) < 2 else sys.argv[1]

monkeys = []

class Monkey:
    def __init__(self, data):
        """Build the monkey"""
        # data is lines
        # line one is monkey number:
        self.id = int(data[0].split()[1].rstrip(':'))
        self.items = [int(x.strip()) for x in data[1].split(':')[1].split(',')]
        self.op = data[2].split('=')[1].split()
        self.test = int(data[3].split()[-1])
        self.test_true = int(data[4].split()[-1])
        self.test_false = int(data[5].split()[-1])
        self.total_inspects = 0

    def catch(self, item):
        self.items.append(item)

    def operation(self):
        new = 0
        old = self.items[0]
        operand = 0
        if self.op[2] == 'old':
            operand = old
        else:
            operand = int(self.op[2])
        if self.op[1] == '+':
            new = old + operand
        elif self.op[1] == '*':
            new = old * operand

        self.items[0] = new

    def inspect(self, monks):
        if self.items:
            self.total_inspects += 1
            self.operation()
            self.items[0] = self.items[0] // 3
            self.test_monkey(monks)
            return True
        else:
            return False

    def test_monkey(self, monks):
        if (self.items[0] % self.test) == 0:
            monks[self.test_true].catch(self.items.pop(0))
        else:
            monks[self.test_false].catch(self.items.pop(0))

    def __str__(self):
        return """
        Monkey: %d
        Items: %s
        Operation: %s
        Test: %d
        Test_true: %d
        Test_false: %d
        """ % (self.id, self.items, self.op, self.test, self.test_true, self.test_false)


with open(fn) as data:
    current_monkey = []
    for line in data:
        if line != '\n':
            current_monkey.append(line)
        else:
            monk = Monkey(current_monkey)
            monkeys.append(monk)
            current_monkey = []
    

for monk in monkeys:
    print(monk)

print('=====================================================')

# We have the monkeys now play the rounds

for round in range(0,20):
    for monk in monkeys:
        while monk.inspect(monkeys):
            pass

    print("Round %d" % round)
    for monk in monkeys:
        print(monk)

# look at total inspections
monkeys.sort(key=lambda x: x.total_inspects, reverse=True)

for monk in monkeys: print(monk)
print(monkeys[0].total_inspects * monkeys[1].total_inspects)