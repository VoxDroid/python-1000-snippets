# Sequence Modeling

## Description
This snippet demonstrates basic sequence modeling techniques using NumPy and scikit-learn.

## Running
Run the included examples:

```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Sample output (from `sample1.py`)
```
Input sequence: [0.         0.14285714 0.28571429 0.42857143 0.57142857 0.71428571
 0.85714286 1.        ]
LSTM output (last time step): [ ... ]
LSTM output shape: (8, 10)
```

## Explanation
- **Sequence Modeling**: Processes ordered data (time series, tokens) where order matters.
- **sample1.py**: Implements a tiny LSTM forward pass using NumPy.
- **sample2.py**: Uses lag features + linear regression to forecast the next timestep.
- **sample3.py**: Uses k-NN to classify synthetic sequences (sine vs square waves).
- **Best Practice**: Use proper train/test splits, scale/normalize data, and use cross-validation for model selection.
