# Multiprocessing

## Description
This snippet uses `multiprocessing` to compute squares of numbers in parallel.

## Code
```python
from multiprocessing import Pool

def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]
with Pool(2) as pool:
    results = pool.map(square, numbers)
print("Squares:", results)
```

## Output
```
Squares: [1, 4, 9, 16, 25]
```

## Explanation
- **Multiprocessing**: Uses `Pool` to run `square` function across multiple processes, bypassing Python’s GIL.
- **Logic**: Maps `square` to a list of numbers, distributing work to 2 processes.
- **Complexity**: O(n) time, parallelized across processes.
- **Use Case**: Used for CPU-bound tasks like computations or data processing.
- **Best Practice**: Close pools; handle process failures; optimize process count.