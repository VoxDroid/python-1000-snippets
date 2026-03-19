# sample3.py
# Generate text using a bigram model by sampling next tokens.

import random
import re
from collections import defaultdict


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def build_bigram_model(tokens: list[str]) -> dict[str, dict[str, int]]:
    model: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for a, b in zip(tokens, tokens[1:]):
        model[a][b] += 1
    return model


def sample_next(word: str, candidates: dict[str, int]) -> str:
    choices, weights = zip(*candidates.items())
    return random.choices(choices, weights=weights, k=1)[0]


def generate_text(model: dict[str, dict[str, int]], start: str, length: int = 10) -> str:
    words = [start]
    for _ in range(length - 1):
        prev = words[-1]
        if prev not in model:
            break
        words.append(sample_next(prev, model[prev]))
    return " ".join(words)


def main() -> None:
    corpus = "the quick brown fox jumps over the lazy dog"
    tokens = tokenize(corpus)
    model = build_bigram_model(tokens)

    random.seed(0)
    print("Generated text:", generate_text(model, start="the", length=12))


if __name__ == "__main__":
    main()
