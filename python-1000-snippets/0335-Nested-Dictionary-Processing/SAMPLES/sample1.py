"""Extract values safely from a nested dictionary structure."""

from typing import Any, Dict, List


def extract_x_values(data: Dict[str, Dict[str, Any]]) -> List[Any]:
    # Safely access nested keys with .get() and filter out missing values
    return [inner.get("x") for inner in data.values() if isinstance(inner, dict) and "x" in inner]


if __name__ == "__main__":
    data = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}, "c": {"y": 5}}
    x_values = extract_x_values(data)
    print("X values:", x_values)
