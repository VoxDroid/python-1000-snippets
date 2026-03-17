"""Process a list of inputs and collect errors instead of failing fast."""

from typing import List, Tuple


def safe_divide(x: float) -> Tuple[float, str]:
    try:
        return 10.0 / x, ""
    except ZeroDivisionError:
        return 0.0, "Division by zero"


def process_values(values: List[float]) -> Tuple[List[float], List[str]]:
    results, errors = [], []
    for v in values:
        res, err = safe_divide(v)
        results.append(res)
        if err:
            errors.append(err)
    return results, errors


if __name__ == "__main__":
    values = [2, 0, 3]
    results, errors = process_values(values)
    print("Results:", results, "Errors:", errors)
