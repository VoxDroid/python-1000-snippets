# Bulkhead Isolation

## Description
This snippet demonstrates bulkhead isolation through separate thread pools for subsystems.

## Code
- `SAMPLES/sample1.py`: two thread pools with confined worker counts.
- `SAMPLES/sample2.py`: show bulkhead status reports.
- `SAMPLES/sample3.py`: logs bulkhead events to `temp/0531_bulkhead_log.txt`.

## Output
- sample1: A and B task results.
- sample2: status dictionary for each bulkhead.
- sample3: logs a handful of events.

## Explanation
- **Bulkhead Isolation**: limits resource impact by bounding concurrency per subsystem.
- **Logic**: separate thread pools and status check.
- **Complexity**: O(n) across tasks.
- **Use Case**: microservices for fault isolation and performance stability.
- **Best Practice**: monitor usage and fine-tune thread limits.
