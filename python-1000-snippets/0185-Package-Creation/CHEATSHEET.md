# 0185-Package-Creation Cheatsheet

- **Purpose**: group related modules under a directory with an `__init__.py` file making it a package.
- **Namespace**: package name becomes part of import path (`import my_package.module`).
- **Structure**: nested packages are allowed; use `from . import submodule` for intra-package imports.
- **Installation**: packages can be installed with pip or made available via `PYTHONPATH`.
- **Tip**: `__init__.py` can import selected names to expose via package-level API.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
