# 0156-Encapsulation Cheatsheet

- **Purpose**: restrict direct access to an object's components to prevent misuse.
- **Private attributes**: prefix with `__` to trigger name mangling; not truly private but harder to access.
- **Protected convention**: prefix with `_` to indicate internal use.
- **Access via methods**: use getters/setters or `@property` for controlled access.
- **Validate inputs** in mutators to enforce invariants.
- **Tips**: Python relies on conventions rather than enforcement; focus on documentation.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
