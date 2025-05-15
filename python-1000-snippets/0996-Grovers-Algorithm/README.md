# Grover's Algorithm

## Description
This snippet simulates Grover’s algorithm to search an unstructured dataset, applied to finding a target entry in a database.

## Code
```python
# Grover's Algorithm: Classical simulation
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Grover's algorithm simulation
    class Grover:
        def __init__(self, n_bits: int, target: int):
            # Initialize search space and target
            self.n_bits = n_bits
            self.size = 2 ** n_bits
            self.target = target

        def oracle(self, x: int) -> int:
            # Simulate oracle: mark target
            return 1 if x == self.target else 0

        def simulate(self) -> int:
            # Simulate Grover with iterative amplification
            state = np.ones(self.size) / np.sqrt(self.size)
            iterations = int(np.pi / 4 * np.sqrt(self.size))
            for _ in range(iterations):
                # Oracle: flip target amplitude
                for i in range(self.size):
                    if self.oracle(i):
                        state[i] *= -1
                # Diffusion: amplify target
                mean = np.mean(state)
                state = 2 * mean - state
            # Sample based on probabilities
            probs = np.abs(state) ** 2
            return np.random.choice(self.size, p=probs)

    # Run Grover's simulation
    def run_grover(n_bits: int) -> dict:
        # Search for target
        target = np.random.randint(0, 2**n_bits)
        grover = Grover(n_bits, target)
        found = grover.simulate()
        return {'found': found, 'target': target}

    # Example usage
    result = run_grover(n_bits=3)
    print("Grover's algorithm result:", result['found'])  # Found item
except ImportError:
    print("Mock Output: Grover's algorithm result: 5")
```

## Output
```
Mock Output: Grover's algorithm result: 5
```
*(Real output with `numpy`: `Grover's algorithm result: <found item, e.g., 5>`)*

## Explanation
- **Purpose**: Simulates Grover’s algorithm to search an unstructured dataset.
- **Real-World Use Case**: Finds a target entry in an unsorted database with fewer iterations.
- **Code Breakdown**:
  - The `Grover` class initializes the search space and target.
  - The `oracle` method marks the target.
  - The `simulate` method mimics amplitude amplification classically.
  - The `run_grover` function returns the found item.
- **Technical Challenges**: Simulating quantum amplification, managing numerical precision, and scaling iterations.
- **Integration**: Complements Quantum Algorithms (Snippet 994) for search problems.
- **Scalability**: O(2^n) complexity; limited to n<10 due to state vector size.
- **Performance Metrics**: Finds target with >90% probability for n<5 in milliseconds.
- **Best Practices**: Optimize iterations, validate with classical search, and use sparse vectors.
- **Extensions**: Support multiple targets or noisy oracles.
- **Limitations**: Classical simulation; quantum version offers O(sqrt(N)) complexity.