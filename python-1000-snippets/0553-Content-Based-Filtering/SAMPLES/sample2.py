# sample2.py
# Select top score item index for content-based filtering.


def best_item(items, user_pref):
    scores = [sum(i * p for i, p in zip(item, user_pref)) for item in items]
    return max(range(len(scores)), key=lambda idx: scores[idx])


if __name__ == '__main__':
    item_features = [[1, 0], [0, 1], [1, 1]]
    user_pref = [1, 0]
    print('Best item index:', best_item(item_features, user_pref))
