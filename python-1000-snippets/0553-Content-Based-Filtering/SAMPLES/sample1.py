# sample1.py
# Compute content-based scores based on user preference vector.


def score_items(items, user_pref):
    return [sum(i * p for i, p in zip(item, user_pref)) for item in items]


if __name__ == '__main__':
    item_features = [[1, 0], [0, 1], [1, 1]]
    user_pref = [1, 0]
    print('Recommendation scores:', score_items(item_features, user_pref))
