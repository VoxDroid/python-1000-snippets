"""Validate numeric input with a custom exception."""

class InvalidInputError(Exception):
    """Raised when input validation fails."""


def check_positive(x: int) -> int:
    if x <= 0:
        raise InvalidInputError("Input must be positive")
    return x


if __name__ == "__main__":
    try:
        print("Result:", check_positive(5))
        print("Result:", check_positive(-1))
    except InvalidInputError as e:
        print("Error:", str(e))
