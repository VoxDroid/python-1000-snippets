# sample3.py
# rotating file handler example

import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('rot.log', maxBytes=100, backupCount=2)
logging.basicConfig(level=logging.INFO, handlers=[handler], format='%(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    for i in range(20):
        logger.info(f'line {i}')
    print('Check rot.log and backups for rotation')
