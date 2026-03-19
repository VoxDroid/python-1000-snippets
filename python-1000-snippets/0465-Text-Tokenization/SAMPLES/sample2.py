# sample2.py
# Demonstrate subword-like tokenization by splitting on common prefixes.

from collections import Counter


def wordpiece_tokenize(word: str, vocab: set[str]) -> list[str]:
    # A simplified WordPiece-style tokenizer.
    tokens = []
    i = 0
    while i < len(word):
        match = None
        for j in range(len(word), i, -1):
            piece = word[i:j]
            if piece in vocab:
                match = piece
                break
        if match is None:
            tokens.append(word[i])
            i += 1
        else:
            tokens.append(match)
            i = j
    return tokens


def main() -> None:
    vocab = {"the", "re", "##ing", "##ed", "test", "token", "##ization"}
    word = "tokenization"

    tokenized = wordpiece_tokenize(word, vocab)

    print("Word:", word)
    print("WordPiece-like tokens:", tokenized)


if __name__ == "__main__":
    main()
