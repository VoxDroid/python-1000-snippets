# 0196-JSON-Serialization Cheatsheet

* `json.dumps(obj)` -> string; `json.loads(str)` -> object.
* Use `indent=2` for pretty output.
* `ensure_ascii=False` for unicode; `sort_keys=True`.
* Serialize custom objects with `default=lambda o: o.__dict__`.
* Read/write files: `json.dump(obj, f)` and `json.load(f)`.
* Handle `JSONDecodeError` when parsing.

