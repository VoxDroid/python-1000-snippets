# 0152-Iterator Cheatsheet

- **Purpose**: create objects that can be iterated with `for` loops.
- **Implement**: define `__iter__(self)` returning self or another iterator; define `__next__(self)` raising `StopIteration` when done.
- **Manual iteration**: use `iter(obj)` and `next(iterator)` to pull values yourself.
- **Common pattern**: wrap or adapt other iterables; e.g., ``class Repeater:`` returns repeated items.
- **Built-in helpers**: `iter(func, sentinel)` produces an iterator calling func until sentinel returned.
- **Use case**: custom traversal, lazy evaluation, infinite sequences.

```python
it = iter([1,2,3])
print(next(it))  # 1
``` 

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
