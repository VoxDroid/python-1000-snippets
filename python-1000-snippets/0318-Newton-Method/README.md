# Newton Method

## Description
This snippet demonstrates Newton’s method (Newton-Raphson) for root-finding and optimization using first and second derivatives.

## Files
- `SAMPLES/sample1.py`: Find sqrt(2) by solving x^2 - 2 = 0.
- `SAMPLES/sample2.py`: Find a root of a cubic polynomial.
- `SAMPLES/sample3.py`: Use Newton's method to find a critical point (optimize) of a function.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Root (sqrt2): 1.41421356237
Root (cubic): 1.0000
Optimum x: 0.00, f(x)=0.00
```

## Explanation
- **Newton’s method**: x_{n+1} = x_n - f(x)/f'(x).
- **Optimizer version**: Use gradient and Hessian to find stationary points.
- **Use Case**: Root-finding, optimization, numerical analysis.
