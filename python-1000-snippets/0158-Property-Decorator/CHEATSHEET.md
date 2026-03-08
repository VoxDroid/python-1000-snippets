# 0158-Property-Decorator Cheatsheet

- **Purpose**: wrap methods to look like attribute access for getters/setters/deleters.
- **Define**: use `@property` for getter, `@x.setter` for setter, `@x.deleter` for deleter.
- **Naming**: store data in a protected attribute (prefix `_`).
- **Read-only**: omit setter to make property immutable.
- **Computed**: property can calculate value on access.
- **Usage**: attributes appear as `obj.attr` not `obj.attr()`.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
