# API Rate Limiting

## Description
This snippet demonstrates rate limiting with a token bucket algorithm in Python.

## Code
- `SAMPLES/sample1.py`: token bucket limiter, requests allowed or rejected.
- `SAMPLES/sample2.py`: simulate requests and count denials.
- `SAMPLES/sample3.py`: log violations to `temp/0528_rate_limit_violations.log`.

## Output
- sample1: shows request allowed/denied status.
- sample2: prints number of denied requests.
- sample3: writes denied events to temp.

## Explanation
- **API Rate Limiting**: prevent API abuse by limiting request rate.
- **Logic**: token bucket with capacity and replenishment rate.
- **Complexity**: O(1) per request.
- **Use Case**: APIs / services under high load.
- **Best Practice**: expose headers (`X-RateLimit-*`); handle bursts; log and alert spikes.
