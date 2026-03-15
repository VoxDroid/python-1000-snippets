# sample3.py
# Assign new points to existing clusters from a trained K-Means model.

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def main():
    X, _ = make_blobs(n_samples=150, centers=3, cluster_std=0.60, random_state=42)

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)

    # New points to classify
    new_points = [[-2, 2], [0, 0], [2, -2]]
    labels = kmeans.predict(new_points)

    print("New points:", new_points)
    print("Assigned cluster labels:", labels.tolist())
    print("Cluster centers:", kmeans.cluster_centers_)


if __name__ == "__main__":
    main()
