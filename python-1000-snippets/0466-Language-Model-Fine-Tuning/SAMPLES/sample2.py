# sample2.py
# "Fine-tune" a simple bigram model by updating it with new text.

from collections import defaultdict
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def update_bigram_model(model: dict[tuple[str, str], int], tokens: list[str]) -> None:
    for a, b in zip(tokens, tokens[1:]):
        model[(a, b)] += 1


def main() -> None:
    base_text = "the cat sat on the mat"
    new_text = "the cat slept on the warm mat"

    tokens_base = tokenize(base_text)
    tokens_new = tokenize(new_text)

    model: dict[tuple[str, str], int] = defaultdict(int)
    update_bigram_model(model, tokens_base)

    print("Bigram count before fine-tuning:")
    print(model)

    update_bigram_model(model, tokens_new)
    print("\nBigram count after fine-tuning:")
    print(model)


if __name__ == "__main__":
    main()
