# Backtracking

## Description
This snippet demonstrates backtracking to solve a simple permutation problem.

## Code
```python
def permute(nums):
    result = []
    def backtrack(path, options):
        if not options:
            result.append(path[:])
        for i in range(len(options)):
            path.append(options[i])
            backtrack(path, options[:i] + options[i+1:])
            path.pop()
    backtrack([], nums)
    return result

print("Permutations:", permute([1, 2]))
```

## Output
```
Permutations: [[1, 2], [2, 1]]
```

## Explanation
- **Backtracking**: Generates all permutations of a list.
- **Logic**: Builds permutations by exploring choices and undoing them.
- **Complexity**: O(n!) for n elements.
- **Use Case**: Used for puzzles like Sudoku or N-Queens.
- **Best Practice**: Prune branches; optimize recursion; validate inputs.