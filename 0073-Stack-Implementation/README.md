# Stack Implementation

## Description
This snippet implements a stack data structure using a Python list, supporting push, pop, and peek operations (LIFO: Last-In-First-Out).

## Code
```python
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

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Popped:", stack.pop())
print("Peek:", stack.peek())
print("Stack:", stack.items)
```

## Output
```
Popped: 3
Peek: 2
Stack: [1, 2]
```

## Explanation
- **Stack**: A LIFO structure where items are added (`push`) and removed (`pop`) from the top.
- **Methods**:
  - `push`: Adds an item to the top.
  - `pop`: Removes and returns the top item.
  - `peek`: Returns the top item without removing it.
  - `is_empty`: Checks if the stack is empty.
- **Use Case**: Stacks are used in algorithms (e.g., undo mechanisms, expression evaluation).
- **Best Practice**: Handle edge cases (e.g., popping from an empty stack); consider thread safety for concurrent use.