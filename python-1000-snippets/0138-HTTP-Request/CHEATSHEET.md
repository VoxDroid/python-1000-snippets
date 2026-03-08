# 0138-HTTP-Request Cheatsheet

- **Purpose**: perform HTTP GET requests using the `requests` library.
- **Installation**: `pip install requests`.
- **Basic usage**:
  ```python
  import requests
  r = requests.get('https://example.com', timeout=5)
  if r.ok:
      data = r.json()  # or r.text
  ```
- **Error handling**: catch `requests.exceptions.RequestException` for network issues.
- **Mocking**: provide a fallback dict when the library is absent or network unreachable.

```python
try:
    import requests
    print(requests.get('https://httpbin.org/get').json())
except Exception:
    print('Mock Response: {...}')
```

- Use timeouts and check `status_code`.
- For POST/headers/authentication, refer to requests docs.

