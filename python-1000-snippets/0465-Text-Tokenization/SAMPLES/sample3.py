# sample3.py
# Token frequency counting using a basic tokenizer.

from collections import Counter
import re


def simple_tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def main() -> None:
    text = "To be, or not to be, that is the question. To be sure, to be."
    tokens = simple_tokenize(text)
    freq = Counter(tokens)

    print("Tokens:", tokens)
    print("Most common tokens:", freq.most_common(3))


if __name__ == "__main__":
    main()
