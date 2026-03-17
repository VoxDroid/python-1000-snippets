"""Traverse a nested dictionary recursively to collect full key paths."""

from typing import Any, Dict, List


def collect_nested_keys(data: Dict[str, Any], parent: str = "") -> List[str]:
    keys = []
    for k, v in data.items():
        full_key = f"{parent}.{k}" if parent else k
        if isinstance(v, dict):
            keys.extend(collect_nested_keys(v, full_key))
        else:
            keys.append(full_key)
    return keys


if __name__ == "__main__":
    nested = {"a": {"b": {"c": 1}, "d": 2}, "e": 3}
    keys = collect_nested_keys(nested)
    print("Nested keys:", keys)
