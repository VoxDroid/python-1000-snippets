# Logging Cheatsheet

## Basic setup
```python
import logging
logging.basicConfig(level=logging.INFO)
```

## Levels
- `logging.debug()`, `info()`, `warning()`, `error()`, `critical()`.

## Handlers
```python
fh = logging.FileHandler('app.log')
logger.addHandler(fh)
```

## Named loggers
```python
logger = logging.getLogger('myapp')
```

## Formatting
`format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'`

## Tips
- Call `logging.getLogger()` to avoid root logger misconfig.
- Use different handlers for console and file outputs.

## Running samples
Activate venv and execute `SAMPLES/sample*.py`; inspect any created log files.
