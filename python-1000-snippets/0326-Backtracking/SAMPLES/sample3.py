"""Subset sum using backtracking."""

from typing import List


def subset_sum(nums: List[int], target: int) -> bool:
    def backtrack(i: int, current: int) -> bool:
        if current == target:
            return True
        if i == len(nums) or current > target:
            return False
        # Choose current element
        if backtrack(i + 1, current + nums[i]):
            return True
        # Skip current element
        return backtrack(i + 1, current)

    return backtrack(0, 0)


if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    found = subset_sum(nums, target)
    print(f"Subset sum for target {target}: {found}")
