"""Flatten a nested dictionary into dot-delimited keys."""

from typing import Any, Dict, Generator, Tuple


def flatten_dict(d: Dict[str, Any], parent: str = "") -> Generator[Tuple[str, Any], None, None]:
    for k, v in d.items():
        key = f"{parent}.{k}" if parent else k
        if isinstance(v, dict):
            yield from flatten_dict(v, key)
        else:
            yield key, v


if __name__ == "__main__":
    data = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}
    flat = dict(flatten_dict(data))
    print("Flattened:", flat)
