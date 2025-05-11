# Policy Gradient

## Description
This snippet demonstrates a simple policy gradient method using `tensorflow`.

## Code
```python
# Note: Requires `tensorflow`. Install with `pip install tensorflow`
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    import numpy as np
    model = Sequential([Dense(2, input_dim=2, activation="softmax")])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")
    states = np.random.random((100, 2))
    actions = np.random.randint(0, 2, 100)
    rewards = np.random.random(100)
    model.fit(states, actions, sample_weight=rewards, epochs=1, verbose=0)
    print("Policy trained")
except ImportError:
    print("Mock Output: Policy trained")
```

## Output
```
Mock Output: Policy trained
```
*(Real output with `tensorflow`: `Policy trained`)*

## Explanation
- **Policy Gradient**: Trains a policy network to select actions based on states.
- **Logic**: Uses a softmax policy and updates based on rewards.
- **Complexity**: O(n*d*i) for n samples, d dimensions, i epochs.
- **Use Case**: Used for continuous or complex action spaces in RL.
- **Best Practice**: Use advantage normalization; stabilize gradients; tune learning rate.