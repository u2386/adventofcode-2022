#coding: utf-8


def main():
    with open("input.txt", "r") as fd:
        lines = fd.read().split("\n")[:-1]
    stacks = []
    for i, line in enumerate(lines):
        if len(line) == 0:
            lines = lines[i+1:]
            break
        line = [line[i:i+3] for i in range(0, len(line), 4) if i % 4 == 0]
        stacks.append(line)
    stacks = stacks[:-1][::-1]
    stacks = [list(sub) for sub in list(zip(*stacks))]
    stacks = [[i for i in stack if i[0] == "["] for stack in stacks]


    for line in lines:
        terms = line.split(" ")
        (count, frm, to) = int(terms[1]), int(terms[3]), int(terms[-1])
        stacks[to-1].extend(stacks[frm-1][-count:])
        stacks[frm-1] = stacks[frm-1][:-count]
    print([s[-1] for s in stacks if s])


main()
