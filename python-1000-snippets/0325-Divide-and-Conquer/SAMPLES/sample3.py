"""Quickselect algorithm to find the k-th smallest element."""

from typing import List


def quickselect(arr: List[int], k: int) -> int:
    if not 0 <= k < len(arr):
        raise IndexError("k is out of range")

    def select(a: List[int], lo: int, hi: int, k_idx: int) -> int:
        if lo == hi:
            return a[lo]
        pivot = a[(lo + hi) // 2]
        left = lo
        right = hi
        while left <= right:
            while a[left] < pivot:
                left += 1
            while a[right] > pivot:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        if k_idx <= right:
            return select(a, lo, right, k_idx)
        if k_idx >= left:
            return select(a, left, hi, k_idx)
        return a[k_idx]

    # Work on a copy to avoid mutating original list
    return select(list(arr), 0, len(arr) - 1, k)


if __name__ == "__main__":
    arr = [7, 2, 1, 6, 8, 5, 3, 4]
    k = 2  # 0-based index for 3rd smallest
    print(f"Array: {arr}")
    print(f"{k+1}rd smallest element: {quickselect(arr, k)}")
