import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format
logger = logging.getLogger("a_name_here")

logger.debug('debug message')
logger.info('info message')