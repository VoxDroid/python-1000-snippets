"""Binary search on a sorted list (divide-and-conquer)."""

from typing import List


def binary_search(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 5
    idx = binary_search(arr, target)
    print(f"Found {target} at index {idx}")
