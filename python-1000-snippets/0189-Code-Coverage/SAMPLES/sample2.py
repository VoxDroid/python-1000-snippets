# sample2.py
# a simple pytest test (run coverage via CLI separately)

def multiply(a, b):
    return a * b


def test_multiply():
    assert multiply(3, 4) == 12


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])


