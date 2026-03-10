# 0172-Bridge-Pattern Cheatsheet

- **Purpose**: decouple an abstraction from its implementation so they can vary independently.
- **Abstraction**: high-level interface (e.g., `Shape`) holds a reference to implementor (e.g., `Renderer`).
- **Implementor**: defines low-level operations; concrete implementors provide specific behavior.
- **Bridge**: the indirection between abstraction and implementor; often an attribute reference.
- **Use case**: when both the abstraction and its implementation may have multiple variants and you want to mix and match.
- **Tip**: avoid class explosion by not creating a subclass for every combination.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
