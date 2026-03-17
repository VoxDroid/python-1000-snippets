# 0309 - Quantum Simulation Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Represent quantum states as complex vectors (state vectors) and gates as unitary matrices.
- Measurement probabilities are the squared magnitudes of amplitudes.
- For multi-qubit systems, use Kronecker (tensor) products to build gate matrices.
- Time evolution under a Hamiltonian is given by `exp(-i * H * dt)`.
