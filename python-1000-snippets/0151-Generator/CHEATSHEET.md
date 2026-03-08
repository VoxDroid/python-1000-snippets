# 0151-Generator Cheatsheet

- **Purpose**: create iterators that produce values on-the-fly using `yield`.
- **Defining**: use `def gen(): yield value` or generator expressions `(x*x for x in range(5))`.
- **Consumption**: iterate with `for`, `next()`, or convert to list.
- **Statefulness**: retains local variables between yields.
- **Memory**: uses constant space, ideal for large or infinite sequences.
- **Examples**:
  ```python
  def count_up(n):
      i = 0
      while i < n:
          yield i
          i += 1
  ```
- **Tips**: avoid reusing exhausted generator; wrap in `itertools.tee` if needed.
- **Common libs**: `itertools` has many generator-producing functions.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
