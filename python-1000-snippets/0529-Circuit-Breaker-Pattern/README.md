# Circuit Breaker Pattern

## Description
This snippet demonstrates circuit breaker behavior with fail tracking and state logging.

## Code
- `SAMPLES/sample1.py`: circuit breaker class with open state after failures.
- `SAMPLES/sample2.py`: demonstrates reset behavior to close the circuit.
- `SAMPLES/sample3.py`: logs state transitions to `temp/0529_circuit_log.txt`.

## Output
- sample1: failure and open states.
- sample2: reset and success after breaking state.
- sample3: log file entries for each check.

## Explanation
- **Circuit Breaker Pattern**: stops repeated failing calls and permits recovery.
- **Logic**: failure threshold triggers open state; reset closes circuit.
- **Complexity**: O(1) per invocation.
- **Use Case**: distributed service resilience.
- **Best Practice**: include backoff, health checks, and logs.
