# sample3.py
# using MagicMock to simulate complex object

from unittest.mock import MagicMock

if __name__ == '__main__':
    db = MagicMock()
    db.query.return_value = ['row1', 'row2']
    print('results', db.query('SELECT'))
    db.query.assert_called_with('SELECT')
