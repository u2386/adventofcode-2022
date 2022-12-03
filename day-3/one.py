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
        rucksacks = fd.read().split("\n")

    output = 0
    for rucksack in rucksacks[:-1]:
        mid = len(rucksack) >> 1
        s0, s1 = set(rucksack[:mid]), set(rucksack[mid:])
        s0 = s0 & s1
        output += priority(list(s0)[0])
    print(output)

main()
