# sample2.py
# logging to both console and file

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('app.log')]
)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('writing to console and file')
    logger.error('an error occurred')
