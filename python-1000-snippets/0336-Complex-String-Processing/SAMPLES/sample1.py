"""Compute word frequency from a block of text with basic normalization."""

import re
from collections import Counter


def normalize_text(text: str) -> str:
    # Lowercase and remove punctuation
    return re.sub(r"[^\w\s]", "", text.lower())


def word_frequency(text: str):
    tokens = re.findall(r"\w+", normalize_text(text))
    return Counter(tokens)


if __name__ == "__main__":
    text = "Hello, world! Hello to the world of Python."
    freq = word_frequency(text)
    print("Word frequencies:", dict(freq))
