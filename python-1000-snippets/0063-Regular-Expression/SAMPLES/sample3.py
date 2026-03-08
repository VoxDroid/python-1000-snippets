# sample3.py
# Replace sensitive words in text using re.sub

import re

if __name__ == '__main__':
    text = 'This is bad and really horrible.'
    censored = re.sub(r'bad|horrible', '***', text)
    print('original:', text)
    print('censored:', censored)
