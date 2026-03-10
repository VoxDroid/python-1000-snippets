# sample3.py
# parameterized test

import pytest

@pytest.mark.parametrize('a,b,expected', [(1,2,3),(0,0,0),(2,2,4)])
def test_add(a,b,expected):
    assert a+b == expected

if __name__ == '__main__':
    pytest.main([__file__])
