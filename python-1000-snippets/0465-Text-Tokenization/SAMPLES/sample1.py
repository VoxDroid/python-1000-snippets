# sample1.py
# Simple whitespace + punctuation tokenization.

import re


def tokenize(text: str) -> list[str]:
    # Split on whitespace and punctuation, keeping contractions intact.
    return [tok for tok in re.findall(r"\w+|'\w+|\S", text) if tok.strip()]


def main() -> None:
    text = "Hello, world! This is a test: tokenization."  # sample input
    tokens = tokenize(text)

    print("Input:", text)
    print("Tokens:", tokens)
    print("Token count:", len(tokens))


if __name__ == "__main__":
    main()
