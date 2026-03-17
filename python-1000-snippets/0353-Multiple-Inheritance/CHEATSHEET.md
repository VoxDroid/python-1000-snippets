# 0353-Multiple-Inheritance Cheatsheet

- Method Resolution Order (MRO) determines which parent method is called.
- Use `super()` to delegate to the next class in MRO.
- Avoid complex diamond inheritance; prefer composition when possible.
- Inspect `Class.__mro__` to understand method lookup order.
