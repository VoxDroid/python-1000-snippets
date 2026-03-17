# 0306 - Finite Element Analysis Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Assemble the global stiffness matrix by summing element contributions.
- Apply boundary conditions by removing fixed DOFs or using large penalty stiffness.
- For modal analysis, compute eigenvalues of `K` relative to mass (e.g., `eig(K, M)`).
- Keep the system size small for in-memory `numpy.linalg.solve`.
