"""Subset sum using branch-and-bound with pruning based on remaining sum."""

from typing import List


def subset_sum_branch_and_bound(nums: List[int], target: int) -> bool:
    nums = sorted(nums, reverse=True)
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums) - 1, -1, -1):
        prefix_sum[i] = prefix_sum[i + 1] + nums[i]

    def search(i: int, current: int) -> bool:
        if current == target:
            return True
        if current > target or i == len(nums):
            return False
        # If even taking all remaining items can't reach target, prune
        if current + prefix_sum[i] < target:
            return False
        # Choose current item
        if search(i + 1, current + nums[i]):
            return True
        # Skip current item
        return search(i + 1, current)

    return search(0, 0)


if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    found = subset_sum_branch_and_bound(nums, target)
    print(f"Subset sum target {target}: {found}")
