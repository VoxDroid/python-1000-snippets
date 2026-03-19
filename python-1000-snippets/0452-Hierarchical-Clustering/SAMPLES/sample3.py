# sample3.py
# Demonstrate how changing linkage affects hierarchical clustering results.

from scipy.cluster.hierarchy import linkage
from sklearn.datasets import load_iris


def cluster_and_count(method: str):
    data = load_iris(as_frame=True)
    X = data.data
    Z = linkage(X, method=method)
    # In hierarchical clustering, there are (n-1) merges
    return Z.shape[0]


def main() -> None:
    methods = ["single", "complete", "average", "ward"]
    for m in methods:
        merges = cluster_and_count(m)
        print(f"Linkage={m}, merges={merges}")


if __name__ == "__main__":
    main()
