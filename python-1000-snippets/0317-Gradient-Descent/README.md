# Gradient Descent

## Description
This snippet implements gradient descent for continuous optimization. Gradient descent iteratively updates parameters in the direction of negative gradient.

## Files
- `SAMPLES/sample1.py`: Gradient descent on a 2D quadratic function with analytic gradient.
- `SAMPLES/sample2.py`: Gradient descent on a shifted quadratic function.
- `SAMPLES/sample3.py`: Gradient descent with numerical gradient (finite differences) on a multimodal function.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Best solution: [0.00 0.00], loss: 0.0000
Best solution: [1.00 -2.00], loss: 0.0000
Best solution: [1.57], loss: -0.98
```

## Explanation
- **Learning rate**: Step size controlling convergence speed.
- **Gradient**: Direction of steepest ascent; descent uses negative gradient.
- **Stopping criteria**: Number of iterations or small gradient norm.
- **Use Case**: Machine learning training, optimization problems.
