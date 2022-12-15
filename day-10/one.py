#coding: utf-8

def main():
    signals = []
    with open("input.txt", "r") as fd:
        cycle = 0
        x = 1
        rq = []
        while True:
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signals.append(x*cycle)
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

    print(sum(signals))



main()
