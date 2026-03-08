# 0140-API-Call Cheatsheet

- **Purpose**: obtain JSON data from a REST API using `requests`.
- **Installation**: `pip install requests`.
- **Basic GET**: `response = requests.get(url)`; use `response.json()` to parse JSON.
- **Error handling**: catch `requests.RequestException` and check `response.status_code`.
- **Timeouts**: specify `timeout=` to avoid hanging indefinitely.

```python
import requests
try:
    r = requests.get('https://api.example.com/data', timeout=3)
    r.raise_for_status()
    data = r.json()
except requests.RequestException as e:
    print('error', e)
```

- Post data with `requests.post(url, json=payload)`.
- Respect API rate limits and authentication requirements.

