#coding: utf-8

world = []
S = (None, None)
E = (None, None)


directs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]



def walk():
    queue = [(S, 0)]
    visited = set()
    visited.add(S)

    while queue:
        (pos, depth), queue = queue[0], queue[1:]
        if pos == E:
            return depth

        (x, y) = pos
        for (dx, dy) in directs:
            nx = x+dx
            ny = y+dy
            if not (0 <= nx < len(world) and 0 <= ny < len(world[0])):
                continue
            if ord(world[nx][ny]) - ord(world[x][y]) > 1:
                continue
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            queue.append(((nx, ny), depth+1))


def main():
    global S, E

    with open("input.txt") as fd:
        row = 0
        for line in fd:
            line = line.strip()
            if not line:
                break

            world.append(list(line))
            col = 0
            for p in world[-1]:
                if p == "S":
                    S = (row, col)
                if p == "E":
                    E = (row, col)
                col += 1
            col = 0
            row += 1

    world[S[0]][S[1]] = "a"
    world[E[0]][E[1]] = "z"
    print(walk())

main()
