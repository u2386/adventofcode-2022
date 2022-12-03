#coding: utf-8

A = ord('A')
a = ord('a')

def priority(c):
    p = ord(c) - a
    if p >= 0:
        return p + 1
    return ord(c) - A + 27


def main():
    rucksacks = []
    with open("input.txt", "r") as fd:
        rucksacks = fd.read().split("\n")[:-1]

    output = 0
    i = 0
    while i < len(rucksacks):
        s0, s1, s2 = set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])
        s0 = s0 & s1 & s2
        output += priority(list(s0)[0])
        i += 3
    print(output)

main()
