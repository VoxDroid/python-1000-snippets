"""Retry a transient operation with exponential backoff."""

import random
import time


class TransientError(Exception):
    pass


def unreliable_operation() -> str:
    if random.random() < 0.7:
        raise TransientError("Temporary failure")
    return "success"


def retry(func, retries: int = 3, backoff: float = 0.5):
    for attempt in range(1, retries + 1):
        try:
            return func()
        except TransientError as e:
            if attempt == retries:
                raise
            time.sleep(backoff * attempt)


if __name__ == "__main__":
    random.seed(42)
    try:
        result = retry(unreliable_operation, retries=5, backoff=0.1)
        print("Operation succeeded after retries:", result)
    except TransientError as e:
        print("Operation failed after retries:", str(e))
