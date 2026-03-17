
# sample2.py
# Parse HTML from a temporary file.

import tempfile

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    print("beautifulsoup4 not installed; install with `pip install beautifulsoup4`")
else:
    html = """
    <html>
      <body>
        <h1>Title</h1>
        <p class='content'>This is a paragraph.</p>
      </body>
    </html>
    """
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".html", delete=False) as f:
        f.write(html)
        path = f.name

    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        title = soup.find("h1")
        content = soup.find("p", class_="content")
        print("Title:", title.text if title else None)
        print("Content:", content.text if content else None)
