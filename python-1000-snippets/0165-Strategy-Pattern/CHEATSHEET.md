# 0165-Strategy-Pattern Cheatsheet

- **Purpose**: allow selecting an algorithm or behavior at runtime by encapsulating each in a separate class or function.
- **Components**: `Strategy` interface/abstract class, concrete strategy implementations, `Context` holding a reference to a strategy.
- **Switching**: `context.set_strategy(new_strategy)` to change behavior dynamically.
- **Function alternatives**: strategies can also be plain functions or callables, eliminating the need for classes.
- **Use cases**: sorting, validation, compression, calculation where multiple methods exist.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
