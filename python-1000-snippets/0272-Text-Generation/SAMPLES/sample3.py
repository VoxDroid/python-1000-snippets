# sample3.py
# Simple character-level Markov text generator.

import random
from collections import defaultdict


def build_char_model(text):
    model = defaultdict(list)
    for a, b in zip(text, text[1:]):
        model[a].append(b)
    return model


def generate_chars(model, start, length=100):
    result = [start]
    current = start
    for _ in range(length - 1):
        next_chars = model.get(current)
        if not next_chars:
            break
        current = random.choice(next_chars)
        result.append(current)
    return "".join(result)


def main():
    prompt = "In a hole in the ground there lived a hobbit."
    model = build_char_model(prompt)

    print("Seed:", prompt)
    print("Generated:", generate_chars(model, prompt[0], length=200))


if __name__ == '__main__':
    main()
