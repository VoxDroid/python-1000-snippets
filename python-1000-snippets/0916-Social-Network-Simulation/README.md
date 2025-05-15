# Social Network Simulation

## Description
This snippet simulates information spread on a social network for a marketing firm, modeling viral content diffusion to optimize campaigns.

## Code
```python
# Social Network Simulation for information spread
# Note: Requires `networkx`, `numpy`. Install with `pip install networkx numpy`
try:
    import networkx as nx
    import numpy as np

    # Social network model
    class SocialNetwork:
        def __init__(self, spread_prob: float):
            # Initialize network and spread probability
            self.G = nx.watts_strogatz_graph(100, 4, 0.1)  # Small-world network
            self.spread_prob = spread_prob
            nx.set_node_attributes(self.G, False, 'informed')  # All uninformed
            self.G.nodes[0]['informed'] = True  # Initial spreader

        def step(self) -> None:
            # Simulate one time step of information spread
            new_informed = []
            for node in self.G.nodes:
                if self.G.nodes[node]['informed']:
                    for neighbor in self.G.neighbors(node):
                        if not self.G.nodes[neighbor]['informed'] and np.random.rand() < self.spread_prob:
                            new_informed.append(neighbor)
            for node in new_informed:
                self.G.nodes[node]['informed'] = True

        def simulate(self, steps: int) -> list:
            # Run simulation for given steps
            informed = []
            for _ in range(steps):
                self.step()
                informed.append(sum(1 for n in self.G.nodes if self.G.nodes[n]['informed']))
            return informed

    # Run social network simulation
    def run_social_simulation(spread_prob: float, steps: int) -> dict:
        # Simulate information spread
        network = SocialNetwork(spread_prob)
        return {'informed': network.simulate(steps)}

    # Example usage
    result = run_social_simulation(spread_prob=0.2, steps=20)
    print("Social network simulation result:", result['informed'][-1])
except ImportError:
    print("Mock Output: Social network simulation result: 50")
```

## Output
```
Mock Output: Social network simulation result: 50
```
*(Real output with `networkx`, `numpy`: `Social network simulation result: <number of informed nodes>`)*

## Explanation
- **Purpose**: Simulates information diffusion on a social network to study viral spread dynamics.
- **Real-World Use Case**: A marketing firm uses this to optimize social media campaigns by targeting influential nodes.
- **Code Breakdown**:
  - The `SocialNetwork` class models a small-world network with information spread.
  - The `step` method updates informed nodes based on spread probability.
  - The `run_social_simulation` function returns the number of informed nodes over time.
- **Technical Challenges**: Modeling realistic network structures, handling stochastic spread, and identifying influencers.
- **Integration**: Complements Agent-Based Modeling (Snippet 915) and Disease Spread Simulation (Snippet 914) for network dynamics.
- **Scalability**: O(n*e) complexity for n nodes and e edges per step; large networks require optimization.
- **Performance Metrics**: Accuracy depends on network topology; spread speed varies with connectivity.
- **Best Practices**: Use real social network data, validate with campaign metrics, and target key nodes.
- **Extensions**: Model content types or integrate with social media APIs.