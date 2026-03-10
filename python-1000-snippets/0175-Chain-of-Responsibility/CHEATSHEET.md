# 0175-Chain-of-Responsibility Cheatsheet

- **Purpose**: allow a request to be passed along a chain of handlers until one handles it.
- **Structure**: each handler has a `handle(request)` method and a reference to the next handler (`successor`).
- **Setup**: build the chain by linking handlers (e.g. `h1 = H1(H2(H3()))`).
- **Variations**: stop on first handle, or let multiple handlers process; use for event bubbling.
- **Tip**: handlers can be functions or objects; use `None` as terminator to avoid checks.

```bash
python3 SAMPLES/sample1.py
python3 SAMPLES/sample2.py
python3 SAMPLES/sample3.py
```
