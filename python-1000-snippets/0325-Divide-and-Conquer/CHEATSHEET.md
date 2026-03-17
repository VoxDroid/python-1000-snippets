# 0325-Divide-and-Conquer Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Merge sort
python SAMPLES/sample2.py  # Binary search
python SAMPLES/sample3.py  # Quickselect (kth smallest)
```

## Tips
- Divide the problem into smaller subproblems, solve recursively, and combine.
- Always include base cases to stop recursion.
- Ensure the merge step handles all possible sub-results.

## Common patterns
- Sorting: split, sort halves, merge.
- Searching: reduce search space by half each time.
- Selection: use recursion to avoid sorting entire collection.

## Example outline (merge sort)
```python
if len(arr) <= 1:
    return arr
mid = len(arr) // 2
left = merge_sort(arr[:mid])
right = merge_sort(arr[mid:])
return merge(left, right)
```
