# HTML Parsing

## Description
This snippet demonstrates parsing HTML using `beautifulsoup4`.

## Code
```python
# Note: Requires `beautifulsoup4`. Install with `pip install beautifulsoup4`
try:
    from bs4 import BeautifulSoup
    html_content = """
    <html>
        <body>
            <h1>Welcome</h1>
            <p class="info">Hello, World!</p>
        </body>
    </html>
    """
    soup = BeautifulSoup(html_content, "html.parser")
    print("Title:", soup.h1.text)
    print("Paragraph:", soup.find("p", class_="info").text)
except ImportError:
    print("Mock Output: Title: Welcome, Paragraph: Hello, World!")
```

## Output
```
Mock Output: Title: Welcome, Paragraph: Hello, World!
```
*(Real output with `beautifulsoup4`: `Title: Welcome, Paragraph: Hello, World!`)*

## Explanation
- **HTML Parsing**: Uses `BeautifulSoup` to parse HTML and extract elements.
- **Logic**: Accesses `h1` text and a `p` element by class.
- **Complexity**: O(n) for parsing n bytes of HTML.
- **Use Case**: Used for web scraping or data extraction.
- **Best Practice**: Use specific selectors; handle malformed HTML; respect robots.txt.