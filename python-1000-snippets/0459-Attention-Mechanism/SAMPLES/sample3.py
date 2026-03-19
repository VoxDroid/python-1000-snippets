# sample3.py
# Show that attention weights sum to 1 along the key dimension.

import numpy as np
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE


def scaled_dot_product_attention(q, k, v):
    dk = q.shape[-1]
    scores = q @ k.T / np.sqrt(dk)
    weights = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    weights = weights / np.sum(weights, axis=-1, keepdims=True)
    return weights, weights.sum(axis=-1)


def main() -> None:
    # Use a larger subset of iris to avoid issues with perplexity.
    iris = load_iris(as_frame=True)
    X = iris.data[:100]

    # Use t-SNE to get a set of embeddings as query/key vectors
    tsne = TSNE(n_components=3, random_state=0, init="pca")
    emb = tsne.fit_transform(X)

    weights, sums = scaled_dot_product_attention(emb, emb, emb)
    print("Attention weight sums (should be 1):", sums)


if __name__ == "__main__":
    main()
