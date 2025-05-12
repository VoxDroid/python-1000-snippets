# Custom Sorting Algorithms

## Description
This snippet demonstrates a bubble sort implementation.

## Code
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Sorted:", bubble_sort([4, 2, 5, 1, 3]))
```

## Output
```
Sorted: [1, 2, 3, 4, 5]
```

## Explanation
- **Custom Sorting Algorithms**: Implements bubble sort to sort a list.
- **Logic**: Repeatedly swaps adjacent elements if out of order.
- **Complexity**: O(n^2) for n elements.
- **Use Case**: Used for educational purposes or small datasets.
- **Best Practice**: Use built-in sorting; optimize comparisons; validate inputs.