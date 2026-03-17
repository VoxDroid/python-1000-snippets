# sample2.py
# Composite representing a file system structure

class Node:
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        raise NotImplementedError


class File(Node):
    def display(self, indent=0):
        print(" " * indent + f"File: {self.name}")


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, node):
        self.children.append(node)

    def display(self, indent=0):
        print(" " * indent + f"Dir: {self.name}")
        for child in self.children:
            child.display(indent + 2)


def main():
    root = Directory("root")
    root.add(File("a.txt"))
    sub = Directory("sub")
    sub.add(File("b.txt"))
    root.add(sub)
    root.display()


if __name__ == "__main__":
    main()
