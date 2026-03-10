# 0182-Prototype Cheatsheet

- **Purpose**: duplicate objects by copying prototypes instead of creating new instances.
- **Methods**: implement `clone()` or use `copy.copy`/`copy.deepcopy`.
- **Shallow vs deep**: shallow clones share referenced objects; deep clones recursively copy.
- **Use-case**: object with complex initialization, default configurations.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```