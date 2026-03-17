
# 0397-Secure-Pickle-Handling Cheatsheet

- `pickle.loads` can execute arbitrary code when loading untrusted data.
- Only unpickle data from trusted sources.
- Override `pickle.Unpickler.find_class` to restrict allowed globals.
- Prefer JSON for simple, safe serialization.
