# sample1.py
# Pytest fixture with function scope

try:
    import pytest  # type: ignore

    @pytest.fixture(scope="function")
    def resource():
        return {"counter": 0}

    def test_increment(resource):
        resource["counter"] += 1
        assert resource["counter"] == 1

    def test_increment_again(resource):
        resource["counter"] += 1
        assert resource["counter"] == 1

    if __name__ == "__main__":
        print("Run `pytest -q` to execute the tests")

except ImportError:
    if __name__ == "__main__":
        print("pytest not installed; install with `pip install pytest`")
