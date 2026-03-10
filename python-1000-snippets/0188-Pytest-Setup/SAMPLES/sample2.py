# sample2.py
# test with fixtures

import pytest

@ pytest.fixture

def nums():
    return [1,2,3]


def test_sum(nums):
    assert sum(nums) == 6

if __name__ == '__main__':
    pytest.main([__file__])
