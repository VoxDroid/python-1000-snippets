# sample2.py
# Trim whitespace and replace multiple spaces with single space.

import re

def clean(s):
    return re.sub(r"\s+", " ", s.strip())

if __name__ == '__main__':
    raw = "   This   has   extra   spaces  "
    print("Cleaned:", clean(raw))

