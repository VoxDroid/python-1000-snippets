# sample1.py
# Compute hybrid scores by mixing collaborative and content scores.


def hybrid_scores(collab_scores, content_scores, alpha=0.5):
    return [round(alpha * c + (1-alpha) * d, 2) for c, d in zip(collab_scores, content_scores)]


if __name__ == '__main__':
    collab = [0.8, 0.2, 0.5]
    content = [0.6, 0.9, 0.3]
    print('Hybrid scores:', hybrid_scores(collab, content))
