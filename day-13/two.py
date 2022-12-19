#coding: utf-8

import json
import functools

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
    l = []
    with open("input.txt") as fd:
        n = 0
        for line in fd:
            line = line.strip()
            if not line:
                continue
            l.append(json.loads(line))

        l.append([[2]])
        l.append([[6]])
        l = sorted(l, key=functools.cmp_to_key(compare))


        x = y =0
        for i in range(len(l)):
            if [[2]] == l[i]:
                x = i+1
            if [[6]] == l[i]:
                y = i+1
        print(x*y)


main()
