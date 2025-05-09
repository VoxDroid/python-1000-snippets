# Signal Handling

## Description
This snippet demonstrates handling system signals (e.g., Ctrl+C) using the `signal` module to gracefully exit a program.

## Code
```python
import signal
import time

def handler(signum, frame):
    print("\nReceived signal, exiting gracefully.")
    exit(0)

signal.signal(signal.SIGINT, handler)
print("Running... Press Ctrl+C to stop.")
while True:
    time.sleep(1)
```

## Output
```
Running... Press Ctrl+C to stop.
^C
Received signal, exiting gracefully.
```

## Explanation
- **signal.signal()**: Registers a handler function for a signal (`SIGINT` for Ctrl+C).
- **Handler**: `handler(signum, frame)` defines custom behavior when the signal is received.
- **Use Case**: Signal handling is used for cleanup, logging, or graceful shutdown in long-running programs.
- **Limitations**: Not all signals can be caught; behavior varies by platform.
- **Best Practice**: Handle only necessary signals and ensure cleanup code is robust.