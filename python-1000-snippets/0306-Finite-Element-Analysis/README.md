# Finite Element Analysis

## Description
This snippet provides small finite element analysis (FEA) examples using `numpy` for matrix assembly and linear algebra. The examples illustrate:
- 1D axial bar stiffness
- Natural frequency (eigenvalue) computation
- 2D truss analysis

## Files
- `SAMPLES/sample1.py`: Axial bar under tension with fixed boundary conditions.
- `SAMPLES/sample2.py`: Computes natural frequencies of a free-free bar using eigenvalues.
- `SAMPLES/sample3.py`: 2D triangular truss under point load.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Displacements: [0.00000000e+00 4.76190476e-05 9.52380952e-05 1.90476190e-04]
Natural frequencies (rad/s): [1.72e+03 3.43e+03 5.15e+03]
Truss displacements: [0.0000 0.0000 0.0000 -0.0003 0.0000 -0.0003]
```

## Explanation
- **Stiffness matrix**: Assembled from element stiffness contributions.
- **Boundary conditions**: Applied by reducing the system or using penalty methods.
- **Eigenanalysis**: Natural frequencies found via eigenvalues of mass-normalized stiffness matrix.
- **Use Case**: Structural analysis, vibration modes, and design validation.
