# Disease Spread Simulation

## Description
This snippet simulates disease spread on a network for a research institute, modeling contact-based transmission to study intervention impacts.

## Code
```python
# Disease Spread Simulation on a network
# Note: Requires `networkx`, `numpy`. Install with `pip install networkx numpy`
try:
    import networkx as nx
    import numpy as np

    # Network-based disease spread model
    class DiseaseNetwork:
        def __init__(self, beta: float, gamma: float):
            # Initialize transmission (beta) and recovery (gamma) rates
            self.beta = beta
            self.gamma = gamma
            self.G = nx.erdos_renyi_graph(100, 0.1)  # Random network
            nx.set_node_attributes(self.G, 'S', 'status')  # All susceptible
            self.G.nodes[0]['status'] = 'I'  # Initial infection

        def step(self) -> None:
            # Simulate one time step of disease spread
            new_status = {}
            for node in self.G.nodes:
                if self.G.nodes[node]['status'] == 'I':
                    # Spread to neighbors
                    for neighbor in self.G.neighbors(node):
                        if self.G.nodes[neighbor]['status'] == 'S' and np.random.rand() < self.beta:
                            new_status[neighbor] = 'I'
                    # Recover
                    if np.random.rand() < self.gamma:
                        new_status[node] = 'R'
            for node, status in new_status.items():
                self.G.nodes[node]['status'] = status

        def simulate(self, steps: int) -> dict:
            # Run simulation for given steps
            infected = []
            for _ in range(steps):
                self.step()
                infected.append(sum(1 for n in self.G.nodes if self.G.nodes[n]['status'] == 'I'))
            return {'infected': infected}

    # Run disease spread simulation
    def run_disease_simulation(beta: float, gamma: float, steps: int) -> dict:
        # Simulate disease spread on network
        model = DiseaseNetwork(beta, gamma)
        return model.simulate(steps)

    # Example usage
    result = run_disease_simulation(beta=0.1, gamma=0.05, steps=50)
    print("Disease spread simulation result:", result['infected'][-1])
except ImportError:
    print("Mock Output: Disease spread simulation result: 5")
```

## Output
```
Mock Output: Disease spread simulation result: 5
```
*(Real output with `networkx`, `numpy`: `Disease spread simulation result: <number of infected nodes>`)*

## Explanation
- **Purpose**: Simulates disease spread on a contact network to evaluate transmission dynamics and interventions.
- **Real-World Use Case**: A research institute uses this to test quarantine or vaccination strategies in a networked population.
- **Code Breakdown**:
  - The `DiseaseNetwork` class models a random network with SIR dynamics.
  - The `step` method updates node statuses (S, I, R) per time step.
  - The `run_disease_simulation` function returns infection counts over time.
- **Technical Challenges**: Modeling realistic networks, handling stochasticity, and scaling to large graphs.
- **Integration**: Complements Epidemiological Modeling (Snippet 913) and Social Network Simulation (Snippet 916) for network-based studies.
- **Scalability**: O(n*e) complexity for n nodes and e edges per step; large networks require sparse graph algorithms.
- **Performance Metrics**: Accuracy depends on network structure; peak infections vary with connectivity.
- **Best Practices**: Use realistic contact networks, validate with empirical data, and account for interventions.
- **Extensions**: Model heterogeneous networks or integrate with mobility data.