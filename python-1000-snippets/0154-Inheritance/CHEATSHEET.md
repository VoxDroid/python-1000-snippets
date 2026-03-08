# 0154-Inheritance Cheatsheet

- **Purpose**: reuse and extend functionality by deriving new classes from existing ones.
- **Syntax**: `class Child(Parent):` inheriting methods and attributes.
- **Constructor chaining**: call parent `__init__` via `super().__init__(...)`.
- **Method overriding**: redefine methods in child; call parent method with `super().method()`.
- **Multiple inheritance**: list several bases `class C(A, B):`; be aware of MRO.
- **Polymorphism**: treat subclass instances as parent types.

```python
class A: pass
class B(A): pass
``` 

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
