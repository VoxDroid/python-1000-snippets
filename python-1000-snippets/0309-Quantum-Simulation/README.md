# Quantum Simulation

## Description
This snippet demonstrates a simple quantum circuit simulation using `qiskit`.

## Code
```python
# Note: Requires `qiskit`. Install with `pip install qiskit`
try:
    from qiskit import QuantumCircuit, Aer, execute
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Hadamard gate
    qc.measure(0, 0)
    simulator = Aer.get_backend("qasm_simulator")
    result = execute(qc, simulator, shots=100).result()
    counts = result.get_counts()
    print("Measurement Counts:", counts)
except ImportError:
    print("Mock Output: Measurement Counts: {'0': 50, '1': 50}")
```

## Output
```
Mock Output: Measurement Counts: {'0': 50, '1': 50}
```
*(Real output with `qiskit`: `Measurement Counts: {'0': ~50, '1': ~50}`)*

## Explanation
- **Quantum Simulation**: Simulates a single qubit with a Hadamard gate.
- **Logic**: Applies a gate, measures, and counts outcomes.
- **Complexity**: O(s) for s shots (simulator varies).
- **Use Case**: Used for quantum algorithm development.
- **Best Practice**: Use real quantum hardware; handle noise; validate circuits.