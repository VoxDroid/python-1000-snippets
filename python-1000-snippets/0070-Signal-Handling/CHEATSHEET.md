# Signal Handling Cheatsheet

## Registering handlers
```python
import signal
signal.signal(signal.SIGINT, handler)
```

## Common signals
- `SIGINT` Ctrl+C
- `SIGTERM` termination request
- `SIGKILL` cannot be caught

## Ignoring signals
```
signal.signal(signal.SIGINT, signal.SIG_IGN)
```

## Tips
- Handler signature: `(signum, frame)`
- A handler should be quick; avoid blocking operations.

## Running samples
Use `timeout` command to send SIGTERM or SIGINT in tests.
