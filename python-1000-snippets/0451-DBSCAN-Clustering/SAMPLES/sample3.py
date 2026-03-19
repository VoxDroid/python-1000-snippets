# sample3.py
# Show how tuning eps and min_samples changes the number of clusters found.

from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs


def run_dbscan(eps: float, min_samples: int):
    X, _ = make_blobs(n_samples=200, centers=3, cluster_std=0.6, random_state=0)
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(X)
    cluster_count = len(set(labels) - {-1})
    noise_count = (labels == -1).sum()
    return cluster_count, noise_count


def main() -> None:
    for eps in (0.3, 0.5, 0.7):
        for min_samples in (3, 5, 8):
            clusters, noise = run_dbscan(eps, min_samples)
            print(f"eps={eps}, min_samples={min_samples} -> clusters={clusters}, noise={noise}")


if __name__ == "__main__":
    main()
