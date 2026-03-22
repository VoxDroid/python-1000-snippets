# sample1.py
# Compute item-item similarity using Pearson correlation (pure Python).

import math


def pearson(ratings1, ratings2):
    n = len(ratings1)
    mean1 = sum(ratings1) / n
    mean2 = sum(ratings2) / n
    num = sum((x-mean1)*(y-mean2) for x,y in zip(ratings1, ratings2))
    den = math.sqrt(sum((x-mean1)**2 for x in ratings1) * sum((y-mean2)**2 for y in ratings2))
    return num/den if den != 0 else 0


def item_correlation(ratings):
    # ratings: list of lists user x item
    m = len(ratings[0])
    cor = {i: {} for i in range(m)}
    for i in range(m):
        for j in range(m):
            col_i = [user[i] for user in ratings]
            col_j = [user[j] for user in ratings]
            cor[i][j] = round(pearson(col_i, col_j), 2)
    return cor


if __name__ == '__main__':
    ratings = [[5,3,0],[4,0,0],[0,2,3]]
    print('Item correlation:', item_correlation(ratings))
