# Session Management

## Description
This snippet demonstrates simple session state management in Python.

## Code
- `SAMPLES/sample1.py`: in-memory session dictionary operations.
- `SAMPLES/sample2.py`: session TTL and validity check.
- `SAMPLES/sample3.py`: persist session store to `temp/0527_sessions.txt`.

## Output
- sample1: prints session data for user1.
- sample2: prints session validity before and after expiry.
- sample3: writes sessions to file.

## Explanation
- **Session Management**: track user session metadata.
- **Logic**: create, validate, and persist session entries.
- **Complexity**: O(1) per operation.
- **Use Case**: stateful user authentication systems.
- **Best Practice**: secure session store, ttl expiry, and rotate keys.
