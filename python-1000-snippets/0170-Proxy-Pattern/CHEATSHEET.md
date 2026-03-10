# 0170-Proxy-Pattern Cheatsheet

- **Purpose**: provide a surrogate or placeholder object controlling access to another object (the subject).
- **Variants**: virtual proxy (lazy initialization), protection proxy (access control), logging proxy, caching proxy, remote proxy.
- **Structure**: Proxy implements the same interface as Subject and holds a reference to real object.
- **Transparency**: Clients use Proxy just like Subject; proxy may add pre/post processing.
- **Python tips**: Use `__getattr__` to delegate transparently; consider decorators for simple cases.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
