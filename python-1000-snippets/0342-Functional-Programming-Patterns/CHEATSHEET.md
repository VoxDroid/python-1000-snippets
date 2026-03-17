# 0342-Functional-Programming-Patterns Cheatsheet

- `map(fn, iterable)` applies `fn` to each element.
- `filter(fn, iterable)` keeps items where `fn(item)` is truthy.
- `reduce(fn, iterable, start)` collapses an iterable to a single value.
- `functools.partial(fn, x)` fixes some arguments of `fn`.
- Compose: `lambda x: f(g(x))`.
