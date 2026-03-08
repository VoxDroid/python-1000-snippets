# 0160-Class-Method Cheatsheet

- **Purpose**: define methods bound to the class rather than an instance; first argument is `cls`.
- **Common uses**: alternative constructors (`from_*`), factories, class-wide state manipulation.
- **Syntax**:
  ```python
  class C:
      @classmethod
      def f(cls, arg):
          return cls(arg)
  ```
- **Call**: `C.f()` or `instance.f()` both receive the class.
- **Subclasses**: called on subclass, `cls` refers to subclass allowing polymorphic construction.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
