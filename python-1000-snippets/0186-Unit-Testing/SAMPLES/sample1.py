# sample1.py
# basic test file demonstrating unittest

import unittest

# code under test

def add(a, b):
    return a + b

# tests

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
