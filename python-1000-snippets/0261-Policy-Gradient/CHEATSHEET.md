# Policy Gradient Cheatsheet

## Key Concepts
- **Policy**: parameterized distribution over actions (here: softmax over logits).
- **REINFORCE**: a Monte Carlo policy gradient method that updates policy weights by the return.
- **Return normalization**: subtracting mean and dividing by std of returns stabilizes training.

## Running Samples
```bash
python python-1000-snippets/0261-Policy-Gradient/SAMPLES/sample1.py
python python-1000-snippets/0261-Policy-Gradient/SAMPLES/sample2.py
python python-1000-snippets/0261-Policy-Gradient/SAMPLES/sample3.py
```

## Tips
- Use a small environment for debugging before scaling to larger tasks.
- A baseline (e.g., average return) can reduce gradient variance.
- Policy gradients can be noisy; increase episodes or use smaller learning rates if needed.
