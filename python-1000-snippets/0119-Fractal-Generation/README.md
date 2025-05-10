# Fractal Generation

## Description
This snippet generates a Sierpinski triangle pattern using recursion, represented as a text-based fractal.

## Code
```python
def sierpinski_triangle(n):
    if n == 0:
        return ["*"]
    smaller = sierpinski_triangle(n-1)
    size = len(smaller)
    result = []
    # Top half: centered smaller triangle
    for line in smaller:
        result.append(" " * size + line + " " * size)
    # Bottom half: two smaller triangles
    for line in smaller:
        result.append(line + " " + line)
    return result

for line in sierpinski_triangle(2):
    print(line)
```

## Output
```
   *   
  * *  
 *   * 
* * * *
```

## Explanation
- **Sierpinski Triangle**: A recursive fractal formed by dividing a triangle into smaller triangles.
- **Logic**: Each level combines a centered smaller triangle (top) with two side-by-side triangles (bottom).
- **Complexity**: O(2^n) time for depth n.
- **Use Case**: Used in fractal studies or computer graphics.
- **Best Practice**: Visualize with graphics; optimize for large depths.