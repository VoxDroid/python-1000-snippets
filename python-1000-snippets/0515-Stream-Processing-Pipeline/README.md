# Stream Processing Pipeline

## Description
This snippet demonstrates stream processing patterns using simple Python stream transformations.

## Code
- `SAMPLES/sample1.py`: rolling mean over streaming values.
- `SAMPLES/sample2.py`: filter + transform pipeline for a generator.
- `SAMPLES/sample3.py`: writes stream stats to `temp/0515_stream_stats.txt`.

## Output
- sample1: `Rolling mean: [None, 1.5, 2.5, 3.5, 4.5]`.
- sample2: `Transformed stream: [0, 4, 8, 12, 16]`.
- sample3: filled stat file.

## Explanation
- **Stream Processing Pipeline**: processes sequence data event-by-event.
- **Logic**: window-based mean and filtering.
- **Complexity**: O(n).
- **Use Case**: real-time analytics and sensor data preprocessing.
- **Best Practice**: maintain fixed memory usage, use lazy generators, persist results to logs.
