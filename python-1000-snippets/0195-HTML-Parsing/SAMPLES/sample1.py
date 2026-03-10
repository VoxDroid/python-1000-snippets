# sample1.py
try:
    from bs4 import BeautifulSoup
    html = "<html><body><h1>Title</h1><p>hi</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    print("Header:", soup.h1.text)
except ImportError:
    print("BeautifulSoup not installed")

