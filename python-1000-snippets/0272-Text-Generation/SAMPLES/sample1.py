# sample1.py
# Generate text using a simple bigram (Markov chain) model.

import random


def build_bigram_model(tokens):
    model = {}
    for a, b in zip(tokens, tokens[1:]):
        model.setdefault(a, []).append(b)
    return model


def generate_text(model, start, length=20):
    result = [start]
    current = start
    for _ in range(length - 1):
        next_words = model.get(current)
        if not next_words:
            break
        current = random.choice(next_words)
        result.append(current)
    return " ".join(result)


def main():
    corpus = (
        "the quick brown fox jumps over the lazy dog "
        "the quick red fox leaped over the sleeping dog "
        "the dog chased the cat through the yard "
    )

    tokens = corpus.split()
    model = build_bigram_model(tokens)

    for start in ["the", "dog", "quick"]:
        print(f"Seed '{start}':", generate_text(model, start, length=15))


if __name__ == '__main__':
    main()
