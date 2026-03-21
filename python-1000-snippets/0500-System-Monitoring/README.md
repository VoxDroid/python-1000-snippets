# System Monitoring

## Description
This snippet demonstrates basic system monitoring using the Python standard library.

## Code
- `SAMPLES/sample1.py`: collects CPU count and load averages via `os`.
- `SAMPLES/sample2.py`: collects disk usage via `shutil.disk_usage`.
- `SAMPLES/sample3.py`: writes a status snapshot to `temp/system_status.txt`.

## Output
- `sample1.py` prints CPUs and load averages.
- `sample2.py` prints disk usage in GB.
- `sample3.py` writes status to `temp/system_status.txt` and prints the output path.

## Explanation
- **System Monitoring**: Captures system-level metrics (CPU, load, disk) without external dependencies.
- **Logic**:
  - `os.cpu_count`, `os.getloadavg` for processor metrics.
  - `shutil.disk_usage` for filesystem metrics.
  - `platform` and file writes for persistent snapshots.
- **Complexity**: O(1) for each metric collection.
- **Use Case**: Basic local monitoring script as a building block for alerts/triggers.
- **Best Practice**: Run periodically (cron/scheduler) and collect historical series for trend analysis.