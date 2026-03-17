# 0362-Thread-Safe-Singleton Cheatsheet

- Use a lock around instance creation to prevent race conditions.
- Store the singleton reference as a class attribute.
- Avoid expensive initialization inside `__new__` when possible.
- For simple cases, module-level singletons are easier.
