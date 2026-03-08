# 0166-Command-Pattern Cheatsheet

- **Purpose**: wrap a request as an object, allowing parametrization of clients with queues, logs, and undo operations.
- **Components**: `Command` interface with `execute()` (and optionally `undo()`), concrete command classes, invoker, and receiver.
- **Invoker**: holds a command and calls its `execute` method (e.g., remote control, button).
- **Extensibility**: add new commands without changing invoker code.
- **Common uses**: GUI button actions, task queues, macros, undo/redo stacks.

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```
