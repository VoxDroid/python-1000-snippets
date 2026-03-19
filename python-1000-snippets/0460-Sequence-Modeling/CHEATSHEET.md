# 0460-Sequence-Modeling Cheatsheet

## Quick Tips
- **Sequence modeling** expects inputs where order matters (e.g., time series, tokens).
- Use lag features (previous timesteps) to convert sequence prediction into a standard regression/classification problem.
- For simple demonstrations, a lightweight custom RNN/LSTM using NumPy can illustrate recurrence without heavy dependencies.

## Running examples
- `python SAMPLES/sample1.py` — minimal LSTM forward pass (NumPy).
- `python SAMPLES/sample2.py` — lag feature regression (scikit-learn).
- `python SAMPLES/sample3.py` — sequence classification (k-NN on synthetic waveforms).
