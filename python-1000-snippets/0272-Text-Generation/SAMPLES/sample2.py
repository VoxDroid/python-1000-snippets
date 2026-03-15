# sample2.py
# Simple trigram model: predict next word given two previous words.

import random
from collections import defaultdict


def build_trigram_model(tokens):
    model = defaultdict(list)
    for a, b, c in zip(tokens, tokens[1:], tokens[2:]):
        model[(a, b)].append(c)
    return model


def generate_text(model, start, length=20):
    result = list(start)
    for _ in range(length - 2):
        key = (result[-2], result[-1])
        candidates = model.get(key)
        if not candidates:
            break
        result.append(random.choice(candidates))
    return " ".join(result)


def main():
    corpus = (
        "to be or not to be that is the question "
        "whether tis nobler in the mind to suffer "
        "the slings and arrows of outrageous fortune "
    )

    tokens = corpus.split()
    model = build_trigram_model(tokens)

    seed = ("to", "be")
    print("Seed", seed, ":", generate_text(model, seed, length=20))


if __name__ == '__main__':
    main()
