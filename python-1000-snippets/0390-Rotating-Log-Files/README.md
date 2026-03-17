
# Rotating Log Files

## Description
Demonstrates how to use Python's `logging` library to rotate log files when they grow too large.

## Files
- `SAMPLES/sample1.py` — Writes logs in a temp directory and shows rotated files.
- `SAMPLES/sample2.py` — Configures a formatter and uses `RotatingFileHandler`.
- `SAMPLES/sample3.py` — Demonstrates `TimedRotatingFileHandler` and manual rollover.

## Usage
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Rotation occurs when the file exceeds `maxBytes` or based on time intervals.
- The examples use temporary directories to avoid polluting the repository.
