# sample1.py
# Basic k-means-like clustering for customer segmentation (pure Python).

import random


def euclidean(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def simple_kmeans(points, k=2, iterations=10):
    centroids = random.sample(points, k)
    for _ in range(iterations):
        clusters = {i: [] for i in range(k)}
        for p in points:
            best = min(range(k), key=lambda i: euclidean(p, centroids[i]))
            clusters[best].append(p)
        for i in range(k):
            if clusters[i]:
                centroid = tuple(sum(vals) / len(vals) for vals in zip(*clusters[i]))
                centroids[i] = centroid
    labels = []
    for p in points:
        labels.append(min(range(k), key=lambda i: euclidean(p, centroids[i])))
    return labels, centroids


if __name__ == '__main__':
    data = [(1, 2), (1, 4), (5, 6), (5, 8)]
    labels, centroids = simple_kmeans(data, k=2)
    print('Cluster labels:', labels)
    print('Centroids:', centroids)
