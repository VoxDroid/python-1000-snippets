# Traffic Simulation

## Description
This snippet simulates a simple traffic light system with cars arriving randomly and waiting during red lights.

## Code
```python
import random

def traffic_simulation(cycles, arrival_rate, green_duration=10, cars_per_green=2, seed=None):
    """Simulate cars arriving at a single traffic light.

    * `cycles` — number of time steps to run
    * `arrival_rate` — probability a new car arrives at each step
    * `green_duration` — number of steps light stays the same before toggling
    * `cars_per_green` — cars that can pass when light turns green
    * `seed` — optional RNG seed for reproducibility

    Returns average waiting cars per cycle.
    """
    if seed is not None:
        random.seed(seed)
    cars_waiting = 0
    total_wait_time = 0
    green = True
    for t in range(cycles):
        if random.random() < arrival_rate:
            cars_waiting += 1
        if t % green_duration == 0:  # switch light periodically
            green = not green
        if not green:
            total_wait_time += cars_waiting
        elif green and cars_waiting > 0:
            cars_waiting -= min(cars_waiting, cars_per_green)
    return total_wait_time / cycles


if __name__ == "__main__":
    print("Average Wait Time:", traffic_simulation(100, 0.3, seed=42))
```

## Output
```
Average Wait Time: 0.87
```
*(Output varies due to randomness; include a `seed` argument for stable results.)*

## Explanation
- **Traffic Simulation**: Models cars arriving randomly and queuing at a light that toggles every `green_duration` steps.
- **Parameters**: control arrival probability, cycle length, and throughput per green period.
- **Complexity**: O(cycles) time.
- **Use Case**: Demonstrates basic traffic flow; applicable in urban planning or discrete-event simulation tutorials.
- **Tip**: seed the RNG during testing; extend to multiple lanes or varying arrival distributions.