# 0149-Context-Manager Cheatsheet

- **Purpose**: manage resource setup/cleanup via `with` statement.
- **Define**: implement `__enter__` and `__exit__(self, exc_type, exc_val, exc_tb)` on a class.
- **Usage**: `with ResourceManager() as rm:` automatically calls enter/exit.
- **Exception handling**: `__exit__` receives exception info and can suppress or re-raise.

```python
class CM:
    def __enter__(self):
        print('enter'); return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit', exc_type)

with CM():
    print('inside')
```

- Built-in context managers: `open`, `threading.Lock`, `decimal.localcontext`, etc.
- Use `contextlib.contextmanager` decorator for generator-based managers.

