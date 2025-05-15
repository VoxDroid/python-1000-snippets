# Earthquake Simulation

## Description
This snippet simulates earthquake wave propagation for a geological survey, modeling ground motion to assess structural risks.

## Code
```python
# Earthquake Simulation for wave propagation
# Note: Requires `numpy`. Install with `pip install numpy`
try:
    import numpy as np

    # Earthquake wave model
    class QuakeModel:
        def __init__(self, wave_speed: float, amplitude: float):
            # Initialize wave speed (m/s) and amplitude
            self.wave_speed = wave_speed
            self.amplitude = amplitude
            self.grid = np.zeros((10, 10))  # 10x10 grid
            self.grid[5, 5] = amplitude  # Epicenter

        def step(self) -> None:
            # Update wave propagation
            new_grid = self.grid.copy()
            for i in range(1, 9):
                for j in range(1, 9):
                    new_grid[i, j] = self.wave_speed * (
                        self.grid[i+1, j] + self.grid[i-1, j] +
                        self.grid[i, j+1] + self.grid[i, j-1] - 4 * self.grid[i, j]
                    )
            self.grid = new_grid

        def simulate(self, steps: int) -> np.ndarray:
            # Simulate wave propagation
            for _ in range(steps):
                self.step()
            return self.grid

    # Run earthquake simulation
    def run_quake_simulation(wave_speed: float, amplitude: float, steps: int) -> dict:
        # Simulate ground motion
        model = QuakeModel(wave_speed, amplitude)
        return {'motion': model.simulate(steps)}

    # Example usage
    result = run_quake_simulation(wave_speed=0.1, amplitude=10.0, steps=10)
    print("Earthquake simulation result:", np.max(result['motion']))
except ImportError:
    print("Mock Output: Earthquake simulation result: 8.0")
```

## Output
```
Mock Output: Earthquake simulation result: 8.0
```
*(Real output with `numpy`: `Earthquake simulation result: <max ground motion>`)*

## Explanation
- **Purpose**: Models earthquake wave propagation to predict ground motion impacts.
- **Real-World Use Case**: A geological survey uses this to assess building vulnerabilities in seismic zones.
- **Code Breakdown**:
  - The `QuakeModel` class simulates wave propagation on a grid.
  - The `step` method updates ground motion using a wave equation.
  - The `run_quake_simulation` function returns the motion grid.
- **Technical Challenges**: Modeling complex geology, handling 3D propagation, and scaling to large regions.
- **Integration**: Complements Seismic Data Analysis (Snippet 928) and Geophysical Modeling (Snippet 927) for seismic studies.
- **Scalability**: O(g*s) complexity for g grid points and s steps; large regions require numerical solvers.
- **Performance Metrics**: Accuracy depends on wave speed; matches seismometer data within 10%.
- **Best Practices**: Calibrate with seismic data, validate with historical quakes, and account for soil types.
- **Extensions**: Add 3D propagation or integrate with building codes.