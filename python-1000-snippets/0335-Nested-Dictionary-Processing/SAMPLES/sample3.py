"""Deep merge two nested dictionaries.

Values in the second dictionary override those in the first.
"""

from typing import Any, Dict


def deep_merge(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    result = dict(a)
    for key, value in b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


if __name__ == "__main__":
    base = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}
    override = {"a": {"z": 9}, "b": {"x": 30}}
    merged = deep_merge(base, override)
    print("Merged:", merged)
