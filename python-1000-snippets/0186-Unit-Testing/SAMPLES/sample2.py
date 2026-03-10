# sample2.py
# test with setUp/tearDown and multiple assertions

import unittest

class Counter:
    def __init__(self):
        self.count = 0
    def incr(self):
        self.count += 1

class TestCounter(unittest.TestCase):
    def setUp(self):
        self.c = Counter()
    def test_initial(self):
        self.assertEqual(self.c.count, 0)
    def test_increment(self):
        self.c.incr()
        self.assertEqual(self.c.count, 1)

if __name__ == '__main__':
    unittest.main()
