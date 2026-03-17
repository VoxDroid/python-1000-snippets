"""Compute the length of the longest increasing subsequence (LIS)."""

from typing import List


def lis_length(arr: List[int]) -> int:
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == "__main__":
    arr = [3, 1, 5, 2, 6, 4, 9]
    print("Array:", arr)
    print("LIS length =", lis_length(arr))
