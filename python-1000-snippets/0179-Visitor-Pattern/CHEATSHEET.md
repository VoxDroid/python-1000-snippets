# 0179-Visitor-Pattern Cheatsheet

- **Purpose**: lets you define new operations on elements of an object structure without changing the classes of the elements.
- **Roles**: `Visitor` interface with visit methods for each element type; concrete visitors implement these operations.
- **Element**: classes implement `accept(visitor)` which calls the appropriate visitor method.
- **Use cases**: operations across complex object structures, such as AST traversal, serialization, analytics.
- **Tip**: adding a new element type requires extending visitor interface; adding new operations is easy (just new visitor).

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
