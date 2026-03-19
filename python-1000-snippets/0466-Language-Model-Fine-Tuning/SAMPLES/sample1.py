# sample1.py
# Build a simple bigram language model from a small corpus.

from collections import defaultdict
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def build_bigram_model(tokens: list[str]) -> dict[tuple[str, str], int]:
    model: dict[tuple[str, str], int] = defaultdict(int)
    for a, b in zip(tokens, tokens[1:]):
        model[(a, b)] += 1
    return model


def main() -> None:
    corpus = """
    The quick brown fox jumps over the lazy dog.
    The quick brown fox is quick.
    """

    tokens = tokenize(corpus)
    model = build_bigram_model(tokens)

    print("Total tokens:", len(tokens))
    print("Total bigrams:", len(model))
    print("Samples from bigram model:")
    for k, v in list(model.items())[:5]:
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
