# Queue Simulation

## Description
This snippet simulates a single-server queue with random arrivals and service times to compute average wait time.

## Code
```python
import random

def queue_simulation(arrival_rate, service_rate, time_steps):
    queue = []
    wait_times = []
    current_time = 0
    serving_until = 0
    
    for t in range(time_steps):
        if random.random() < arrival_rate:
            queue.append(t)
        if t >= serving_until and queue:
            arrival_time = queue.pop(0)
            wait_times.append(t - arrival_time)
            serving_until = t + random.expovariate(service_rate)
    
    return sum(wait_times) / len(wait_times) if wait_times else 0

arrival_rate = 0.1
service_rate = 0.2
print("Average Wait Time:", queue_simulation(arrival_rate, service_rate, 1000))
```

## Output
```
Average Wait Time: 4.823529411764706
```
*(Output varies due to randomness)*

## Explanation
- **Queue Simulation**: Models customers arriving and being served; tracks wait times.
- **Parameters**: `arrival_rate` (probability of arrival), `service_rate` (exponential service time).
- **Complexity**: O(time_steps) time.
- **Use Case**: Used in operations research, call centers, or network modeling.
- **Best Practice**: Increase `time_steps` for accuracy; add metrics like queue length.