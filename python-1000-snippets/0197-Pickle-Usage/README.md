# Pickle Usage

## Description
This snippet demonstrates serializing and deserializing Python objects using `pickle`.

## Code
```python
import pickle

data = {"name": "Bob", "scores": [90, 85]}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
print("Loaded:", loaded_data)
```

## Output
```
Loaded: {'name': 'Bob', 'scores': [90, 85]}
```

## Explanation
- **Pickle Usage**: Uses `pickle.dump` to serialize a dictionary to a file and `pickle.load` to deserialize it.
- **Logic**: Saves and loads data to/from `data.pkl`.
- **Complexity**: O(n) for n bytes in the data.
- **Use Case**: Used for saving Python objects like models or caches.
- **Best Practice**: Avoid untrusted pickle files; use `with` for file handling; consider JSON for portability.