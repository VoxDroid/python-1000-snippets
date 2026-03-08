# sample1.py
# Basic 0/1 knapsack using 2D table

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

if __name__ == '__main__':
    vals = [60, 100, 120]
    wts = [10, 20, 30]
    cap = 50
    print('max value', knapsack(vals, wts, cap))
