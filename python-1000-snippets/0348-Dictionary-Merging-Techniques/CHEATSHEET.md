# 0348-Dictionary-Merging-Techniques Cheatsheet

- `merged = {**a, **b}` (b overrides a)
- `a.update(b)` mutates `a`.
- `ChainMap(a, b)` creates view layered map.
- Deep merge requires recursion over nested dicts.
