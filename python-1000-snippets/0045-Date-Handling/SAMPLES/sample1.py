# sample1.py
# Show current date and various formatted strings

from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    print('now:', now)
    print('YYYY-MM-DD:', now.strftime('%Y-%m-%d'))
    print('Month/Day/Year:', now.strftime('%m/%d/%Y'))
    print('ISO format:', now.isoformat())
