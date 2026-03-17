# 0350-Custom-Iterator-Design Cheatsheet

- Iterator class must implement `__iter__` and `__next__`.
- `for` loops use `iter()` and `next()` under the hood.
- Raise `StopIteration` when done.
- Iterators can be stateful and memory efficient.
