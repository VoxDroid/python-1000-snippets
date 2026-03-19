# sample1.py
# Run Agglomerative hierarchical clustering on the iris dataset.

from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris


def main() -> None:
    data = load_iris(as_frame=True)
    X = data.data

    clustering = AgglomerativeClustering(n_clusters=3)
    labels = clustering.fit_predict(X)

    unique, counts = np.unique(labels, return_counts=True)
    print("Cluster counts:", dict(zip(unique, counts)))
    print("First 10 labels:", labels[:10])


if __name__ == "__main__":
    import numpy as np

    main()
