# 0181-Builder-Pattern Cheatsheet

- **Purpose**: separate the construction of a complex object from its representation, allowing the same construction process to create different representations.
- **Components**: `Builder` class with methods for configuring parts, `Director` optional to orchestrate steps, the `Product` returned by `build()`.
- **Fluent interface**: return `self` from setter methods to chain calls.
- **Use cases**: configuration objects, query builders, UI widgets.
- **Tips**: validate required parts before build, provide defaults as needed.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
