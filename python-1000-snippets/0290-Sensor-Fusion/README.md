# Sensor Fusion

## Description
This snippet demonstrates sensor fusion using a weighted average of two sensors.

## Code
```python
import numpy as np
sensor1 = np.random.normal(10, 1, 10)  # Sensor 1: mean 10, std 1
sensor2 = np.random.normal(10, 2, 10)  # Sensor 2: mean 10, std 2
w1, w2 = 0.67, 0.33  # Weights based on inverse variance
fused = w1 * sensor1 + w2 * sensor2
print("Fused Mean:", np.mean(fused))
```

## Output
```
Fused Mean: 10.02
```

## Explanation
- **Sensor Fusion**: Combines two sensor readings to improve accuracy.
- **Logic**: Weights sensors by inverse variance and computes a weighted average.
- **Complexity**: O(n) for n measurements.
- **Use Case**: Used for combining GPS, IMU, or other sensor data.
- **Best Practice**: Use Kalman filter for dynamics; validate weights; handle outliers.