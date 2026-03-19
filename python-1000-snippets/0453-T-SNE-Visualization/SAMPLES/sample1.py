# sample1.py
# Run t-SNE on the iris dataset and print the first few 2D embeddings.

from sklearn.datasets import load_iris
from sklearn.manifold import TSNE


def main() -> None:
    data = load_iris(as_frame=True)
    X = data.data

    tsne = TSNE(n_components=2, random_state=0, init="pca")
    embedding = tsne.fit_transform(X)

    print("Embedding shape:", embedding.shape)
    print("First 5 points:")
    for i, (x, y) in enumerate(embedding[:5]):
        print(f"  {i}: ({x:.3f}, {y:.3f})")


if __name__ == "__main__":
    main()
