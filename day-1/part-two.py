#coding: utf-8

import heapq

def main():
    calories = []
    with open("input.txt", "r") as fd:
        calories = fd.read().split("\n")

    heap = [0, 0, 0]
    temp = 0
    for cal in calories:
        if cal == "":
            _ = heapq.heappushpop(heap, temp)
            temp = 0
            continue
        temp += int(cal)

    print(sum(heap))

main()
