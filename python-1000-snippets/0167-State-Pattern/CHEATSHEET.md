# 0167-State-Pattern Cheatsheet

- **Purpose**: change behavior of an object when its internal state changes without conditional statements scattered throughout methods.
- **Structure**: context object holds a reference to a state object implementing a common interface; states handle context and possibly transition to other states.
- **Transition**: states typically update `context.state` to a different state instance.
- **Use cases**: finite state machines, UI widgets, parser states.
- **Alternate**: use enum-based switch or strategy pattern for simpler cases.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
