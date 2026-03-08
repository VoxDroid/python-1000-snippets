# sample3.py
# Calculate difference between two dates

from datetime import datetime

if __name__ == '__main__':
    a = input('First date (YYYY-MM-DD): ')
    b = input('Second date (YYYY-MM-DD): ')
    try:
        da = datetime.strptime(a, '%Y-%m-%d')
        db = datetime.strptime(b, '%Y-%m-%d')
        diff = db - da
        print('Difference:', diff.days, 'days')
    except ValueError:
        print('Invalid format')
