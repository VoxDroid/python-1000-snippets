# sample3.py
# Use stack to reverse a list

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def is_empty(self):
        return len(self.items) == 0

if __name__ == '__main__':
    original = [1, 2, 3, 4, 5]
    s = Stack()
    for v in original:
        s.push(v)
    reversed_list = []
    while not s.is_empty():
        reversed_list.append(s.pop())
    print('original', original)
    print('reversed', reversed_list)
