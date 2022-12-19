#coding: utf-8

import json

def compare(x, y):
    if type(x) == int and type(y) == int:
        if x < y:
            return -1
        elif x == y:
            return 0
        return 1
    elif type(x) == list and type(y) == list:
        i = 0
        for i in range(min(len(x), len(y))):
            cmp = compare(x[i], y[i])
            if cmp != 0:
                return cmp
        lx, ly = len(x), len(y)
        if lx < ly:
            return -1
        elif lx == ly:
            return 0
        return 1
    else:
        if type(x) == int:
            return compare([x], y)
        return compare(x, [y])


def main():
    right = []
    result = []
    with open("input.txt") as fd:
        pair = []
        n = 0
        for line in fd:
            line = line.strip()
            if not line:
                continue

            pair.append(json.loads(line))
            if len(pair) < 2:
                continue

            n += 1
            print(n, pair)
            if compare(pair[0], pair[1]) == -1:
                result.append(n)

            pair = pair[:0]
    print(result)
    print(sum(result))


main()
