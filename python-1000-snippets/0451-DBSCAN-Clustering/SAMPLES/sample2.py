# sample2.py
# Detect noise points (label = -1) produced by DBSCAN.

from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs


def main() -> None:
    X, _ = make_blobs(n_samples=250, centers=3, cluster_std=0.8, random_state=1)
    dbscan = DBSCAN(eps=0.4, min_samples=5)
    labels = dbscan.fit_predict(X)

    noise_mask = labels == -1
    print("Total points:", len(labels))
    print("Noise points:", noise_mask.sum())
    print("Sample noise indices:", [i for i, v in enumerate(noise_mask) if v][:10])


if __name__ == "__main__":
    main()
