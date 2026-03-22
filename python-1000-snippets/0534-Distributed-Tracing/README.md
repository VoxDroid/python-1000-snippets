# Distributed Tracing

## Description
This snippet simulates distributed tracing spans and exports to file.

## Code
- `SAMPLES/sample1.py`: start/end span events list.
- `SAMPLES/sample2.py`: nested span event sequence.
- `SAMPLES/sample3.py`: writes trace events to `temp/0534_trace_output.txt`.

## Output
- sample1: trace entries printed.
- sample2: nested events printed.
- sample3: trace output file written.

## Explanation
- **Distributed Tracing**: track request flow across components.
- **Logic**: produce start/end span event logs.
- **Complexity**: O(1) per span event.
- **Use Case**: distributed service observability.
- **Best Practice**: use standard tracing libraries and exporters in production.
