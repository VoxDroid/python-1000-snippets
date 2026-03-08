# sample3.py
# Retrieve chosen items from knapsack table

def knapsack_with_items(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    # backtrack
    res = dp[n][capacity]
    w = capacity
    items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i-1)
            w -= weights[i-1]
    return res, list(reversed(items))

if __name__ == '__main__':
    vals = [60, 100, 120]
    wts = [10, 20, 30]
    cap = 50
    print('result', knapsack_with_items(vals, wts, cap))
