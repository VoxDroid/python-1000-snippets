# sample2.py
# Find top correlated item for item0 to recommend with collaborative filtering.


def top_correlated_item(correlation):
    item0 = correlation[0]
    return max((j for j in item0 if j != 0), key=lambda j: item0[j])


if __name__ == '__main__':
    corr = {0:{0:1.0,1:0.76,2:0.34}, 1:{0:0.76,1:1.0,2:0.12}, 2:{0:0.34,1:0.12,2:1.0}}
    print('Top item for item0:', top_correlated_item(corr))
