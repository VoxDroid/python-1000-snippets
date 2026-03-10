# sample1.py
# basic patch decorator example

import unittest
from unittest.mock import patch
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import dependency


def process_data():
    return f"Processed: {dependency.get_data()}"

class TestProcessData(unittest.TestCase):
    @patch('dependency.get_data')
    def test_process(self, mock_get):
        mock_get.return_value = 'Mocked'
        self.assertEqual(process_data(), 'Processed: Mocked')

if __name__ == '__main__':
    unittest.main()
