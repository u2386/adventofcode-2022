#coding: utf-8

TYPE_DIR = "dir"
TYPE_FILE = "file"


class Node(object):

    def __init__(self, typ, name, parent=None, size=0):
        self.typ = typ
        self.name = name
        self.parent = parent
        self.__size = size
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def __str__(self):
        return "<%s:%s: %s>" % (self.typ, self.name, self.children)

    __repr__ = __str__

    def size(self):
        if self.typ == TYPE_FILE:
            return self.__size
        else:
            return sum([child.size() for child in self.children])


root = current = Node(TYPE_DIR, "/")

def cd(name):
    global current

    if name == "/":
        current = root
    elif name == "..":
        current = current.parent
    else:
        for child in current.children:
            if name == child.name:
                current = child
                return

objs = []

def main():
    with open("input.txt", "r") as fd:
        for line in fd:
            line = line.strip()
            if not line:
                break

            if line.startswith("$ cd"):
                (_, _, path) = line.split(" ")
                cd(path)
            elif line.startswith("$ ls"):
                continue
            else:
                type_or_size, name = line.split(" ")
                if type_or_size == TYPE_DIR:
                    node = Node(TYPE_DIR, name, current)
                    current.add_child(node)
                    objs.append(node)
                else:
                    node = Node(TYPE_FILE, name, current, int(type_or_size))
                    current.add_child(node)
    print(sum(n.size() for n in objs if n.size() < 100000))

main()
