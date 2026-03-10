# sample1.py
# basic console logging example

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')

if __name__ == '__main__':
    main()
