# sample2.py
# Space-optimized knapsack using 1D array

def knapsack_opt(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i]-1, -1):
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    return dp[capacity]

if __name__ == '__main__':
    vals = [20, 5, 10, 40, 15, 25]
    wts = [1, 2, 3, 8, 7, 4]
    cap = 10
    print('max', knapsack_opt(vals, wts, cap))
