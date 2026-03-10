# sample2.py
# patch object method and check call args

import unittest
from unittest.mock import patch
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import dependency

class Foo:
    def run(self):
        return dependency.get_data()

class TestFoo(unittest.TestCase):
    def test_run(self):
        with patch('dependency.get_data', return_value='X') as mock_get:
            f = Foo()
            res = f.run()
            mock_get.assert_called_once()
            self.assertEqual(res, 'X')

if __name__ == '__main__':
    unittest.main()
