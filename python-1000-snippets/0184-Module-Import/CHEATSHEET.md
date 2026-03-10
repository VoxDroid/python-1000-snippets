# 0184-Module-Import Cheatsheet

- **Purpose**: organize code into separate files (modules) and import them where needed.
- **Syntax**: `import module`, `from module import name`, `import module as alias`.
- **Relative imports**: use `from . import foo` inside packages, or manipulate `sys.path` for standalone scripts.
- **Module search path**: printed via `import sys; print(sys.path)`; includes script directory.
- **Tips**: avoid name collisions with standard library; use `__init__.py` to make packages; keep modules small.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
