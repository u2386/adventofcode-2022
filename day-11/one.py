#coding: utf-8

import heapq

monkeys = []


class Monkey:

    def __init__(self, num, items):
        self.num = num
        self.items = items
        self.operation = lambda x: x
        self.test = lambda x: x
        self.nexts = []
        self.activities = 0

    def inspect(self):
        self.activities += len(self.items)
        for item in self.items:
            t = item
            item = self.operation(item)
            item = item // 3
            if self.test(item):
                monkeys[self.nexts[0]].items.append(item)
            else:
                monkeys[self.nexts[1]].items.append(item)
        self.items = []

    def __str__(self):
        return "Monkey#%s<%s>" % (self.num, self.items)

    __repr__ = __str__


def test_func(v):
    return lambda x: x % v == 0

def operation_func(op, z):
    if op == "*":
        if z == "old":
            return lambda x: x * x
        else:
            return lambda x: x * int(z)
    elif op == "+":
        if z == "old":
            return lambda x: x + x
        else:
            return lambda x: x + int(z)


def main():
    with open("input.txt") as fd:
        for line in fd:
            line = line.strip()

            if line.startswith("Monkey"):
                (_, num) = line[:-1].split(" ")
                monkey = Monkey(num, [])
                monkeys.append(monkey)

            elif line.startswith("Starting"):
                items = line[line.find(":")+1:].split(", ")

                monkey = monkeys[-1]
                monkey.items = [int(i) for i in items]

            elif line.startswith("Operation"):
                (_, op, z) = line[len("Operation: new = "):].split(" ")

                monkey = monkeys[-1]
                monkey.operation = operation_func(op, z)

            elif line.startswith("Test"):
                v = int(line[len("Test: divisible by "):])

                monkey = monkeys[-1]
                monkey.test = test_func(v)

            elif line.startswith("If"):
                num = line[-1]

                monkey = monkeys[-1]
                monkey.nexts.append(int(num))

    print("starting")
    print(monkeys)
    for r in range(20):
        for monkey in monkeys:
            monkey.inspect()
        print("round:", r)
        print(monkeys)


    h = [0, 0]
    for monkey in monkeys:
        heapq.heappushpop(h, monkey.activities)
    print(h[0]*h[1])

main()
