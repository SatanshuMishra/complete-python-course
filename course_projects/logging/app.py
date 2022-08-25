from datetime import date
import logging

logging.basicConfig(
  format='%(asctime)s %(levelname)-8s [%(filename)s: %(lineno)d] %(message)s',
  datefmt='%d-%m-%y %H:%M:%S', 
  level=logging.DEBUG,
  filename='logs.txt'
)

logger = logging.getLogger('example')

logger.info('This will not show up.')
logger.warning('This will')
logger.debug('This is a debug message')
logger.critical('This is a critical error!')

"""
LEVELS OF LOGS:

DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
# BECOMES A CHILD LOGGER OF LOGGER WITH NAME 'example'
logger = logging.getLogger('example.data')