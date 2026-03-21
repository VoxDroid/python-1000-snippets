# Cron Job Automation

## Description
This snippet demonstrates cron-like automation with Python built-ins, without external `schedule` dependency.

## Code
- `SAMPLES/sample1.py`: simulates periodic task scheduling with `threading.Timer`.
- `SAMPLES/sample2.py`: uses a loop + `time.sleep` for recurring jobs.
- `SAMPLES/sample3.py`: writes job history to `temp/0507_cron_log.txt`.

## Output
- sample1: prints task run counts.
- sample2: prints timestamps and completion message.
- sample3: writes a log file plus path.

## Explanation
- **Cron Job Automation**: periodic task runtime scheduling in Python.
- **Logic**: use `Timer` for delayed re-scheduling and sleep loops for simple intervals.
- **Complexity**: linear in runs + fixed interval overhead.
- **Use Case**: schedule local maintenance checks, data snapshots, or sync jobs.
- **Best Practice**: use robust scheduler frameworks (APScheduler/Cron) in production; test intervals and exceptions.
