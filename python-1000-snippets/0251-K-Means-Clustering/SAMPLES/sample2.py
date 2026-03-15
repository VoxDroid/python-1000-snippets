# sample2.py
# Use the elbow method (inertia) to inspect how K affects clustering.

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def main():
    X, _ = make_blobs(n_samples=200, centers=4, cluster_std=0.60, random_state=42)

    inertias = []
    for k in range(1, 6):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)

    print("K values:", list(range(1, 6)))
    print("Inertias:", inertias)


if __name__ == "__main__":
    main()
