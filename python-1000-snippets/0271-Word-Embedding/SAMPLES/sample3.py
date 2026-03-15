# sample3.py
# Compute cosine similarity between word vectors.

from gensim.models import Word2Vec
import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def main():
    sentences = [
        "the cat sat on the mat".split(),
        "the dog chased the cat".split(),
        "the dog sat on the log".split(),
        "cats and dogs are pets".split(),
    ]

    model = Word2Vec(sentences, vector_size=10, window=2, min_count=1, epochs=50, seed=42)

    cat_vec = model.wv["cat"]
    dog_vec = model.wv["dog"]
    mat_vec = model.wv["mat"]

    print("Cosine similarity cat/dog:", cosine_similarity(cat_vec, dog_vec))
    print("Cosine similarity cat/mat:", cosine_similarity(cat_vec, mat_vec))


if __name__ == '__main__':
    main()
