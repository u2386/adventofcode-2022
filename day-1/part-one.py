#coding: utf-8


def main():
    calories = []
    with open("input.txt", "r") as fd:
        calories = fd.read().split("\n")

    most = 0
    temp = 0
    for cal in calories:
        if cal == "":
            most = max(most, temp)
            temp = 0
            continue
        temp += int(cal)
    print(most)


if __name__ == "__main__":
    main()
