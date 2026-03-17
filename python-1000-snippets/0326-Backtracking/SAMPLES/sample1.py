"""Generate all permutations of a list using backtracking."""

from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    results: List[List[int]] = []

    def backtrack(curr: List[int]):
        if len(curr) == len(nums):
            results.append(list(curr))
            return
        for x in nums:
            if x in curr:
                continue
            curr.append(x)
            backtrack(curr)
            curr.pop()

    backtrack([])
    return results


if __name__ == "__main__":
    nums = [1, 2, 3]
    perms = permutations(nums)
    print("Permutations:", perms)
