# sample2.py
# Logging to both console and file

import logging

if __name__ == '__main__':
    logger = logging.getLogger('sample2')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    fh = logging.FileHandler('sample2.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)

    logger.info('This will appear in console and file')
    logger.error('An error logged to both')
    print('Log written to sample2.log')
