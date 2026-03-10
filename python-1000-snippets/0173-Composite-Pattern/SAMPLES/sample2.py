# sample2.py
# filesystem-like composite structure

class Component:
    def display(self, indent=0):
        pass

class File(Component):
    def __init__(self, name):
        self.name = name
    def display(self, indent=0):
        print(' ' * indent + f"File: {self.name}")

class Directory(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    def add(self, comp):
        self.children.append(comp)
    def display(self, indent=0):
        print(' ' * indent + f"Directory: {self.name}")
        for c in self.children:
            c.display(indent + 2)

if __name__ == '__main__':
    root = Directory('root')
    root.add(File('file1.txt'))
    sub = Directory('sub')
    sub.add(File('file2.txt'))
    root.add(sub)
    root.display()
