# Multiple Inheritance

## Description
This snippet demonstrates multiple inheritance with method resolution.

## Code
```python
class A:
    def feature(self):
        return "Feature A"

class B:
    def feature(self):
        return "Feature B"

class C(A, B):
    pass

obj = C()
print(obj.feature())
```

## Output
```
Feature A
```

## Explanation
- **Multiple Inheritance**: Combines features from multiple parent classes.
- **Logic**: Class `C` inherits from `A` and `B`; method resolution order prioritizes `A`.
- **Complexity**: O(1) for method lookup.
- **Use Case**: Used for combining behaviors in complex class hierarchies.
- **Best Practice**: Avoid diamond problem; use `super()`; check MRO with `__mro__`.