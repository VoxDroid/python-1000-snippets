# sample1.py
# Core logic used for branch coverage analysis.


def check_value(x: int) -> str:
    """Return a classification for the provided integer.

    This function is intentionally written with multiple branches
    to make it easy to exercise branch coverage tools.
    """

    if x > 0:
        return "Positive"
    elif x == 0:
        return "Zero"
    else:
        return "Negative"


def main() -> None:
    for value in (-1, 0, 1):
        print(f"{value} -> {check_value(value)}")


if __name__ == "__main__":
    main()
