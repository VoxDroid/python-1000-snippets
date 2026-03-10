# 0173-Composite-Pattern Cheatsheet

- **Purpose**: compose objects into tree structures and let clients treat individual objects and compositions uniformly.
- **Key roles**: `Component` interface, `Leaf` for primitive objects, `Composite` for containers holding children.
- **Methods**: composites usually implement `add`, `remove`, `get_child`, and delegate primary operations to children.
- **Benefits**: simplifies client code that needs to work with hierarchical data (e.g., directories, UI widgets).
- **Tip**: consider implementing traversal or iteration methods (e.g. depth-first walk).

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
