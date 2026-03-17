# sample2.py
# Pytest fixture with module scope

try:
    import pytest  # type: ignore

    @pytest.fixture(scope="module")
    def shared_resource():
        return {"value": 0}

    def test_a(shared_resource):
        shared_resource["value"] = 1
        assert shared_resource["value"] == 1

    def test_b(shared_resource):
        assert shared_resource["value"] == 1

    if __name__ == "__main__":
        print("Run `pytest -q` to execute the tests")

except ImportError:
    if __name__ == "__main__":
        print("pytest not installed; install with `pip install pytest`")
