
# sample3.py
# Use CSS selectors to find elements.

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    print("beautifulsoup4 not installed; install with `pip install beautifulsoup4`")
else:
    html = """
    <div class='items'>
      <div class='item'>A</div>
      <div class='item'>B</div>
      <div class='item'>C</div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".items .item")
    print("Items:", [i.text for i in items])
