#coding: utf-8

def main():
    with open("input.txt", "r") as fd:
        window = []
        p = 0
        while True:
            p += 1
            c = fd.read(1)
            if c == "\n":
                print("break")
                break

            offset = 0
            for i in range(len(window)):
                if c == window[i]:
                    offset = i+1

            window = window[offset:]
            window.append(c)
            if len(window) == 4:
                print(p)
                break


main()
