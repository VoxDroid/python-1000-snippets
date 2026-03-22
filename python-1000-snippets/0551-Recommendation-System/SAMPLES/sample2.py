# sample2.py
# Recommend items for user 0 using nearest neighbor similarity.


def recommend(user_item):
    target = user_item[0]
    best_user = 1
    best_score = -1
    for i in range(1, len(user_item)):
        score = sum(ti * ui for ti, ui in zip(target, user_item[i]))
        if score > best_score:
            best_score = score
            best_user = i
    recommendations = [i for i, val in enumerate(user_item[best_user]) if target[i] == 0 and val > 0]
    return recommendations


if __name__ == '__main__':
    user_item = [[5, 3, 0], [4, 0, 0], [0, 2, 3]]
    print('Recommendations for user0:', recommend(user_item))
