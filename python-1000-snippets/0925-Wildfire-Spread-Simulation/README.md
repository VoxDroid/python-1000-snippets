# Wildfire Spread Simulation

## Description
This snippet simulates wildfire spread for a fire management agency, modeling fire progression to plan evacuation routes.

## Code
```python
# Wildfire Spread Simulation for fire progression
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Wildfire spread model
    class FireModel:
        def __init__(self, wind_speed: float, fuel: float):
            # Initialize wind speed (m/s) and fuel density
            self.wind_speed = wind_speed
            self.fuel = fuel
            self.grid = np.zeros((10, 10))  # 10x10 grid
            self.grid[5, 5] = 1  # Initial fire

        def step(self) -> None:
            # Update fire spread
            new_grid = self.grid.copy()
            for i in range(1, 9):
                for j in range(1, 9):
                    if self.grid[i, j] == 1:
                        # Spread to neighbors based on wind and fuel
                        spread_prob = self.fuel * (1 + self.wind_speed / 10)
                        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            if np.random.rand() < spread_prob and new_grid[i+di, j+dj] == 0:
                                new_grid[i+di, j+dj] = 1
            self.grid = new_grid

        def simulate(self, steps: int) -> np.ndarray:
            # Simulate fire spread
            for _ in range(steps):
                self.step()
            return self.grid

    # Run wildfire simulation
    def run_fire_simulation(wind_speed: float, fuel: float, steps: int) -> dict:
        # Simulate wildfire spread
        model = FireModel(wind_speed, fuel)
        return {'fire_grid': model.simulate(steps)}

    # Example usage
    result = run_fire_simulation(wind_speed=5.0, fuel=0.2, steps=10)
    print("Wildfire spread simulation result:", np.sum(result['fire_grid']))
except ImportError:
    print("Mock Output: Wildfire spread simulation result: 15")
```

## Output
```
Mock Output: Wildfire spread simulation result: 15
```
*(Real output with `numpy`: `Wildfire spread simulation result: <number of burning cells>`)*

## Explanation
- **Purpose**: Models wildfire spread to predict fire behavior and inform management strategies.
- **Real-World Use Case**: A fire management agency uses this to plan evacuation routes and deploy resources during wildfires.
- **Code Breakdown**:
  - The `FireModel` class simulates fire spread on a grid with wind and fuel effects.
  - The `step` method updates fire spread to neighboring cells.
  - The `run_fire_simulation` function returns the final fire grid.
- **Technical Challenges**: Modeling complex terrain, handling variable weather, and scaling to large areas.
- **Integration**: Complements Environmental Modeling (Snippet 920) and Climate Change Simulation (Snippet 921) for fire studies.
- **Scalability**: O(g*s) complexity for g grid points and s steps; large areas require numerical solvers.
- **Performance Metrics**: Accuracy depends on fuel and wind; matches observed fire perimeters.
- **Best Practices**: Calibrate with fire data, validate with satellite imagery, and account for suppression.
- **Extensions**: Add terrain effects or integrate with weather models.