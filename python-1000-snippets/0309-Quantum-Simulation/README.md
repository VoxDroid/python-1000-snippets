# Quantum Simulation

## Description
This snippet implements basic quantum state simulation using NumPy for state vectors and gate operations. It does not require external quantum SDKs.

## Files
- `SAMPLES/sample1.py`: Simulates a single-qubit Hadamard gate and computes outcome probabilities.
- `SAMPLES/sample2.py`: Simulates a two-qubit circuit with Hadamard and CNOT to create a Bell state.
- `SAMPLES/sample3.py`: Simulates time evolution of a two-level system under a Hamiltonian.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
Probabilities: {'0': 0.50, '1': 0.50}
Bell state probabilities: {'00': 0.50, '11': 0.50}
Final state amplitudes: [0.71+0.00j 0.71+0.00j]
```

## Explanation
- **State vector**: Represents the amplitude of each computational basis state.
- **Quantum gates**: Modeled as unitary matrices applied to state vectors.
- **Measurement**: Computes probabilities from amplitudes.
- **Use Case**: Experiment with quantum algorithms and small-scale simulations.
