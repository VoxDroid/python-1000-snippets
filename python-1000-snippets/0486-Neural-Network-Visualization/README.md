# Neural Network Visualization

## Description
This snippet demonstrates constructing and displaying neural network architecture data without external plotting libraries.

## Code
The sample scripts show:
- `sample1.py`: Build a simple feedforward network and print node/connection counts.
- `sample2.py`: Compute a forward pass with a hardcoded network.
- `sample3.py`: Render a textual layer visualization of a network.

## Output
`sample1.py` prints node and connection counts and sample connections.

`sample2.py` prints network input/output values after a forward pass.

`sample3.py` prints a textual layer representation, e.g.:
```
  O O O O
O O O O O O O O
  O O O O O O
    O O
```

## Explanation
- **Neural Network Visualization**: Represents network structure and data in a text-friendly way.
- **Logic**: Builds layers and connection lists, computes outputs, and renders textual diagrams.
- **Complexity**: O(n + e) for n neurons and e connections.
- **Use Case**: Useful for educational demos and understanding network topology without graphics libraries.
- **Best Practice**: Use consistent layer sizing, annotate node roles, and compare outputs across layers.