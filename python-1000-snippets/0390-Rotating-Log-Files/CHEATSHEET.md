
# 0390-Rotating-Log-Files Cheatsheet

- Use `logging.handlers.RotatingFileHandler` for size-based log rotation.
- Use `logging.handlers.TimedRotatingFileHandler` for time-based rotation.
- Set `backupCount` to keep a fixed number of rotated files.
- Use a `Formatter` to include timestamps and log levels.
- Use temporary directories in examples to avoid leaving log files behind.
