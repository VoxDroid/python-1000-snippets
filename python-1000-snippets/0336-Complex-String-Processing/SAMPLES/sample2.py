"""Extract emails and URLs from text using regular expressions."""

import re
from typing import List, Tuple


def extract_contacts(text: str) -> Tuple[List[str], List[str]]:
    emails = re.findall(r"[\w.%-]+@[\w.-]+\.[A-Za-z]{2,6}", text)
    urls = re.findall(r"https?://\S+", text)
    return emails, urls


if __name__ == "__main__":
    text = "Contact us at user@example.com or visit https://example.com for more info."
    emails, urls = extract_contacts(text)
    print("Emails:", emails)
    print("URLs:", urls)
