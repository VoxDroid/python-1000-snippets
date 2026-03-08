# URL Parsing Cheatsheet

## urlparse
```python
from urllib.parse import urlparse
p = urlparse('https://example.com/path?x=1')
print(p.scheme, p.netloc, p.path, p.query)
```

## parse_qs and parse_qsl
```python
from urllib.parse import parse_qs
qs = parse_qs('a=1&a=2&b=3')
```

## urlunparse/urljoin
```python
from urllib.parse import urlunparse
urlunparse(('https','example.com','/','', 'a=1',''))
```

## Tips
- `urlparse` returns a namedtuple with attributes: scheme, netloc, path, params, query, fragment.
- Use `urlsplit` if you don't need params.
- To modify query parameters, parse them, update dict, and reconstruct with `urlencode`.

## Running samples
Activate venv then run `SAMPLES/sample*.py`.
