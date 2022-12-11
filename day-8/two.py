#coding: utf-8

import math

def main():
    grid = []
    with open("input.txt", "r") as fd:
        for line in fd:
            line = line.strip()
            if not line:
                break
            grid.append([int(i) for i in line])


    max_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            e = grid[row][col]
            scores = []

            r, c = row-1, col
            n = 0
            while r >= 0:
                n += 1
                if grid[r][col] >= e:
                    break
                r -= 1
            scores.append(n)

            r, c = row+1, col
            n = 0
            while r < len(grid):
                n += 1
                if grid[r][col] >= e:
                    break
                r += 1
            scores.append(n)

            r, c = row, col-1
            n = 0
            while c >= 0 :
                n += 1
                if grid[row][c] >= e:
                    break
                c -= 1
            scores.append(n)

            r, c = row, col+1
            n = 0
            while c < len(grid[row]):
                n += 1
                if grid[row][c] >= e:
                    break
                c += 1
            scores.append(n)

            max_score = max(max_score, math.prod(i for i in scores))
    print(max_score)


main()
