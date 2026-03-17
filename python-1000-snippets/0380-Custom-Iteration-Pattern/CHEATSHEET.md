# 0380-Custom-Iteration-Pattern Cheatsheet

- Implement `__iter__` and `__next__` for custom iterators.
- Return `self` from `__iter__` and raise `StopIteration` when done.
- Iterators maintain internal state across iterations.
- Use generators (`yield`) for simpler iteration patterns.
