# sample3.py
# Using a named logger in a module-like fashion

import logging

logger = logging.getLogger('myapp.module')

def do_something():
    logger.info('Doing something important')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(name)s - %(levelname)s - %(message)s')
    do_something()
