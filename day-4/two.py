#coding: utf-8


def main():
    paris = []
    with open("input.txt", "r") as fd:
        pairs = fd.read().split("\n")[:-1]

    overlaps = 0
    for pair in pairs:
        (first, second) = [list(map(int, i.split("-"))) for i in pair.split(",")]
        if max(first[0], second[0]) <= min(first[-1], second[-1]):
            overlaps += 1

    print(overlaps)

main()
