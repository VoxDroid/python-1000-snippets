# sample1.py
# Compute user-user cosine similarity using pure Python.

import math


def cosine_similarity(u, v):
    dot = sum(ui * vi for ui, vi in zip(u, v))
    norm_u = math.sqrt(sum(ui * ui for ui in u))
    norm_v = math.sqrt(sum(vi * vi for vi in v))
    return dot / (norm_u * norm_v) if norm_u > 0 and norm_v > 0 else 0.0


def user_similarity_matrix(users):
    n = len(users)
    sim = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sim[i][j] = round(cosine_similarity(users[i], users[j]), 2)
    return sim


if __name__ == '__main__':
    user_item = [[5, 3, 0], [4, 0, 0], [0, 2, 3]]
    print('Similarity matrix:', user_similarity_matrix(user_item))
