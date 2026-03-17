# FastAPI Authentication

## Description
Demonstrates basic authentication using FastAPI and how to test endpoints without running a persistent server.

## Files
- `SAMPLES/sample1.py` — Secure endpoint with HTTP Basic auth tested via FastAPI test client.
- `SAMPLES/sample2.py` — POST endpoint returning JSON payloads.
- `SAMPLES/sample3.py` — Custom response status codes and headers.

## Usage
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Install FastAPI with `python -m pip install fastapi`.
- These scripts use the FastAPI test client so no server needs to be started.
