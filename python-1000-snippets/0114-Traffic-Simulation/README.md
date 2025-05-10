# Traffic Simulation

## Description
This snippet simulates a simple traffic light system with cars arriving randomly and waiting during red lights.

## Code
```python
import random

def traffic_simulation(cycles, arrival_rate):
    cars_waiting = 0
    total_wait_time = 0
    green = True
    for t in range(cycles):
        if random.random() < arrival_rate:
            cars_waiting += 1
        if t % 10 == 0:  # Switch light every 10 time steps
            green = not green
        if not green:
            total_wait_time += cars_waiting
        elif green and cars_waiting > 0:
            cars_waiting -= min(cars_waiting, 2)  # 2 cars pass per green
    return total_wait_time / cycles

print("Average Wait Time:", traffic_simulation(100, 0.3))
```

## Output
```
Average Wait Time: 1.23
```
*(Output varies due to randomness)*

## Explanation
- **Traffic Simulation**: Models cars arriving and waiting at a traffic light; green/red cycles every 10 steps.
- **Logic**: Cars accumulate during red; up to 2 pass during green.
- **Complexity**: O(cycles) time.
- **Use Case**: Used in urban planning or traffic flow analysis.
- **Best Practice**: Add multiple lanes or realistic arrival patterns.