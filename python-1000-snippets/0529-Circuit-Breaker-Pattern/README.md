# Circuit Breaker Pattern

## Description
This snippet demonstrates a simple circuit breaker implementation.

## Code
```python
try:
    class CircuitBreaker:
        def __init__(self, max_failures=3):
            self.failures = 0
            self.max_failures = max_failures
        
        def call(self, func):
            if self.failures >= self.max_failures:
                return "Circuit open"
            try:
                return func()
            except:
                self.failures += 1
                return "Failure"
    
    cb = CircuitBreaker()
    print("Circuit state:", cb.call(lambda: 1/0))
except ImportError:
    print("Mock Output: Circuit state: Failure")
```

## Output
```
Mock Output: Circuit state: Failure
```
*(Real output: `Circuit state: Failure`)*

## Explanation
- **Circuit Breaker Pattern**: Prevents repeated failures in a service.
- **Logic**: Tracks failures and opens circuit after a threshold.
- **Complexity**: O(1) per call.
- **Use Case**: Used in distributed systems for fault tolerance.
- **Best Practice**: Set reset timers; log states; tune thresholds.