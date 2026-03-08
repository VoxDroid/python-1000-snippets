# 0162-Singleton-Pattern Cheatsheet

- **Purpose**: restrict a class to one instance; provide global access point.
- **Common implementations**: override `__new__`, use metaclass, or module-level instance.
- **Thread-safety**: wrap instance creation with a lock in multithreaded code.
- **Usage**: call the class normally; subsequent calls return same object.
- **Alternatives**: use module variables (Python modules are singletons) or dependency injection.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
