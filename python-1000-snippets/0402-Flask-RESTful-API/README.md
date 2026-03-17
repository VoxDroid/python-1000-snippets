# Flask RESTful API

## Description
Demonstrates building small REST endpoints with Flask, and validates them using Flask's test client so no server needs to run.

## Files
- `SAMPLES/sample1.py` — Basic GET endpoint and response JSON.
- `SAMPLES/sample2.py` — POST endpoint that echoes a JSON payload.
- `SAMPLES/sample3.py` — Endpoint with path parameter and error handling.

## Usage
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Notes
- Scripts install `flask` if missing.
- Flask's test client runs requests in-process without listening on a network port.
