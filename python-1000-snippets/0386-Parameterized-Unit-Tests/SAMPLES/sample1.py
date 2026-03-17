# sample1.py
# Example pytest parameterized test (requires pytest)


def add(a, b):
    return a + b


try:
    import pytest  # type: ignore

    @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
    def test_add(a, b, expected):
        assert add(a, b) == expected

    if __name__ == "__main__":
        print("pytest is available. Run: pytest -q")

except ImportError:
    if __name__ == "__main__":
        print("pytest not installed. Install with: pip install pytest")
