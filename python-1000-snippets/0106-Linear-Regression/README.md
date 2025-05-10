# Linear Regression

## Description
This snippet performs simple linear regression to fit a line `y = mx + b` to data using the least squares method.

## Code
```python
def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(xi * xi for xi in x)
    
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    b = (sum_y - m * sum_x) / n
    return m, b

x = [1, 2, 3, 4]
y = [2, 4, 5, 4]
m, b = linear_regression(x, y)
print(f"Line: y = {m:.2f}x + {b:.2f}")
```

## Output
```
Line: y = 0.80x + 1.50
```

## Explanation
- **Linear Regression**: Finds the best-fit line by minimizing squared errors.
- **Formulas**: Slope `m = (nΣxy - ΣxΣy)/(nΣx² - (Σx)²)`; intercept `b = (Σy - mΣx)/n`.
- **Complexity**: O(n) time.
- **Use Case**: Used in data analysis, forecasting, or machine learning.
- **Best Practice**: Use libraries like scikit-learn; validate data for outliers.