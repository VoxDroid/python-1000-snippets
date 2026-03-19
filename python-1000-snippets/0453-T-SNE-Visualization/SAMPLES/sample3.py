# sample3.py
# Compare t-SNE perplexity settings for the same dataset.

from sklearn.datasets import load_iris
from sklearn.manifold import TSNE


def main() -> None:
    data = load_iris(as_frame=True)
    X = data.data

    for perplexity in (5, 30, 50):
        tsne = TSNE(n_components=2, random_state=0, perplexity=perplexity, init="pca")
        embedding = tsne.fit_transform(X)
        print(f"perplexity={perplexity}, sample[0]={embedding[0][0]:.3f},{embedding[0][1]:.3f}")


if __name__ == "__main__":
    main()
