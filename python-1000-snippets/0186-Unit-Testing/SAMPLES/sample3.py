# sample3.py
# demonstrating test discovery with a named test_* file

# simply reuse sample1's tests by importing
from sample1 import TestAdd

if __name__ == '__main__':
    import unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdd)
    unittest.TextTestRunner().run(suite)
