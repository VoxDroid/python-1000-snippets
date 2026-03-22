# sample2.py
# Choose the best item from hybrid recommendations.


def top_recommendation(scores):
    return max(range(len(scores)), key=lambda i: scores[i])


if __name__ == '__main__':
    scores = [0.7, 0.55, 0.4]
    print('Top recommendation index:', top_recommendation(scores))
