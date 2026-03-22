# sample2.py
# Determine optimal weights by minimum variance (brute force for 2 assets).


def portfolio_variance(weights, returns_cov):
    n = len(weights)
    var = 0
    for i in range(n):
        for j in range(n):
            var += weights[i] * returns_cov[i][j] * weights[j]
    return round(var ** 0.5, 4)


def best_weights(cov_matrix):
    best = None
    best_var = float('inf')
    for w in [i/100 for i in range(101)]:
        var = portfolio_variance([w, 1-w], cov_matrix)
        if var < best_var:
            best_var = var
            best = w
    return best, best_var


if __name__ == '__main__':
    cov = [[0.04, 0.01], [0.01, 0.05]]
    optimal, var = best_weights(cov)
    print('Optimal weight for asset1:', optimal, 'variance:', var)
