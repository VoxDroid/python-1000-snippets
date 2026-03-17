# 0356-Private-Attribute-Management Cheatsheet

- Prefix with `__` for name mangling (not truly private).
- Access mangled attribute via `_ClassName__attr` only when necessary.
- Use `@property` to control access to internal state.
- `__slots__` can restrict attributes and save memory.
