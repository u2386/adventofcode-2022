#coding: utf-8

scores = {
    ("A", "X"): 1+3,
    ("A", "Y"): 2+6,
    ("A", "Z"): 3+0,
    ("B", "X"): 1+0,
    ("B", "Y"): 2+3,
    ("B", "Z"): 3+6,
    ("C", "X"): 1+6,
    ("C", "Y"): 0+2,
    ("C", "Z"): 3+3,
}

def main():
    with open("input.txt", "r") as fd:
        results = fd.read().split("\n")
    print(sum([scores[tuple(i.split(" "))] for i in results if i]))

main()
