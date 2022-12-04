#coding: utf-8


def main():
    paris = []
    with open("input.txt", "r") as fd:
        pairs = fd.read().split("\n")[:-1]

    overlaps = 0
    for pair in pairs:
        (first, second) = [list(map(int, i.split("-"))) for i in pair.split(",")]
        if first[0] <= second[0] and first[-1] >= second[-1]:
            overlaps += 1
        elif second[0] <= first[0] and second[-1] >= first[-1]:
            overlaps += 1

    print(overlaps)

main()
