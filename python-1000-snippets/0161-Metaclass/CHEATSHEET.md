# 0161-Metaclass Cheatsheet

- **Purpose**: customize class creation by defining a metaclass (class of a class).
- **Define**: subclass `type` and override `__new__` or `__init__` to modify `attrs` or perform checks.
- **Usage**: specify via `class C(metaclass=MyMeta):` or set `__metaclass__` in Python 2.
- **Common patterns**: enforce naming rules, auto-register subclasses, add methods, implement singletons.
- **Note**: metaclasses affect all subclasses; use sparingly.

```python
class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['added'] = lambda self: 'hi'
        return super().__new__(cls, name, bases, attrs)

class C(metaclass=Meta):
    pass

print(C().added())
```

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
