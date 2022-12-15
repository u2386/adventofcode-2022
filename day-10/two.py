#coding: utf-8

def main():
    crt = [["."] * 40 for _ in range(6)]
    with open("input.txt", "r") as fd:
        cycle = 0
        x = 1
        rq = []
        while True:
            cycle += 1
            if rq:
                (_, v) = rq.pop()
                x += int(v)
            else:
                line = fd.readline().strip()
                if not line:
                    break
                items = line.split(" ")
                if items[0] == "addx":
                    rq.append(items)

            row = cycle // 40
            col = cycle % 40
            if col == x-1 or col == x or col == x+1:
                crt[row][col] = "#"
            if col == 0:
                for row in crt:
                    print("".join(row))
                print()

main()
