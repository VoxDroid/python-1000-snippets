# sample2.py
# Handle underflow gracefully

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.items:
            print('stack empty, cannot pop')
            return None
        return self.items.pop()

if __name__ == '__main__':
    s = Stack()
    print('pop on empty:', s.pop())
    s.push('a')
    print('pop now:', s.pop())
    print('pop again:', s.pop())
