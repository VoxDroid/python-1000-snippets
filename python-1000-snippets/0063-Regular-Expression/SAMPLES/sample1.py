# sample1.py
# Extract all numbers from a string using findall

import re

if __name__ == '__main__':
    text = "Order 66 cost $99 and 100 units"
    nums = re.findall(r'\d+', text)
    print('found numbers:', nums)
