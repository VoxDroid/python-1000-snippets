# 0341-Complex-Lambda-Expressions Cheatsheet

- **Conditional lambda**: `lambda x: x**2 if x > 0 else -x`
- **Sorting with key**: `sorted(items, key=lambda x: (x[1], x[0]))`
- **Pipeline**: `sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data)))`
- Keep lambdas short; if logic grows, use a named function.
