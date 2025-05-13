# Distributed Tracing

## Description
This snippet demonstrates setting up a trace using `opentelemetry`.

## Code
```python
# Note: Requires `opentelemetry-api`. Install with `pip install opentelemetry-api`
try:
    from opentelemetry import trace
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("example"):
        print("Trace started")
except ImportError:
    print("Mock Output: Trace started")
```

## Output
```
Mock Output: Trace started
```
*(Real output with `opentelemetry`: `Trace started`)*

## Explanation
- **Distributed Tracing**: Tracks requests across services.
- **Logic**: Starts a trace span for an operation.
- **Complexity**: O(1) per span.
- **Use Case**: Used for debugging microservices.
- **Best Practice**: Export traces; add metadata; integrate with Jaeger.