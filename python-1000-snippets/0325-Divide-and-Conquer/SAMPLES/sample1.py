"""Merge sort: divide, sort, and merge subarrays."""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    arr = [5, 2, 8, 3, 1, 7, 4, 6]
    print("Unsorted:", arr)
    print("Sorted:", merge_sort(arr))
