# 0153-Class-Definition Cheatsheet

- **Purpose**: define custom types with attributes and methods.
- **Basic syntax**: `class C:` followed by indented body; use `def __init__(self,...)` to initialize.
- **Instance creation**: `obj = C(arg1, arg2)`; access with `obj.attr`.
- **Class vs instance variables**: define on class for shared defaults.
- **Special methods**: `__str__`, `__repr__`, `__eq__` add behavior.
- **Inheritance**: subclass using `class Sub(C):` to extend.
- **Tips**: keep `__init__` simple; consider `@dataclass` for boilerplate.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
