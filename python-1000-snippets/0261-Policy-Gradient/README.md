# Policy Gradient

## Description
This snippet demonstrates a simple policy gradient (REINFORCE) algorithm using NumPy.

## Code
The `SAMPLES/` folder includes:

- `sample1.py` — shows how a softmax policy produces action probabilities for a given state.
- `sample2.py` — trains a policy using REINFORCE on a small 1D grid environment.
- `sample3.py` — trains a policy and then evaluates the learned deterministic policy.

Run a sample with:

```bash
python python-1000-snippets/0261-Policy-Gradient/SAMPLES/sample2.py
```

## Output
Each sample prints policy behavior (probabilities), training progress, and final evaluation metrics.

## Notes
- This is a toy example: the environment is a 1D grid and the policy is linear over one-hot states.
- The core idea is to update the policy parameters in the direction of higher reward using sampled returns.
