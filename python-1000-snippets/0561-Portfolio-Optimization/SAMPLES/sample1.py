# sample1.py
# Calculate portfolio variance and risk without numpy using lists.


def portfolio_variance(weights, returns_cov):
    # returns_cov is matrix in list-of-lists
    n = len(weights)
    var = 0
    for i in range(n):
        for j in range(n):
            var += weights[i] * returns_cov[i][j] * weights[j]
    return round(var ** 0.5, 4)


if __name__ == '__main__':
    returns_cov = [[0.04, 0.01], [0.01, 0.05]]
    print('Portfolio variance:', portfolio_variance([0.5,0.5], returns_cov))
