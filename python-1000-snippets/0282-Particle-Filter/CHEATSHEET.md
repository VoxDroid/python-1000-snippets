# 0282 - Particle Filter Cheatsheet

## Quick Commands
```bash
pip install numpy
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use `weights *= likelihood` and normalize to update particle weights.
- Effective sample size (ESS): `1 / np.sum(weights**2)`.
- Resample when ESS drops (e.g., below N/2) to avoid particle degeneracy.
- Use systematic resampling for better diversity than naive sampling.
