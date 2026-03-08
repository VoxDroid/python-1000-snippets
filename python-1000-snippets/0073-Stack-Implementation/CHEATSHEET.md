# 0073-Stack-Implementation Cheatsheet

- Use a Python list to implement stack operations:
  ```python
  stack = []
  stack.append(item)    # push
  item = stack.pop()    # pop
  top = stack[-1]       # peek
  is_empty = len(stack) == 0
  ```
- For encapsulation, wrap list in a `Stack` class with methods: `push`, `pop`, `peek`, `is_empty`.
- Handle popping from empty stack gracefully (e.g., return `None` or raise exception).
- Useful in recursion elimination, expression evaluation, backtracking, undo/redo systems.


## Quick examples

- Pop until empty:
  ```python
  while not stack.is_empty():
      stack.pop()
  ```

- Reverse a list using stack:
  ```python
  s = Stack()
  for x in mylist:
      s.push(x)
  reversed_list = []
  while not s.is_empty():
      reversed_list.append(s.pop())
  ```
