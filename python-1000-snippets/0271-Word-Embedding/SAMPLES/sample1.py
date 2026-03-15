# sample1.py
# Train a small Word2Vec model and inspect a word vector.

from gensim.models import Word2Vec


def main():
    # Tiny toy corpus (each sentence is a list of tokens)
    sentences = [
        "the cat sat on the mat".split(),
        "the dog chased the cat".split(),
        "the dog sat on the log".split(),
        "cats and dogs are pets".split(),
    ]

    model = Word2Vec(sentences, vector_size=10, window=2, min_count=1, epochs=50, seed=42)

    # Print the vector for a word
    cat_vec = model.wv["cat"]
    print("Vector for 'cat' (first 5 dims):", cat_vec[:5])

    # Save the model for later use (optional) - stored in the current directory
    model.save("word2vec_small.model")
    print("Saved model to word2vec_small.model")


if __name__ == "__main__":
    main()
