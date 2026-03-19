# sample2.py
# Segment an image using KMeans clustering on pixel intensity values.

import numpy as np
from sklearn.cluster import KMeans


def make_gradient_image(shape=(100, 150)) -> np.ndarray:
    # Simple gradient image with a circular patch of different intensity.
    x = np.linspace(0, 255, shape[1], dtype=np.uint8)
    img = np.tile(x, (shape[0], 1))
    rr, cc = np.ogrid[: shape[0], : shape[1]]
    circle = (rr - shape[0] // 2) ** 2 + (cc - shape[1] // 2) ** 2
    img[circle < (min(shape) // 4) ** 2] = 30
    return img


def segment_kmeans(image: np.ndarray, n_clusters: int = 3) -> np.ndarray:
    flat = image.reshape(-1, 1).astype(float)
    kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=5)
    labels = kmeans.fit_predict(flat)
    return labels.reshape(image.shape), kmeans.cluster_centers_.ravel()


def main() -> None:
    img = make_gradient_image()
    segments, centers = segment_kmeans(img, n_clusters=3)

    print("Image shape:", img.shape)
    print("Cluster centers:", [round(float(c), 2) for c in centers.tolist()])
    print("Segment label counts:")
    unique, counts = np.unique(segments, return_counts=True)
    for u, c in zip(unique, counts):
        print(f"  label={u}: {c} pixels")


if __name__ == "__main__":
    main()
