# 0343-Map-Reduce-Pipeline Cheatsheet

- **Map**: Transform elements.
- **Filter**: Select elements.
- **Reduce**: Aggregate elements.
- Pipelines: chain operations for clarity and laziness.

Example pipeline:
```
result = reduce(fn, map(transform, filter(predicate, items)), initial)
```
