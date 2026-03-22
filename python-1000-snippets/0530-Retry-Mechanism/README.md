# Retry Mechanism

## Description
This snippet demonstrates retry behavior for unreliable operations.

## Code
- `SAMPLES/sample1.py`: decorator-based retry for transient failures.
- `SAMPLES/sample2.py`: exponential backoff retry loop.
- `SAMPLES/sample3.py`: logs attempts to `temp/0530_retry_log.txt`.

## Output
- sample1: `Retry result: success`.
- sample2: `Call result: done`.
- sample3: outcome and log path.

## Explanation
- **Retry Mechanism**: retries on transient failures.
- **Logic**: attempt function multiple times with optional delays.
- **Complexity**: O(n) with retries.
- **Use Case**: unstable network operations, database connections.
- **Best Practice**: handle specific exceptions, add backoff, record retries.
