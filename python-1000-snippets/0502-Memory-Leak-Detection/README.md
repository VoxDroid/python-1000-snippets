# Memory Leak Detection

## Description
This snippet demonstrates memory tracking and leak detection using Python standard `tracemalloc`.

## Code
- `SAMPLES/sample1.py`: create objects, take a snapshot, print top allocations.
- `SAMPLES/sample2.py`: compare two snapshots to identify growth.
- `SAMPLES/sample3.py`: save top snapshot information to `temp/0502_mem_snapshot.txt`.

## Output
- `sample1.py`: top 5 allocations displayed.
- `sample2.py`: top 5 positive differences shown.
- `sample3.py`: output file path displayed.

## Explanation
- **Memory Leak Detection**: Tracks allocations and compares snapshots.
- **Logic**: allocate memory blocks, use `tracemalloc.start()`, `take_snapshot()`, `statistics()`, `compare_to()`.
- **Complexity**: O(n) for object list creation and diff scan.
- **Use Case**: regression detection for creeping memory use in long-running processes.
- **Best Practice**: Collect snapshots periodically and analyze with `pstats` and `tracemalloc` filters.
