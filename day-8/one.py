#coding: utf-8

def main():
    grid = []
    with open("input.txt", "r") as fd:
        for line in fd:
            line = line.strip()
            if not line:
                break
            grid.append([int(i) for i in line])


    count = 0
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            e = grid[row][col]
            if max([i[col] for i in grid[:row]]) < e:
                count += 1
            elif max([i[col] for i in grid[row+1:]]) < e:
                count += 1
            elif max(grid[row][:col]) < e:
                count += 1
            elif max(grid[row][col+1:]) < e:
                count += 1

    print(count + len(grid)*2 + len(grid[0])*2 - 4)

main()
