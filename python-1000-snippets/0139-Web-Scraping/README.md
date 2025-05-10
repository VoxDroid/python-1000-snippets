# Web Scraping

## Description
This snippet scrapes a mock webpage’s title using `requests` and `beautifulsoup4`.

## Code
```python
# Note: Requires `requests` and `beautifulsoup4`. Install with `pip install requests beautifulsoup4`
try:
    import requests
    from bs4 import BeautifulSoup
    response = requests.get("https://example.com")
    soup = BeautifulSoup(response.text, "html.parser")
    print("Title:", soup.title.string)
except ImportError:
    print("Mock Title: Example Domain")
```

## Output
```
Mock Title: Example Domain
```
*(Real output with libraries: `Title: Example Domain`)*

## Explanation
- **Web Scraping**: Uses `requests` to fetch HTML and `BeautifulSoup` to parse and extract the `<title>`.
- **Mock**: Provides a static title if libraries are unavailable.
- **Complexity**: O(n) for parsing n bytes of HTML.
- **Use Case**: Used for data extraction or monitoring websites.
- **Best Practice**: Respect robots.txt; handle parsing errors; use specific selectors.