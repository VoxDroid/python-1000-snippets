# sample2.py
try:
    from bs4 import BeautifulSoup
    html = "<ul><li>A</li><li>B</li></ul>"
    soup = BeautifulSoup(html, "html.parser")
    for li in soup.find_all("li"):
        print("item", li.text)
except ImportError:
    print("mock items")

