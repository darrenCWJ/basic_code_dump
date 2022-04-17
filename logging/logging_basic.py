import logging

logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the warning
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelnames)s - %(message)s')

stream_h.setFormatter(formatter) 
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)



