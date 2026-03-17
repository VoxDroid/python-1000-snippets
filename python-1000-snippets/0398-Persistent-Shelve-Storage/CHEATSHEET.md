
# 0398-Persistent-Shelve-Storage Cheatsheet

- Use `shelve.open(filename)` to get a dict-like persistent store.
- Close the shelf to flush data (use `with` statement).
- Use `writeback=True` to cache mutable objects and call `sync()`.
- Avoid concurrent access to the same shelf from multiple processes.
