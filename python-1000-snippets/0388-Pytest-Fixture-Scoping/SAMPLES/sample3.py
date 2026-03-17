# sample3.py
# Pytest fixture with session scope

try:
    import pytest  # type: ignore

    @pytest.fixture(scope="session")
    def session_resource():
        return {"initialized": True}

    def test_session_a(session_resource):
        assert session_resource["initialized"]

    def test_session_b(session_resource):
        assert session_resource["initialized"]

    if __name__ == "__main__":
        print("Run `pytest -q` to execute the tests")

except ImportError:
    if __name__ == "__main__":
        print("pytest not installed; install with `pip install pytest`")
