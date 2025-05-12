# Dynamic HTML Scraping

## Description
This snippet demonstrates HTML scraping using `beautifulsoup4`.

## Code
```python
# Note: Requires `beautifulsoup4`. Install with `pip install beautifulsoup4`
try:
    from bs4 import BeautifulSoup
    html = "<div class='item'>Data</div>"
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find('div', class_='item').text
    print("Scraped:", data)
except ImportError:
    print("Mock Output: Scraped: Data")
```

## Output
```
Mock Output: Scraped: Data
```
*(Real output with `beautifulsoup4`: `Scraped: Data`)*

## Explanation
- **Dynamic HTML Scraping**: Extracts data from HTML using CSS selectors.
- **Logic**: Parses HTML with `BeautifulSoup` and extracts text from a div.
- **Complexity**: O(n) for n nodes in HTML.
- **Use Case**: Used for web scraping or data extraction.
- **Best Practice**: Handle missing elements; respect robots.txt; use robust selectors.