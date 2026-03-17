# 0360-Class-Method-Patterns Cheatsheet

- Use `@classmethod` to access the class (`cls`) rather than instance (`self`).
- Common use cases: alternative constructors, caching, or class-level state.
- `cls` allows subclasses to override behavior.
- Static methods don't have access to `cls` or `self`.
