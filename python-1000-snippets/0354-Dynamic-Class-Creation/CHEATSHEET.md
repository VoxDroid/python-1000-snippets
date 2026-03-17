# 0354-Dynamic-Class-Creation Cheatsheet

- `type(name, bases, dict)` creates a class at runtime.
- `types.new_class(name, bases, exec_body=...)` for more flexible class creation.
- Useful for meta-programming, plugins, or DSLs.
- Keep generated classes simple for readability.
