# RabbitMQ Work Queues

## Description
Demonstrates a work queue pattern using Kombu with an in-memory transport (no RabbitMQ server required).

## Files
- `SAMPLES/sample1.py` — Publish and consume a single task.
- `SAMPLES/sample2.py` — Process multiple tasks and acknowledge messages.
- `SAMPLES/sample3.py` — Use exchanges and routing keys to route messages.

## Usage
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Scripts install `kombu` if missing.
- Uses `memory://` transport to avoid external dependencies.
