
# sample1.py
# Parse a simple HTML string.

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    print("beautifulsoup4 not installed; install with `pip install beautifulsoup4`")
else:
    html = "<div><span class='item'>Hello</span></div>"
    soup = BeautifulSoup(html, "html.parser")
    item = soup.find("span", class_="item")
    print("Found:", item.text if item else None)
