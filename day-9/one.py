#coding: utf-8


def move(pos, direct):
    if direct == "R":
        return (pos[0], pos[1]+1)
    if direct == "L":
        return (pos[0], pos[1]-1)
    if direct == "U":
        return (pos[0]-1, pos[1])
    if direct == "D":
        return (pos[0]+1, pos[1])

def around(pos):
    return [
        (pos[0]+x, pos[1]+y) for x, y in (
            (0, 0),
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        )
    ]


def main():
    tail = head = (0, 0)
    count = 0
    seen = set(tail)
    with open("input.txt", "r") as fd:
        for line in fd:
            line = line.strip()
            direct, steps = line.split(" ")
            for _ in range(int(steps)):
                prev, head = head, move(head, direct)
                if tail in around(head):
                    continue
                tail = prev
                if tail not in seen:
                    count += 1
                    seen.add(tail)
    print(count)


main()
