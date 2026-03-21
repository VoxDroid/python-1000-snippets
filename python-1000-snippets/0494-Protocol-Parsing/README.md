# Protocol Parsing

## Description
This snippet demonstrates parsing HTTP headers using `http.client`.

## Code
```python
try:
    from http.client import parse_headers
    from io import BytesIO
    headers = b"Content-Type: text/html\r\nHost: example.com\r\n\r\n"
    parsed = parse_headers(BytesIO(headers))
    print("Parsed headers:", dict(parsed))
except ImportError:
    print("Mock Output: Parsed headers: {'Content-Type': 'text/html', 'Host': 'example.com'}")
```

## Output
`sample1.py` prints parsed HTTP headers.
`sample2.py` prints parsed query parameters.
`sample3.py` validates JSON payload protocol object.

## Explanation
- **Protocol Parsing**: Handles HTTP header text, URL query strings, and JSON message bodies.
- **Logic**: String splitting and JSON parsing with validation.
- **Complexity**: O(n) for n fields.
- **Use Case**: Useful for implementing lightweight protocol parsing without external libs.
- **Best Practice**: Sanitize input and handle malformed values robustly.