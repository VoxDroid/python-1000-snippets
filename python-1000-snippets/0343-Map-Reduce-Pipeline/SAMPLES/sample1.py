# sample1.py
# Word frequency counter using map/reduce

from functools import reduce
import re


def word_counts(text):
    words = re.findall(r"\b\w+\b", text.lower())
    counts = reduce(
        lambda acc, w: {**acc, w: acc.get(w, 0) + 1},
        words,
        {},
    )
    return counts


def main():
    text = "To be, or not to be: that is the question."
    print("text:", text)
    print("word counts:", word_counts(text))


if __name__ == "__main__":
    main()
