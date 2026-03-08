# sample1.py
# Basic stack operations: push, pop, peek

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0

if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print('peek', s.peek())
    print('pop', s.pop())
    print('stack', s.items)
