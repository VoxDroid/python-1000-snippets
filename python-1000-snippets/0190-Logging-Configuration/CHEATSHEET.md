# 0190-Logging-Configuration Cheatsheet

* Configure logging with `logging.basicConfig()`:
  - `level`: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - `format`: e.g. `'%(asctime)s - %(levelname)s - %(message)s'`
  - `handlers`: list of handlers (`FileHandler`, `StreamHandler`, `RotatingFileHandler`)
* Get logger: `logger = logging.getLogger(__name__)`
* Change level at runtime: `logger.setLevel(logging.DEBUG)`
* Use `logging.config.fileConfig()` or `dictConfig()` for complex apps.
* Rotate files with `logging.handlers.RotatingFileHandler` or `TimedRotatingFileHandler`.
* Avoid `print()`; use structured logging when needed (e.g. JSON).

