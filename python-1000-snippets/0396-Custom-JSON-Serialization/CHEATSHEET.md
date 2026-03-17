
# 0396-Custom-JSON-Serialization Cheatsheet

- Define a method to convert your object into primitives (dict/list).
- Use `json.dumps(obj, default=lambda o: o.__dict__)` for quick serialization.
- For dataclasses, use `dataclasses.asdict()`.
- Avoid serializing non-serializable objects (like file handles) directly.
