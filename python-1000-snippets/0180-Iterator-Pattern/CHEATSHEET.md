# 0180-Iterator-Pattern Cheatsheet

- **Purpose**: provide a uniform way to access elements of an aggregate object sequentially without exposing its underlying representation.
- **Participants**: `Iterator` with `__iter__` and `__next__`, `Aggregate` or `Collection` providing a method to create iterators.
- **Usage**: use `for` loops or manual `next()` calls; support multiple iterators over same collection.
- **Python note**: any object implementing the iterator protocol works with `for`; use generator functions for simplicity.
- **Tips**: make iterator independent of collection to avoid state clashes; avoid modifying collection while iterating.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
