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
```
Mock Output: Parsed headers: {'Content-Type': 'text/html', 'Host': 'example.com'}
```
*(Real output: `Parsed headers: {'Content-Type': 'text/html', 'Host': 'example.com'}`)*

## Explanation
- **Protocol Parsing**: Extracts HTTP header fields.
- **Logic**: Parses a byte string into a dictionary.
- **Complexity**: O(n) for n header lines.
- **Use Case**: Used in network programming or web scraping.
- **Best Practice**: Validate headers; handle malformed input; log errors.