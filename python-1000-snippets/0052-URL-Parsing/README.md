# URL Parsing

## Description
This snippet demonstrates parsing a URL into its components (e.g., scheme, host, path) using the `urllib.parse` module.

## Code
```python
from urllib.parse import urlparse

url = input("Enter a URL: ")
parsed = urlparse(url)
print("Scheme:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)
```

## Output
```
Enter a URL: https://example.com/path/to/page
Scheme: https
Netloc: example.com
Path: /path/to/page
```

## Explanation
- **urlparse()**: Breaks a URL into components: `scheme` (e.g., `https`), `netloc` (domain), `path`, `params`, `query`, and `fragment`.
- **Input**: Accepts any valid URL (e.g., HTTP, HTTPS, FTP).
- **Use Case**: URL parsing is used in web scraping, API clients, or link analysis.
- **Error Handling**: Invalid URLs may raise exceptions or produce unexpected results; add validation in production.
- **Best Practice**: Use `urllib.parse` for robust URL handling; validate URLs before parsing.