# sample1.py
# Apply DBSCAN clustering to synthetic blob data and print cluster labels.

from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs


def main() -> None:
    X, _ = make_blobs(n_samples=200, centers=3, cluster_std=0.6, random_state=0)
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(X)

    unique_labels = set(labels)
    print("Clusters found (including noise):", unique_labels)
    print("Number of clusters (excluding noise):", len(unique_labels - {-1}))

    # Print first 10 labels for inspection
    print("First 10 labels:", labels[:10])


if __name__ == "__main__":
    main()
