# sample1.py
# Perform K-Means clustering on synthetic data and print cluster centers.

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def main():
    X, _ = make_blobs(n_samples=150, centers=3, cluster_std=0.60, random_state=42)

    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)

    print("Cluster centers:", kmeans.cluster_centers_)
    print("First 10 labels:", labels[:10].tolist())


if __name__ == "__main__":
    main()
