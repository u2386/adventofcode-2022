#coding: utf-8


class Knot:

    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
        self.next = None

    def move(self, pos):
        (self.x, self.y) = pos

        if self.next:
            next = self.next
            dx, dy = self.x-next.x, self.y-next.y

            if dx == 2 and dy == 2:
                self.next.move((next.x + 1, next.y + 1))
            elif dx == 2 and dy == -2:
                self.next.move((next.x + 1, next.y - 1))
            elif dx == -2 and dy == 2:
                self.next.move((next.x - 1, next.y + 1))
            elif dx == -2 and dy == -2:
                self.next.move((next.x - 1, next.y - 1))
            elif dx == 2:
                self.next.move((next.x + 1, self.y))
            elif dx == -2:
                self.next.move((next.x - 1, self.y))
            elif dy == 2:
                self.next.move((self.x, next.y + 1))
            elif dy == -2:
                self.next.move((self.x, next.y - 1))

    def __str__(self):
        return "knot#%d<%d, %d>" % (self.n, self.x, self.y)

    __repr__ = __str__


class Rope:

    def __init__(self, length):
        self.knots = [Knot(n, 0, 0) for n in range(length)]
        for i in range(len(self.knots)-1):
            self.knots[i].next = self.knots[i+1]

    def move(self, direct):
        head = self.knots[0]
        pos = move((head.x, head.y), direct)
        head.move(pos)


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
    r = Rope(10)
    seen = set()
    with open("input.txt", "r") as fd:
        for line in fd:
            (direct, steps) = line.strip().split(" ")
            steps = int(steps)
            for _ in range(steps):
                r.move(direct)
                tail = r.knots[-1]
                pos = (tail.x, tail.y)
                seen.add(pos)
        print(len(seen))

main()
