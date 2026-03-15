# sample2.py
# Compute word similarities using a trained Word2Vec model.

from gensim.models import Word2Vec


def main():
    sentences = [
        "the cat sat on the mat".split(),
        "the dog chased the cat".split(),
        "the dog sat on the log".split(),
        "cats and dogs are pets".split(),
    ]

    model = Word2Vec(sentences, vector_size=10, window=2, min_count=1, epochs=50, seed=42)

    # Find words most similar to 'cat'
    print("Top 3 words similar to 'cat':")
    for word, similarity in model.wv.most_similar('cat', topn=3):
        print(f"  {word}: {similarity:.4f}")


if __name__ == '__main__':
    main()
