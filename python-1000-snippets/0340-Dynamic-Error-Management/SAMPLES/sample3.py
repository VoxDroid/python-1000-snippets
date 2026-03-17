"""Collect multiple errors using a context manager."""

from contextlib import contextmanager
from typing import List


class ErrorCollector(Exception):
    def __init__(self, errors: List[str]):
        super().__init__("Multiple errors occurred")
        self.errors = errors


@contextmanager
def collect_errors():
    errors: List[str] = []
    try:
        yield errors
    finally:
        if errors:
            raise ErrorCollector(errors)


if __name__ == "__main__":
    try:
        with collect_errors() as errors:
            errors.append("Error A")
            errors.append("Error B")
    except ErrorCollector as e:
        print("Collected errors:", e.errors)
